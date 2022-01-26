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

# detail view for specific meetup
def details(request, meet_slug):
    # mock data
    specific_meet = {
            'title': 'PyATL',
            'location': 'Atlanta',
            'description': "PyAtl meets every month in Atlanta for presentations and discussion about Python, the powerful and easy-to-use programming language. Every meeting tries to include something for beginners, and also to tackle advanced topics for seasoned developers. We are all learning, so don't be shy about attending, no matter your experience level!",
            'slug': 'atlanta-pyatl'
        }

    return render(request, 'meets/detail.html', {
        'title': specific_meet['title'],
        'description': specific_meet['description'],
        'location': specific_meet['location']
    })