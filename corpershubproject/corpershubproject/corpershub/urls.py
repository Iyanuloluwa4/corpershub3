from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from .views import ConnectView, CheckItOutView, CommonFlexView, ProfileView

urlpatterns = [
    #path('', ConnectView.as_view(template_name='connect.html'), name='available_jobs'),
    path('', CommonFlexView.as_view(template_name='commonflex.html'), name='common_flex'),
    path('<int:pk>', CheckItOutView.as_view(template_name='check_it_out.html'), name='job'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
]