from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.urls import reverse
from .models import Topic, Response
from django.shortcuts import render, redirect
from django.views.generic import View

class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        return Topic.objects.all()

class DetailView(generic.DetailView):
    model = Topic
    template_name = 'blog/detail.html'



class TopicCreate(CreateView):
    model = Topic
    fields = '__all__'

class TopicUpdate(UpdateView):
    model = Topic
    fields = '__all__'

class TopicDelete(DeleteView):
    model = Topic
    success_url = reverse_lazy('blog:index')



class ResponseCreate(CreateView):
    model = Response
    fields = '__all__'

class ResponseUpdate(UpdateView):
    model = Response
    fields = '__all__'

class ResponseDelete(DeleteView):
    model = Response
    success_url = reverse_lazy('blog:index')
