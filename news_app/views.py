from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone

from .models import News, Category
from .forms import ContactForm

####################################################
def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return News.published.all().order_by('-publish_time')
####################################################


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug, status=News.Status.Published)
    context = {
        'news': news,
    }
    return render(request, 'news/news_detail.html', context)

class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.published.all()


####################################################
def homePageView(request):
    categories = Category.objects.all().order_by('-publish_time')
    news_list = News.published.all().order_by('-publish_time')[:5]
    politics_news_one = News.published.all().filter(category__name='POLITICS').order_by('-publish_time')[:1]
    politics_news = News.published.all().filter(category__name='POLITICS').order_by('-publish_time')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'politics_news_one': politics_news_one,
        'politics_news': politics_news,
    }
    return render(request, 'news/index.html', context)


class HomePageView(ListView):
    model = News
    template_name = 'news/index.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:5]
        context['politics_news'] = News.published.all().filter(category__name='POLITICS').order_by('-publish_time')[:5]
        context['tourism_news'] = News.published.all().filter(category__name='TOURISM').order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name='SPORT').order_by('-publish_time')[:5]
        context['tech_news'] = News.published.all().filter(category__name='TECH').order_by('-publish_time')[:5]
        context['today'] = timezone.now().strftime("%A, %B %d, %Y")
        return context
####################################################


def noPageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)

####################################################
def contactPageView(request):
    print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat! </h2>")
    context = {
        'form': form
    }
    return render(request, 'news/contact.html', context)

class ContactView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid() and request.POST:
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat! </h2>")
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)
####################################################

class PoliticsNewsView(ListView):
    model = News
    template_name = 'news/politics_news.html'
    context_object_name = 'politics_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='POLITICS').order_by('-publish_time')
        return news


class TourismNewsView(ListView):
    model = News
    template_name = 'news/tourism_news.html'
    context_object_name = 'tourism_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='TOURISM').order_by('-publish_time')
        return news


class SportNewsView(ListView):
    model = News
    template_name = 'news/sport_news.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='SPORT').order_by('-publish_time')
        return news


class TechNewsView(ListView):
    model = News
    template_name = 'news/tech_news.html'
    context_object_name = 'tech_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name='TECH').order_by('-publish_time')
        return news





