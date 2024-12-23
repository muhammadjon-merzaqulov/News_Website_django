from .models import News, Category


def latest_news(request):
    latest_news1 = News.published.all().order_by('-publish_time')[:10]
    categories = Category.objects.all()
    news_list = News.published.all().order_by('-publish_time')[:4]
    context = {
        'latest_news1': latest_news1,
        'categories': categories,
        'news_list': news_list
    }
    return context