from django.conf.urls import url

from team import views


urlpatterns = [
    url(r'^team/create/$', views.TeamCreateView.as_view(), name='team-create'),
    url(r'^team/list/$', views.TeamListView.as_view(), name='team-list'),
    url(r'^team/detail/(?P<pk>\d+)/$', views.TeamDetailView.as_view(), name='team-detail'),
    url(r'^team/update/(?P<pk>\d+)/$', views.TeamUpdateView.as_view(), name='team-update'),
    url(r'^team/delete/(?P<pk>\d+)/$', views.TeamDeleteView.as_view(), name='team-delete'),
]
