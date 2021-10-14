import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))

def get_request(url, **kwargs):
    """ Get """
    try:
        response = requests.get(
            url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        print("Network exception occurred")
    json_data = json.loads(response.text)
    return json_data
# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)

def get_dealerships_from_cf():
    """ Get Dealerships"""
    results = []
    json_result = get_request(API_URL_DEALERSHIP)
    if json_result:
        dealerships = json_result["entries"]
        for dealer in dealerships:
            car_dealer = CarDealer(id=dealer["id"],
                                   city=dealer["city"],
                                   state=dealer["state"],
                                   st=dealer["st"],
                                   address=dealer["address"],
                                   zip=dealer["zip"],
                                   lat=dealer["lat"],
                                   long=dealer["long"],
                                   short_name=dealer["short_name"],
                                   full_name=dealer["full_name"])
            results.append(car_dealer)
    return results

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function


def get_dealer_reviews_from_cf(dealerId):
    """ Get Reviews"""
    results = []
    json_result = get_request(API_URL_REVIEW, dealerId=dealerId)
    if json_result:
        reviews = json_result["entries"]
        for review in reviews:
            sentiment = analyze_review_sentiments(review["review"])
            dealer_review = DealerReview(id=review["id"],
                                         name=review["name"],
                                         dealership=review["dealership"],
                                         review=review["review"],
                                         purchase=review["purchase"],
                                         purchase_date=review["purchase_date"],
                                         car_make=review["car_make"],
                                         car_model=review["car_model"],
                                         car_year=review["car_year"],
                                         sentiment=sentiment)
            results.append(dealer_review)
    return results



# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



