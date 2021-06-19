from django.db import models
from django.db.models.fields import related
from login.models import User

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name= "messages", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # message_comments = a list of comments associated with a given message

    def __repr__ (self):
        return f"<Message: {self.id} {self.message}>"

class Comment(models.Model):
    comment = models.TextField()
    message = models.ForeignKey(Message, related_name= "message_comments", on_delete= models.CASCADE)
    user = models.ForeignKey(User, related_name= "user_comments", on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__ (self):
        return f"<Comment: {self.id} {self.comment}>"





# Create your models here.
