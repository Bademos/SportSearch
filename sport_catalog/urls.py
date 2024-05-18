from django.urls import path, re_path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('test/',views.test, name="test" ),
    path('events/', views.AllEventsListView.as_view(), name="all_events" ),
    path('sportsmen/', views.AllSportUsers.as_view(), name="all_sportsmen" ),
    path('managers/', views.AllManagerUsers.as_view(), name="all_managers" ),
    path('reviews/', views.AllReviewsListView.as_view(), name="all_reviews" ),

    re_path(r'^myEvents/$', views.EventsByUserListView.as_view(), name='my-events'),
    re_path(r'^myReviews/$', views.ReviewsByUserListView.as_view(), name='my-reviews'),
    re_path(r'^myComplaints/$', views.ComplaintsByUserListView.as_view(), name='my-complaints'),
    re_path(r'^event/(?P<pk>[0-9a-f-]+)$', views.EventDetailedView.as_view(), name='event-detail'),
    re_path(r'^review/(?P<pk>[0-9a-f-]+)$', views.ReviewDetailedView.as_view(), name='review-detail'),
    re_path(r'^complaint/(?P<pk>[0-9a-f-]+)$', views.ComplaintsDetailedView.as_view(), name='complaint-detail'),
    
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^edit/$', views.edit, name='edit'),

    re_path(r'^sportsman/(?P<pk>[0-9a-f-]+)$', views.SportuserDetailedView.as_view(), name='sportuser-detail'),

]

urlpatterns += [
    re_path(r'^event/create/$', views.EventCreate.as_view(), name='event_create'),
   # re_path(r'^event/(?P<pk>[0-9a-f-]+)/update/$', views.AuthorUpdate.as_view(), name='event_update'),
    #re_path(r'^event/(?P<pk>[0-9a-f-]+)/delete/$', views.AuthorDelete.as_view(), name='event_delete'),
]

urlpatterns += [
    re_path(r'^review/create/$', views.ReviewCreate.as_view(), name='review_create'),
   # re_path(r'^review/(?P<pk>[0-9a-f-]+)/update/$', views.ReviewUpdate.as_view(), name='review_update'),
    #re_path(r'^review/(?P<pk>[0-9a-f-]+)/delete/$', views.ReviewDelete.as_view(), name='review_delete'),
]
