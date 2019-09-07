from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
    views.post_detail,
    name='post_detail'),
    
]