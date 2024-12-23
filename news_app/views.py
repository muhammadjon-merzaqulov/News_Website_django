from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from .models import News, Category
from .forms import ContactForm


def news_list(request):
    news_list = News.published.all()
    context = {
        'news_list': news_list
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    contex = {
        'news': news,
    }
    return render(request, 'news/single.html', contex)


def homePageView(request):
    categories = Category.objects.all()
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
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['uzb_news'] = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[:5]
        context['jahon_news'] = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name='Sport').order_by('-publish_time')[:5]
        context['tech_news'] = News.published.all().filter(category__name='Fan-texnika').order_by('-publish_time')[:5]
        return context


class CategoryPageView(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-publish_time')[:4]
        context['uzb_news'] = News.published.all().filter(category__name="O'zbekiston").order_by('-publish_time')[:5]
        context['jahon_news'] = News.published.all().filter(category__name='Jahon').order_by('-publish_time')[:5]
        context['sport_news'] = News.published.all().filter(category__name='Sport').order_by('-publish_time')[:5]
        context['tech_news'] = News.published.all().filter(category__name='Fan-texnika').order_by('-publish_time')[:5]
        return context


def noPageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)


# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if form.is_valid() and request.method == 'POST':
#         form.save()
#         return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat! </h2>")
#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

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





