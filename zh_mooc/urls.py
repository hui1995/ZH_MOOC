"""zh_mooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve

import xadmin
from users.views import IndexView, ForgetPwdView, RegisterView, LoginView, AciveUserView, LogoutView, ResetView, \
    ModifyPwdView
from zh_mooc.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', xadmin.site.urls),
    url('^$', IndexView.as_view(), name="index"),
#富文本相关url
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'register/$',RegisterView.as_view(),name='register'),
    url('^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^course/',include('courses.urls',namespace='course')),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),

    url(r'^register/$',RegisterView.as_view(),name='register'),
    url(r'^active/(?P<active_code>.*)/$', AciveUserView.as_view(), name="user_active"),
    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace="org")),
]
#全局404页面配置
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'
