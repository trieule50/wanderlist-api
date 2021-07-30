from django.db import models


# Create your models here.

class State(models.Model):
    name = models.CharField(max_length=250)
    state_flag = models.TextField()
    owner = models.ForeignKey('users.User', related_name='states', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Recommendation(models.Model):
    title = models.CharField(max_length=500)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='recommendations')
    body = models.TextField() 
    photo_url = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'users.User', related_name='recommendations', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title