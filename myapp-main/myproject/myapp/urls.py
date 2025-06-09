from django.urls import path
from . import views
from .views import upload_file, owner_page

urlpatterns = [
    path('', views.upload_file, name='upload'),
    path('upload/', upload_file, name='upload_file'),
    path('owner/', owner_page, name='owner_page'),

]