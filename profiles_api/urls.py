from django.urls import path
from profiles_api import views




urlpatterns = [
    path('hello-view/', views.HelloApiview.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('hello-viewset/',views.HelloViewSet.as_view({'get':'list'})),
    path('profile/', views.UserProfileViewSet.as_view({'get':'list', 'post':'create'})),
    path('feed/',views.UserProfileFeedViewSet.as_view({'get':'list'})),
    path('chair/<int:id>/',views.SillasProfileViewSet.as_view({'get':'list', 'post':'create', 'delete': 'destroy'})),
]
