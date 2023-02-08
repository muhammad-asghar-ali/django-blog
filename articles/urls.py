from django.urls import path, re_path
from . import views

# for multiple same names we use name-spacing

app_name = 'articles'

urlpatterns = [
    # Named URL's
    path('', views.article_list, name="list"),
    path('create/', views.article_create, name='create'),
    # URL Parameters
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail")
]
