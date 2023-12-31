from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('create', views.create, name='create'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    path('<int:post_id>/comment/', views.post_comment, name='post_comment')
]