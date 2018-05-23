from django.db import models
from django.urls import reverse

class Topic(models.Model):
    topic_title = models.CharField(max_length=256)
    topic_subject = models.CharField(max_length=256)
    topic_logo = models.ImageField(default= " ", blank=True)

    def get_absolute_url(self):
        return reverse('blog:index');

    def __str__(self):
        return self.topic_title

class Response(models.Model):
    resp_topic = models.ForeignKey(Topic, on_delete=models.CASCADE, default= " ")
    resp_name = models.CharField(max_length=256, default = " ")
    resp_body = models.CharField(max_length=512)

    def get_absolute_url(self):
        return reverse('blog:detail', args=[str(self.resp_topic.id)]);

    def get_success_url(self):
        return reverse('blog:detail', args=[str(self.resp_topic.id)]);

    def __str__(self):
        return self.resp_name
