from django.shortcuts import render,HttpResponseRedirect
from django.urls import reverse , reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DetailView,DeleteView,View,TemplateView
from .models import Blog,Comment,Like,Love
from .forms import CommentForm
import uuid

# Create your views here.



class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'blog/my_blogs.html'




class CreateBlog(LoginRequiredMixin,CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = ('blog_title','blog_content','blog_pic','category')

    def form_valid(self,form):
        new_blog_obj = form.save(commit = False)
        new_blog_obj.author = self.request.user
        title = new_blog_obj.blog_title
        new_blog_obj.slug = title.replace(" ","-") +"--"+str(uuid.uuid4())
        new_blog_obj.save()

        return HttpResponseRedirect(reverse('index'))

class BlogList(ListView):
    context_object_name = 'blogs'
    model = Blog
    template_name = 'blog/blog_list.html'
    #queryset = Blog.objects.order_by('-publish_date')


def blog_details(request,pk):
    blog = Blog.objects.get(pk=pk)
    comment_form=CommentForm()
    already_liked = Like.objects.filter(blog=blog, user= request.user)
    if already_liked:
        liked = True
    else:
        liked = False
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.user = request.user
            comment.blog=blog
            comment.save()
            return HttpResponseRedirect(reverse('blog:details', kwargs={'pk':pk}))

    return render(request,'blog/blog_details.html',context={'blog':blog,'comment_form':comment_form,'liked':liked})


@login_required
def liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        liked_post = Like(blog=blog, user=user)
        liked_post.save()
    return HttpResponseRedirect(reverse('blog:details', kwargs={'pk':blog.pk}))

@login_required
def loved(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_loved = Love.objects.filter(blog=blog, user=user)
    if not already_loved:
        loved_post = Love(blog=blog, user=user)
        loved_post.save()
    return HttpResponseRedirect(reverse('blog:details', kwargs={'pk':blog.pk}))

@login_required
def unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('blog:details', kwargs={'pk':blog.pk}))

class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('blog_title','blog_content','blog_pic','category')
    template_name = 'blog/blog_edit.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog:details', kwargs={'pk':self.object.pk})
