from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Comment,Post,Category
from .forms import CommentForm,sharepost
from django.core.mail import send_mail
from taggit.models import Tag
from django.db.models import Count
from django.http import JsonResponse
from .serializers import CategorySerializer,PostSerializer,CommentSerializer
# Create your views here.


def PostList(request, slug=None, tag_slug=None):
    category=None
    categories=Category.objects.all()
    posts =Post.objects.all()
    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])  
    # = Post.published.all()
    paginator = Paginator(posts, 2) # 3 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
         # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
            # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
  
    if slug:
        category=get_object_or_404(Category,slug=slug)
        posts =Post.objects.all()
        posts=posts.filter(category=category)
        paginator = Paginator(posts, 2) # 3 posts in each page
        page = request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range deliver last page of results
            posts = paginator.page(paginator.num_pages)
        
    context={
        'tag':tag,
        'Posts':posts,
        'categories':categories,
        'category':category
    }
    return render(request,'blog/postlist.html',context)

def PostDetail(request,id,slug):
    posts = get_object_or_404(Post, id=id,slug=slug)
    #similar posts
    # List of similar posts
    post_tags_ids = posts.tags.values_list('id', flat=True)
    similar_posts = Post.objects.filter(tags__in=post_tags_ids).exclude(id=posts.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-created')[:4]
     #list of active comments
    comments = Comment.objects.filter(post=posts)
    new_comment=None

    if request.method=="POST":
        #A comment was posted 
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            #create comment object but don't save to a database yet
            new_comment=comment_form.save(commit=False)
            #Assign the current post to the comment
            new_comment.post=posts
            #save the comment to the database
            new_comment.save()

    else:
        comment_form=CommentForm()
    context={
        'Post':posts,
        'form':comment_form,
        'comments':comments,
        'similar_posts':similar_posts
    }
    return render(request,'blog/postdetail.html',context)

def post_share(request, post_id,post_slug):
    post= get_object_or_404(Post, id=post_id,slug=post_slug)
    #post=Post.objects.filter(id=post_id)
    sent=False
    if request.method=="POST":
        share=sharepost(request.POST)
        if share.is_valid():
            cd=share.cleaned_data
            post_url = request.build_absolute_uri(post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" f"{cd['name']}'s comments: {cd['comment']}"
            
            send_mail(subject, message, 'admin@myblog.com', [cd['to']])
            sent = True

    else:
        share=sharepost()
    dict={
        'post':post,
        'form':share,
        'sent':sent}

    return render(request,"blog/sharepost.html",dict)