from django.urls import path

from . import views

urlpatterns = [
    path('', views.list_request, name='list_request'),
    path('requests/new/', views.create_request, name='create_request'),
    path('requests/<int:pk>/', views.view_request, name='view_request'),
    path('requests/<int:pk>/edit/', views.update_request, name='update_request'),
    path('requests/<int:pk>/delete/', views.delete_request, name='delete_request'),
    path('archived_requests', views.list_archived_requests, name='list_archived_request'),
    path('requests/<int:pk>/archive', views.archive_request, name='archive_request'),
    path('requests/<int:pk>/new-comment/', views.create_comment, name='create_comment'),
    path('requests/<int:pk>/<int:comment_pk>/edit/', views.update_comment, name='update_comment'),
    path('requests/<int:pk>/<int:comment_pk>/delete/', views.delete_comment, name='delete_comment')
]
