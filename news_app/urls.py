from django.urls import path
from .views import news_list, news_detail, homePageView, noPageView, ContactView, HomePageView, CategoryPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('category/', CategoryPageView.as_view(), name='category'),
    path('news/all/', news_list, name='all_news_list'),
    path('news/<int:id>/', news_detail, name='news_detail'),

]