import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger(__name__)

# Create a `get_request` to make HTTP GET requests
# e.g., response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
#                                     auth=HTTPBasicAuth('apikey', api_key))
def get_request(url, api_key, **kwargs):
    print("GET from {}".format(url))
    print(kwargs)
    try:
        if api_key is not None:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs, auth=HTTPBasicAuth('apikey', api_key))
        else:
            response = requests.get(url, headers={'Content-Type': 'application/json'}, params=kwargs)
    except:
        print("Network Error")
    status_code = response.status_code
    print("With status code {}".format(status_code))
    json_data = json.loads(response.text)
    return json_data, status_code

# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
# def get_dealers_from_cf(url, **kwargs):
# - Call get_request() with specified arguments
# - Parse JSON results into a CarDealer object list
def get_dealers_from_cf(url, **kwargs):
    info = []
    result = "ok"
    # - Call get_request() with specified arguments
    logger.info("Get Dealers from CF")
    json_result, status_code = get_request(url, None)
    if status_code == 200 and json_result:
        dealers = json_result['body']
        logger.info(len(dealers))
        for dealer in dealers:
            dlr_data = dealer['doc']
            #print('ADDRESS', dlr_data["address"])
            if dlr_data.get('address'):
            # Create a CarDealer object with values in `doc` object
                dealer_obj = CarDealer(address=dlr_data.get("address"), city=dlr_data.get("city"), full_name=dlr_data.get("full_name"),
                            id=dlr_data.get("id"), lat=dlr_data.get("lat"), long=dlr_data.get("long"),
                            short_name=dlr_data.get("short_name"), state=dlr_data.get("state"),
                            st=dlr_data.get("st"), zip=dlr_data.get("zip"))
            
            # dealer_obj = CarDealer(address=dealer["doc"]["address"], city=dealer["doc"]["city"], full_name=dealer["doc"]["full_name"],
            #                     id=dealer["doc"]["id"], lat=dealer["doc"]["lat"], long=dealer["doc"]["long"],
            #                     short_name=dealer["doc"]["short_name"], 
            #                     st=dealer["doc"]["st"], state=dealer["doc"]["state"], zip=dealer["doc"]["zip"])
                info.append(dealer_obj)
    elif json_result:
        result = json_result["message"]
    else:
        result = "Unknown error"
    return info, result

# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
# def get_dealer_by_id_from_cf(url, dealerId):
# - Call get_request() with specified arguments
# - Parse JSON results into a DealerView object list


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
# def analyze_review_sentiments(text):
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



