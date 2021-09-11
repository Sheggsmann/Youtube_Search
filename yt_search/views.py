from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Contact
from .youtube import Youtube
import json

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
    
    max_results = 5
    if not request.user.is_authenticated:
        max_results = 3
    
    results = youtube.search(video_name, location_tuple, min_subsCount, max_subsCount, max_results)

    if request.user.is_authenticated:
        channel_ids = [channel.channel_id for channel in request.user.contact_set.all()]
        for result in results:
            if result['channel_id'] in channel_ids:
                result['contacted'] = True
            else:
                result['contacted'] = False

    context = {
        'results': results,
        'search': video_name,
        'min_subs': min_subsCount,
        'max_subs': max_subsCount,
        'location': location
    }

    return render(request, 'yt_search/results.html', context)


def about(request):
    context = {}
    return render(request, 'yt_search/about.html', context)


def contact(request, channel_id):
    data = json.loads(request.body)
    contact = Contact.objects.filter(channel_id__exact=channel_id)
    if contact:
        contact.user.add(request.user)
        contact.save()
    else:
        data = json.loads(request.body)
        contact = Contact(channel_id=channel_id, video_id=data['video_id'],
        channel_name=data['channel_name'])
        contact.save()
        contact.user.add(request.user)
    return JsonResponse({'message': 'success'})


def contacts(request):
    user_contacts = request.user.contact_set.all()
    context = {'contacts': user_contacts}
    return render(request, 'yt_search/contacts.html', context)