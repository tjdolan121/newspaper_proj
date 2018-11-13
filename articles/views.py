from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect  # NEW
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Comment
from .forms import CommentForm


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    login_url = 'login'
    paginate_by = 5


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article  # Added 'Comment'
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ('title', 'body', )
    login_url = 'login'

    def form_valid(self, form):
        """Logged in user will be automatically considered the author"""
        form.instance.author = self.request.user
        return super().form_valid(form)


def add_comment_to_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = CommentForm()
    return render(request, 'add_comment_to_article.html', {'form': form})


class CommentUpdateView(LoginRequiredMixin, UpdateView):
    model = Comment
    fields = ('comment', )
    template_name = 'comment_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentDeleteView(LoginRequiredMixin, DeleteView):
    model = Comment
    template_name = 'comment_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)