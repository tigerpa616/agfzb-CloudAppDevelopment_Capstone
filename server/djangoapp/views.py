from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def index(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create an `about` view to render a static about page
def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)



# Create a `contact` view to return a static contact page
def contact(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact.html', context)


# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to login page again
            return render(request, 'djangoapp/login.html', context)
    else:
        return render(request, 'djangoapp/login.html', context)
  
   
# ...

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return render(request, 'djangoapp/index.html')
# ...

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            # Login the user and redirect to course list page
            login(request, user)
            return redirect("djangoapp/index")
        else:
            return render(request, 'djangoapp/registration.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    if request.method == "GET":
        dealerships = get_dealerships_from_cf()
        context = {"dealerships": dealerships}
        get_dealerships_view = render(request, 'djangoapp/index.html', context)
    return get_dealerships_view


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...
def get_dealer_reviews(request, dealer_id, dealer_name):
    """ Dealerships Details """
    if request.method == "GET":
        dealer_reviews = get_dealer_reviews_from_cf(dealer_id)
        context = {
            "dealer_id": dealer_id,
            "dealer_name": dealer_name,
            "reviews": dealer_reviews
        }
        dealer_details_view = render(
            request, 'djangoapp/reviews.html', context)
    return dealer_details_view
# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
def add_dealer_review(request, dealer_id, dealer_name):
    """ Add Review View """
    if request.method == "GET":
        cars = CarModel.objects.filter(dealer_id=dealer_id)
        context = {"cars": cars, "dealer_id": dealer_id,
                   "dealer_name": dealer_name}
        add_review_view = render(request, 'djangoapp/add_review.html', context)
    if request.method == "POST" and request.user.is_authenticated:
        form = request.POST
        review = {
            "review_id": random.randint(0, 100),
            "reviewer_name": form["fullname"],
            "dealership": dealer_id,
            "review": form["review"]
        }
        if form.get("purchase"):
            review["purchase"] = True
            review["purchase_date"] = form["purchasedate"]
            car = get_object_or_404(CarModel, pk=form["car"])
            review["car_make"] = car.carmake.name
            review["car_model"] = car.name
            review["car_year"] = car.year
        json_result = add_dealer_review_to_db(review)
        add_review_view = redirect(
            'djangoapp:dealer_reviews', dealer_id=dealer_id, dealer_name=dealer_name)
    return add_review_view

