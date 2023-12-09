from .views import latest_news_links, get_top_news, home, all_news

from django.urls import path, include

urlpatterns = [
    path('', home, name='home'),
    path('link/',latest_news_links,name='latest_link'),
    path('top/', get_top_news, name='get_top_news'),
    path('news/', all_news, name='all_news'),

]
