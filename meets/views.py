from django.shortcuts import render

# import models
from .models import Meet

# Create your views here.

def index(request):
    # pull data from model
    # <model>.objects.all() call will get all objects
    meets = Meet.objects.all()

    # render accepts dictionary (key-value pair) as 3rd argument
    # key = name exposed in HTML template
    # value = python data to expose in template
    return render(request, 'meets/index.html', {
        'meet_list': meets, 
    })

# detail view for specific meetup
def details(request, meet_slug):
    # <model>.objects.get() will fetch a single instace from DB
    # in this case, fetch the meet with a slug that matches this page's slug
    # slug is passed to view function from urls.py
    # return error if something goes wrong
    try:
        specific_meet = Meet.objects.get(slug=meet_slug)

        return render(request, 'meets/detail.html', {
            # expose meet's values to template using context
            'title': specific_meet.title,
            'description': specific_meet.description,
            'location': specific_meet.location,
            'meet_found': True
        })
    except Exception as e:
        print(e)
        return render(request, 'meets/detail.html', {
            'error': e,
            'slug': meet_slug,
            'meet_found': False
        })