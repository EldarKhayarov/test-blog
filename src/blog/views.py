from django.views.generic import (
    ListView,
    DetailView
)
from django.http import (
    HttpResponseForbidden,
    HttpResponseRedirect,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.views.generic.edit import FormMixin
from django.urls import reverse_lazy

from .models import Post, PostIsRead
from .forms import PostForm


User = get_user_model()


class IsOwnerMixin:
    """
    Миксина с методом авторизации.
    """
    def is_owner(self):
        """
        Проверяет, является ли пользователь владельшем страницы.
        """
        return self.request.user.is_authenticated \
               and self.request.user.username == self.kwargs.get(self.slug_url_kwarg)


class FeedListView(LoginRequiredMixin, ListView):
    template_name = 'blog/feed.html'

    def get_queryset(self):
        return Post.objects.filter(author__in=self.request.user.authors.all())

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # Добавим в контекст пометки о прочитанности
        context['marked_post_ids'] = PostIsRead.objects\
            .filter(user=self.request.user)\
            .values_list('post_id', flat=True)\
            .all()
        return context


class UserDetailView(
    LoginRequiredMixin,
    IsOwnerMixin,
    FormMixin,
    DetailView
):
    model = User
    post_model = Post
    template_name = 'blog/user_detail.html'
    slug_field = 'username'
    form_class = PostForm

    def get_success_url(self):
        # Возвращаем адрес пользователя
        return self.object.get_url()

    def post(self, request, *args, **kwargs):
        """
        Метод необходим для публикации постов.
        """
        # Авторизация
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
        """
        Метод для получения списка постов на странице пользователя.
        """
        context = super().get_context_data(**kwargs)
        # Посты данного пользователя
        context['posts'] = Post.objects.filter(author_id=self.object.id)
        # Если это страница авторизированного пользователя, то даём ему право добавлять посты
        context['is_owner'] = self.is_owner()
        if not context['is_owner']:
            context['is_followed'] = self.request.user in self.object.followers.all()
        return context


class FollowActionsAbstractView(IsOwnerMixin, LoginRequiredMixin, DetailView):
    """
    Абстрактный класс для Follow/Unfollow классов.
    """
    model = User
    queryset = model.objects.filter(is_active=True)
    slug_field = 'username'

    def get_success_url(self):
        return self.object.get_url()


class FollowView(FollowActionsAbstractView):
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.is_owner():
            return HttpResponseForbidden()
        request.user.follow(self.get_object())
        return HttpResponseRedirect(self.get_success_url())


class UnfollowView(FollowActionsAbstractView):
    def _remove_read_marks(self):
        """
        Метод для удаления пометок о прочитанности постов автора,
        от которого отписывается пользователь.
        """
        PostIsRead.objects.filter(
            post__author_id=self.object.id,
            user_id=self.request.user.id
        ).delete()

    def get(self, request, *args, **kwargs):
        """
        Метод отписки от пользователя.

        Происходит авторизация пользователя, затем вызываются методы
        отписки класса модели и удаления пометок прочитанности.
        """
        self.object = self.get_object()
        if self.is_owner():
            return HttpResponseForbidden()

        request.user.unfollow(self.get_object())
        self._remove_read_marks()
        return HttpResponseRedirect(self.get_success_url())


class MarkUnmarkAbstractView(LoginRequiredMixin, DetailView):
    model = Post
    success_url = reverse_lazy('feed-list')


class MarkReadView(MarkUnmarkAbstractView):
    def get(self, request, *args, **kwargs):
        """
        Метод создания записи с пометкой о прочитанности.

        После выполнения происходит перенаправление на главнную.
        """
        self.object = self.get_object()
        if not PostIsRead.objects.filter(
                user=request.user.id,
                post_id=self.object.id
        ).exists():
            PostIsRead.objects.create(
                user=request.user,
                post=self.object
            )

        return HttpResponseRedirect(self.success_url)


class UnmarkReadView(MarkUnmarkAbstractView):
    def get(self, request, *args, **kwargs):
        """
        Метод для удаления записи с пометкой о прочитанности конкретного поста.

        После выполнения удаления происходит перенаправление на
        главную страницу.
        """
        self.object = self.get_object()
        PostIsRead.delete(
            PostIsRead.objects.get(user=request.user, post=self.object)
        )

        return HttpResponseRedirect(self.success_url)
