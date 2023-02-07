from django.urls import path, re_path
from . import views

# for multiple same names we use name-spacing

app_name = 'accounts'

urlpatterns = [
    # Named URL's
    path('signup/', views.signup_view, name="signup"),
]

