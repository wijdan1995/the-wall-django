from django.db import models
from login_app.models import User

class MessageManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["content"]) < 2:
            errors["content"] = "Message should be at least 2 characters"
        return errors
    def delete_validator(self, user_email, message_id):
        errors = {}
        user = User.objects.get(email=user_email)
        message =  self.get(id=message_id)
        if message not in user.messages.all():
            errors["message"] = "Message don't belong to this user"
        return errors

class Message(models.Model):
    content = models.TextField()
    written_by = models.ForeignKey(User, related_name="messages", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = MessageManager()

class CommentManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData["comment"]) < 2:
            errors["comment"] = "Comment should be at least 2 characters"
        return errors

class Comment(models.Model):
    comment = models.TextField()
    written_by = models.ForeignKey(User, related_name="comments", on_delete = models.CASCADE)
    written_on = models.ForeignKey(Message, related_name="comments", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = CommentManager()
    
