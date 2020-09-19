from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('relations/', views.relations_index, name='index'),
  path('relations/<int:relation_id>/', views.relations_detail, name='detail'),
  path('relations/create/', views.RelationCreate.as_view(), name='relations_create'),
  path('relations/<int:pk>/update/', views.RelationUpdate.as_view(), name='relations_update'),
  path('relations/<int:pk>/delete/', views.RelationDelete.as_view(), name='relations_delete'),
  path('relations/<int:relation_id>/add_communication/', views.add_communication, name='add_communication'),
  path('relations/<int:relation_id>/add_photo/', views.add_photo, name='add_photo'),
  path('relations/<int:relation_id>/assoc_activity/<int:activity_id>/', views.assoc_activity, name='assoc_activity'),
  path('relations/<int:relation_id>/unassoc_activity/<int:activity_id>/', views.unassoc_activity, name='unassoc_activity'),
  path('activitys/', views.ActivityList.as_view(), name='activitys_index'),
  path('activitys/<int:pk>/', views.ActivityDetail.as_view(), name='activitys_detail'),
  path('activitys/create/', views.ActivityCreate.as_view(), name='activitys_create'),
  path('activitys/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activitys_update'),
  path('activitys/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activitys_delete'),
]