from django.shortcuts import render

# Create your views here.

def index(request):
    # mock data until models up
    meets = [
        {
            'title': 'PyATL',
            'location': 'Atlanta',
            'slug': 'atlanta-pyatl'
        },
        {
            'title': 'BrooklynJS',
            'location': 'New York City',
            'slug': 'newyorkcity-brooklynjs'
        }
    ]

    # render accepts dictionary (key-value pair) as 3rd argument
    # key = name exposed in HTML template
    # value = python data to expose in template
    return render(request, 'meets/index.html', {
        'meet_list': meets,
        'show_meetups': True
    })