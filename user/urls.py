from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.register, name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.UserLogoutView.as_view(), name='logout'),
    path('profile/',views.profile, name='profile'),
    path('edit-profile/',views.editProfile, name='edit_profile'),
]