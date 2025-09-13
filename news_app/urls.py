from django.urls import path
from .views import (news_list, news_detail, homePageView, noPageView,
                    ContactView, HomePageView, NewsListView, NewsDetailView,
                    PoliticsNewsView, TourismNewsView, SportNewsView, TechNewsView )


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('category/', noPageView, name='category'),
    path('news/all/', NewsListView.as_view(), name='all_news_list'),
    path('news/<slug:slug>/', NewsDetailView.as_view(), name='news_detail'),
    path('politics/', PoliticsNewsView.as_view(), name='politics_news'),
    path('tourism/', TourismNewsView.as_view(), name='tourism_news'),
    path('sport/', SportNewsView.as_view(), name='sport_news'),
    path('tech/', TechNewsView.as_view(), name='tech_news')
]