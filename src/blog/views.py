from django.views.generic import (
    ListView,
    DetailView
)
from django.http import (
    HttpResponseForbidden,
    HttpResponseNotAllowed,
    HttpResponseRedirect,
)
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.views.generic.edit import FormMixin

from .models import Post, PostIsRead
from .forms import PostForm


User = get_user_model()


class IsOwnerMixin:
    def is_owner(self):
        return self.request.user.is_authenticated \
               and self.request.user.username == self.kwargs.get(self.slug_url_kwarg)


class FeedListView(LoginRequiredMixin, ListView):
    template_name = 'blog/feed.html'

    def get_queryset(self):
        return Post.objects.filter(author__in=self.request.user.authors.all()).all()


class UserDetailView(IsOwnerMixin, FormMixin, DetailView):
    model = User
    post_model = Post
    template_name = 'blog/user_detail.html'
    slug_field = 'username'
    form_class = PostForm

    def get_success_url(self):
        return self.object.get_url()

    def post(self, request, *args, **kwargs):
        if not self.is_owner():
            return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.post_model.objects.create(
            title=form.cleaned_data['title'],
            text=form.cleaned_data['text'],
            author=self.object
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Посты данного пользователя
        context['posts'] = Post.objects.filter(author_id=self.object.id)
        # Если это страница авторизированного пользователя, то даём ему право добавлять посты
        context['is_owner'] = self.is_owner()
        if not context['is_owner']:
            context['is_followed'] = self.request.user in self.object.followers.all()
        return context


class FollowActionsAbstractView(IsOwnerMixin, LoginRequiredMixin, DetailView):
    model = User
    queryset = model.objects.filter(is_active=True)
    slug_field = 'username'
    allowed_methods = ['POST', 'OPTIONS']

    def get_success_url(self):
        print(self.object.get_url())
        return self.object.get_url()

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(self.allowed_methods)


class FollowView(FollowActionsAbstractView):
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.is_owner():
            return HttpResponseForbidden()
        request.user.follow(self.get_object())
        return HttpResponseRedirect(self.get_success_url())


class UnfollowView(FollowActionsAbstractView):
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.is_owner():
            return HttpResponseForbidden()
        request.user.unfollow(self.get_object())
        return HttpResponseRedirect(self.get_success_url())
