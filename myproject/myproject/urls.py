"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from afl_user import views
from afl_user import views as user_views
from django.contrib.auth import views as auth_views

# from django.conf.urls import handler404,handler500
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    # user section
    path('user/register',user_views.signup.as_view(),name="signup"),
    path('user/', user_views.login,name="login"),
    path('user/logout',auth_views.LogoutView.as_view(), name='logout'),
    path('reset/',user_views.PasswordResetView.as_view(),name='password_reset'),
	path('reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'),name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'),name='password_reset_confirm'),
	path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'),name='password_reset_complete'),	
    path('settings/password/', user_views.password_change,name='password_change'),
	path('settings/password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'),name='password_change_done'),
	path('settings/account/', user_views.UserUpdateView.as_view(), name='my_account'),
    path('error',views.error_view,name='error_view')
]
