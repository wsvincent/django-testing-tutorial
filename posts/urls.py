from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostPageView.as_view(), name='posts'),
]
