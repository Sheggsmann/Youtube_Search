from django.shortcuts import render, redirect
from .youtube import Youtube


youtube = Youtube()


# Create your views here.
def home(request):
    context = {}
    return render(request, 'yt_search/home.html', context)


def search(request):
    data = request.GET
    video_name = data.get('video_name')
    location = data.get('location')
    lat = data.get('lat')
    lng = data.get('lng')
    location_tuple = (lat, lng)
    min_subsCount = int(data.get('min'))
    max_subsCount = int(data.get('max'))
    max_subsCount = 10**10 if max_subsCount > 9999 else max_subsCount 
    
    results = youtube.search(video_name, location_tuple, min_subsCount, max_subsCount)

    if not request.user.is_authenticated:
        if len(results) > 3:
            results = results[:3]

    context = {
        'results': results,
        'search': video_name,
        'min_subs': min_subsCount,
        'max_subs': max_subsCount,
        'location': location
    }

    print('\n\n', results[:3], '\n\n')

    return render(request, 'yt_search/results.html', context)


def about(request):
    context = {}
    return render(request, 'yt_search/about.html', context)