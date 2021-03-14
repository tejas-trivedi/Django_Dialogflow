from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('chat/', views.chat_view, name='chat-home'),
    path('about/', views.about, name='about'),
    path('', views.index_view, name='index'),

]


