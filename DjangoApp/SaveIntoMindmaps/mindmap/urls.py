from django.conf.urls import url
from . import views

#TEMPLATE URLS!
app_name = 'mindmap'

urlpatterns = [
    url(r'^mindmap/', views.Mindmap, name='Mindmap'),
    url(r'^SaveUserSelection/', views.SaveUserSelection, name='SaveUserSelection'),
]
