### app urls

from django.urls import path

from .views import MainPageView, StoryCreateView

urlpatterns = [
	path('', MainPageView.as_view(), name="main"),
	path('story/', StoryCreateView.as_view(), name="story"),
]