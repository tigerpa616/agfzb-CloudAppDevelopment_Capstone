from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import index

app_name = 'djangoapp'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL

    # path for about view
    
    # Create a path object defining the URL pattern to the index view
    path('', views.index, name='index'),
    path('djangoapp/about', views.about, name='about'),
    path('djangoapp/index', views.get_dealerships, name='about'),

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)