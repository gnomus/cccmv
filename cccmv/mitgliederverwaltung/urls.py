from django.conf.urls import patterns, url

from cccmv.mitgliederverwaltung import views

urlpatterns = patterns('',
    url(r'^mitglieder/(?P<memberId>\d+)/loeschen/$', views.deleteMember, name='deleteMember'),
    url(r'^mitglieder/(?P<memberId>\d+)/$', views.showMember, name='showMember'),
    url(r'^mitglieder/neu/$', views.createMember, name='newMember'),
    url(r'^mitglieder/$', views.listMember, name='listMember'),
    url(r'^$', views.index, name='index'),
)