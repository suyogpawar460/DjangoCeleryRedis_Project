from django.urls import path

from .views import GenerateRandomUserView, UsersListView

urlpatterns = [
    path('users/', UsersListView.as_view(), name='users_list'),
    path('generate/', GenerateRandomUserView.as_view(), name='generate')
]