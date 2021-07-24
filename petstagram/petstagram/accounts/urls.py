from django.urls import path

from petstagram.accounts.views import login_user, register_user, logout_user, profile_details

urlpatterns = (
    path('register/', register_user, name='register'),
    path('login/', login_user, name='log in'),
    path('logout/', logout_user, name='log out'),
    path('profile/', profile_details, name='profile details')
)
