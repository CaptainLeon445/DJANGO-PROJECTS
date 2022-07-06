from django.urls import path
from loginapp import views
from django.contrib.auth import views as auth_views

app_name = 'loginapp'
urlpatterns=[
    path('SignUp/',views.create_account,name="create_account"),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name="password_reset"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name='password_change'),
    path('password_change_done/',auth_views.PasswordChangeDoneView.as_view(),name="password_change_done"),
    path('',views.welcome,name='welcome'),
    path('save_password/',views.create_pwd,name="create_pwd"),
    path('list_password/',views.pwd_list,name="pwd_list"),
    path('<int:id>/delete/',views.delete,name="delete"),
    path('<int:id>/edit/',views.Edit,name="edit"),
    path('<int:year>/<int:day>/<int:month>/<slug:pwd>/<int:id>/',views.pwd_detail,name="pwd_detail"),
    #path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
   
]