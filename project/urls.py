from django.conf.urls import url

from project import views


urlpatterns = [
    url(r'^project/create/$', views.ProjectCreateView.as_view(), name='project-create'),
    url(r'^project/list/$', views.ProjectListView.as_view(), name='project-list'),
    url(r'^project/detail/(?P<pk>\d+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^project/update/(?P<pk>\d+)/$', views.ProjectUpdateView.as_view(), name='project-update'),
    url(r'^project/delete/(?P<pk>\d+)/$', views.ProjectDeleteView.as_view(), name='project-delete'),
]
