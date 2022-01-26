from django.shortcuts import render

# Create your views here.

def index(request):
    meets = [
        {'title': 'First Meetup'},
        {'title': 'Second Meetup'}
    ]

    # render accepts dictionary (key-value pair) as 3rd argument
    # key = name exposed in HTML template
    # value = python data to expose in template
    return render(request, 'meets/index.html', {
        'meet_list': meets,
        'show_meetups': True
    })