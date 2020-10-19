from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.edit import DeletionMixin
from django.views.generic.base import View
from django.contrib.messages.views import SuccessMessageMixin
from management.models import Category, Article, ArticleImage


category_success_redirect = reverse_lazy('management:category_list')
article_success_redirect = reverse_lazy('management:article_list')


class CategoryListView(ListView):
    model = Category
    paginate_by = 10


class CategoryCreateView(SuccessMessageMixin, CreateView):
    model = Category
    fields = ('name',)
    extra_context = {'page_name': 'Создание категории', 'object_name': 'Новая категория'}
    success_message = 'Новая категория создана.'
    success_url = category_success_redirect


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    model = Category
    fields = ('name',)
    success_message = 'Категория изменена.'
    success_url = category_success_redirect

    def get_context_data(self, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['page_name'] = 'Редактирование категории'
        context['object_name'] = self.get_object().name
        return context


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category
    success_message = 'Категория удалена.'
    success_url = category_success_redirect

    def get_context_data(self, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['page_name'] = 'Удаление категории'
        context['object_name'] = self.get_object().name
        return context


class ArticleListView(ListView):
    model = Article
    paginate_by = 10


class ArticleCreateView(SuccessMessageMixin, CreateView):
    model = Article
    fields = ('name', 'content', 'category')
    extra_context = {'page_name': 'Создание статьи', 'object_name': 'Новая статья'}
    success_message = 'Новая статья создана.'
    success_url = article_success_redirect


class ArticleUpdateView(SuccessMessageMixin, UpdateView):
    model = Article
    fields = ('name', 'content', 'category')
    success_message = 'Статья изменена.'
    success_url = article_success_redirect

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Редактирование статьи'
        context['object_name'] = self.get_object().name
        return context


class ArticleDeleteView(SuccessMessageMixin, DeleteView):
    model = Article
    success_message = 'Статья удалена.'
    success_url = article_success_redirect

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = 'Удаление статьи'
        context['object_name'] = self.get_object().name
        return context


class ArticleImageListView(ListView):
    model: ArticleImage = ArticleImage
    template_name = 'management/article_image_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article'] = Article.objects.get(pk=self.kwargs['article_pk'])
        return context

    def get_queryset(self):
        return self.model.objects.filter(article__pk=self.kwargs['article_pk'])


class ArticleImageCreateView(SuccessMessageMixin, CreateView):
    model = ArticleImage
    fields = ('image', 'article')
    success_message = 'Изображение добавлено.'

    def get_success_url(self):
        return self.request.headers['referer']

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, 'Изображение не выбрано.')
        return redirect(self.request.headers['referer'])


class ArticleImageDeleteView(SuccessMessageMixin, DeletionMixin, View):
    model: ArticleImage = ArticleImage
    success_message = 'Изображение удалено.'

    def get_object(self):
        return self.model.objects.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        return self.request.headers['referer']
