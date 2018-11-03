from django.urls import path

from .views import PostPageView

urlpatterns = [
    path('', PostPageView.as_view(), name='posts'),
]
