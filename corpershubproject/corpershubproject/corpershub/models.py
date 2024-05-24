from django.db import models
from django.contrib.auth.models import User


class WebPages(models.Model):
    name = models.CharField(max_length=20)
    link = models.CharField(max_length=60, unique=True)
    date_uploaded = models.DateTimeField(unique=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    corper_name = models.CharField(max_length=100, blank=True)
    location = models.CharField(max_length=200, blank=True)
    hub_id = models.CharField(max_length=200, blank=True)
    about_me = models.TextField(max_length=2000, blank=True)

    def __str__(self):
        return f"Profile '{self.user}'  for {self.corper_name}"


class CommonFlex(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.FileField(blank=True, upload_to='video')
    picture = models.ImageField(blank=True, upload_to='picture')
    vibes = models.TextField(max_length=400, blank=True)


    # class Meta:
    #   unique_together = ('user', 'vibes',)


    def __str__(self):
        return f"Flex '{self.picture}'  for {self.user}"


# class Flex(models.Model):
#   video = models.FileField(blank=True, upload_to='flex_video')
#  picture = models.ImageField(blank=True, upload_to='flex_picture')
# corper_name = models.CharField(max_length=2000)
# location = models.CharField(max_length=1290)
# vibes = models.TextField(max_length=3090)

# def __str__(self):
#   return self.corper_name


class Connect(models.Model):
    client = models.CharField(max_length=220)
    client_location = models.CharField(max_length=1000)
    job_title = models.CharField(max_length=220)
    job_description = models.TextField(max_length=2000)
    job_requirement = models.TextChoices
    due_delivery_time = models.DateTimeField()
    type_of_job = models.TextChoices
    verification_status = models.TextChoices
    link = models.CharField(max_length=60, unique=True)
    date_uploaded = models.DateTimeField(unique=True)

    def __str__(self):
        return self.client
