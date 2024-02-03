from django.urls import path
from .views import (
    HomeView,
    AboutView,
    ProductView,
    LoginView,
    SignupView,
    ContactView,
    NovelListView,
    NovelDetailView,
    NovelCreateView,
    NovelUpdateView,
    NovelDeleteView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('products/', ProductView.as_view(), name='products'),
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('novel/list/', NovelListView.as_view(), name='novel_list'),
    path('novel/<int:pk>/', NovelDetailView.as_view(), name='novel_detail'),
    path('novel/create/', NovelCreateView.as_view(), name='add_novel'),  # Added this line
    path('novel/<int:pk>/edit/', NovelUpdateView.as_view(), name='novel_edit'),
    path('novel/<int:pk>/delete/', NovelDeleteView.as_view(), name='novel_confirm_delete'),
]
