from django.urls import path
from . import views
app_name = 'wall'
urlpatterns = [
    path('wall', views.index, name='root'),
    path('message/create/<user_email>', views.message_create, name='message_create'),
    path('message/delete/<user_email>/<int:message_id>', views.message_delete, name='message_delete'),
    path('comment/create/<user_email>/<int:message_id>', views.comment_create, name='comment_create'),
]