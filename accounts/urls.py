from django.urls import path, re_path
from . import views

# for multiple same names we use name-spacing

app_name = 'accounts'

urlpatterns = [
    # Named URL's
    path('signup/', views.signup_view, name="signup"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
]

