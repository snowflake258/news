from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from management.models import Article


class StartPage(ListView):
    model: Article = Article
    paginate_by = 5
    template_name = 'news_site/start_page.html'

    def get_queryset(self):
        category_id = self.kwargs.get('category', None)

        if category_id is None:
            return self.model.objects.all()
        return self.model.objects.filter(category_id=category_id)


class ArticleDetail(DetailView):
    model: Article = Article
    template_name = 'news_site/article_detail.html'
