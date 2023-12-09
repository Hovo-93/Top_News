from multiprocessing import Pool

from django.shortcuts import render, redirect
from .models import *
from .services import NewsLinkScraper, TopNewsScraper
from django.http import JsonResponse, HttpResponse
from django.contrib import messages

URL = 'https://news.am/eng/'


# Create your views here.


def latest_news_links(request):
    links_scrapper = NewsLinkScraper(URL)
    top_news_links = links_scrapper.scrapy_top_news_links()

    existing_urls = set(TopNewsLink.objects.values_list('url', flat=True))
    print(existing_urls, '-----------')
    if existing_urls:
        return HttpResponse('Existing URLs')
    new_urls = [url for url in top_news_links if url not in existing_urls]
    if not new_urls:
        return HttpResponse('DB is already updated', status=200)
    instances = [TopNewsLink(url=url) for url in new_urls]
    created = TopNewsLink.objects.bulk_create([url for url in instances])
    if created:
        return HttpResponse('Objects are created successfully', status=201)
    return HttpResponse('Creation was failed', status=400)


def get_top_news(request):
    """
        Get top news using multiprocessing
    :param request:
    :return:
    """
    links = TopNewsLink.objects.values_list('url', flat=True)

    top_news_scraper = TopNewsScraper()
    num_processes = 5

    with Pool(processes=num_processes) as pool:
        results = pool.map(top_news_scraper.get_all_info, links)
        instances = []
        for result in results:
            existing_news = News.objects.filter(
                title=result['article_title'],
                image=result['image_url'],
                text=result['article_texts']
            ).first()
            if not existing_news:
                instance = News(
                    title=result['article_title'],
                    image=result['image_url'],
                    text=result['article_texts']
                )
                instances.append(instance)

        # if instances:
        #     News.objects.bulk_create(instances)
        #     return HttpResponse('Objects are created successfully', status=201)
        #
        # return HttpResponse('No new objects were created', status=400)
        if instances:
            News.objects.bulk_create(instances)
            # If objects are created successfully, set a success message
            messages.success(request, 'Objects are created successfully')
            return redirect('home')  # Replace 'home' with the name of your home view

        # If no new objects were created, set an error message
        messages.error(request, 'No new objects were created')
        return redirect('home')  # Replace 'home' with the name of your home view


def all_news(request):
    # Retrieve all news objects
    all_news_items = News.objects.all()
    context = {
        'all_news_items': all_news_items
    }
    return render(request, 'all_news.html', context)


def home(request):
    return render(request, 'home.html')
