from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from post.models import BlogPost
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator


class BlogHome(ListView):
    model = BlogPost
    context_object_name = "post"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)

#@method_decorator(login_required, name="dispatch")
class BlogPostCreate(CreateView):
    model         = BlogPost
    template_name = "post/blogpost_create.html"
    fields        = ['title', 'content',]


class BlogPostUpdate(UpdateView):
    model              = BlogPost
    template_name      = "post/blogpost_edit.html"
    fields             = ['title', 'content', 'published',]


class BlogPostDelete(DeleteView):
    model              = BlogPost
    context_object_name = "post"
    success_url        = reverse_lazy('post:home')
    

class BlogPostDetail(DetailView):
    model               = BlogPost
    context_object_name = "post"


 