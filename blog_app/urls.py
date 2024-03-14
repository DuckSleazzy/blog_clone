from django.urls import path, include
from blog_app import views

urlpatterns = [
    path("", views.PostListView.as_view(),name='home'),
    path("about/", views.AboutView.as_view(),name='about'),
    path("post/new/", views.CreatePostView.as_view(),name='post_create'), # with this
    path("post/<pk>/", views.PostDetailView.as_view(),name='post_detail'), # swapped this
    path("post/<pk>/update/", views.UpdatePostView.as_view(),name='post_update'),
    path("post/<pk>/delete/", views.DeletePostView.as_view(),name='post_delete'),
    path("drafts/",views.DraftListView.as_view(),name='post_draft'),
    path("post/<pk>/comment/",views.add_comments,name='comment'),
    path("comment/<pk>/approve/",views.approve_comment,name='approve_comment'),
    path("comment/<pk>/remove/",views.remove_comment,name='remove_comment'),
    path("post/<pk>/publish/", views.publish_post,name='publish_post'),    
]