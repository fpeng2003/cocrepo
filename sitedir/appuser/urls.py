from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^userinfo', views.wechat, name='wechat'),
    url(r'allteams', views.allteams, name='allteams'),
    url(r'alltasks', views.alltasks, name='alltasks'),
    url(r'^team/(?P<teamid>\d+)/$', views.teams),
    url(r'^task/(?P<taskid>\d+)/$', views.taskdetail, name='taskdetail'),
    url(r'^setpersonid/(?P<personid>\d+)/$', views.setpersonid, name='setpersonid'),
    url(r'^getpersonid', views.getpersonid, name='getpersonid'),
    url(r'^profile$',views.getPersonalProfile,name = "no"),
    url(r'^profile/(?P<personid>\d+)/$', views.getProf, name='getPersonalProfile'),
     url(r'^education-history/(?P<personid>\d+)/$', views.EducationHistory, name='eduh'),
    url(r'^profile-settings', views.profilesettings, name='profile-settings'),
    url(r'^profile-save', views.savesettings, name='profile-settings'),
    url(r'education-save', views.educationhandle, name='handle'),
    url(r'employment-save', views.employmenthandle, name='handles'),
    url(r'^employment-history/(?P<personid>\d+)/$', views.EmploymentHistory, name='emph'),
]
