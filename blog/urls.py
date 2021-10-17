from django.urls import path
from . import views
urlpatterns= [ 
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts", views.AllPosts.as_view(), name="posts"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="posts-details")
]
