from django.conf.urls import url

from organization.views import TeacherListView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, \
    TeacherDetailView, OrgView,AddUserAskView

urlpatterns= [
url(r'^list/$', OrgView.as_view(), name="org_list"),
    url(r'^teacher/list/$', TeacherListView.as_view(), name="teacher_list"),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),

    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),



    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name="add_fav"),

    # 讲师列表页


    # 讲师详情页
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),



]

# }