from django.urls import path

from .views import (
    CustomerUserListAPIview,
    CustomeUserCreateAPIview,
    CustomeUserChangeAPIview,
    CustomeuserDeleteAPIview,
    CustomeUserDetailsAPIview,
)

app_name = "custome_user"

urlpatterns = [
    path('user-list/', CustomerUserListAPIview.as_view(), name='user_list'),
    path('user-create/', CustomeUserCreateAPIview.as_view(), name='user_create'),
    path('user-details/<int:id>/', CustomeUserDetailsAPIview.as_view(), name='user_detail'),
    path('user-change/<int:id>/', CustomeUserChangeAPIview.as_view(), name='change_user'),
    path('user-delete/<int:id>/', CustomeuserDeleteAPIview.as_view(), name='delete_user')
]
