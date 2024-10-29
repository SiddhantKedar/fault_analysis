from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('upload/', views.upload_file_view, name='upload_file'),
    # path('success/', views.upload_success, name='upload_success'),
]