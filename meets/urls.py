# Import dependencies from django
from django.urls import path

# Import dependencies from app
from . import views


urlpatterns = [
    # define urlpatterns to connect paths to views
    # path(<url>, <view to load>, [<name>])

    # path for main page
    path('meets/', views.index, name="meets"), # <domain>/index/

    # dynamic path for meet detail
    # <> means dynamic data passed into url path
    # <slug: [name]> makes it conform to slug pattern
    # make sure to pass slug [name] to view function
    path('meets/<slug:meet_slug>', views.details, name="details"), # <domain>/meets/<dynamic-path>
]
