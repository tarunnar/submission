import requests
from pprint import pprint

endpoint="https://developers.zomato.com/api/v2.1/"
headers = {
    'Accept': 'application/json',
    'user-key': '2ddaa2d4d751aa03dd3493372fbac29e'

}
resp = requests.get(endpoint+"categories", headers=headers)
pprint(resp.json())

categories={'categories': [{'categories': {'id': 1, 'name': 'Delivery'}},
                {'categories': {'id': 2, 'name': 'Dine-out'}},
                {'categories': {'id': 3, 'name': 'Nightlife'}},
                {'categories': {'id': 4, 'name': 'Catching-up'}},
                {'categories': {'id': 5, 'name': 'Takeaway'}},
                {'categories': {'id': 6, 'name': 'Cafes'}},
                {'categories': {'id': 7, 'name': 'Daily Menus'}},
                {'categories': {'id': 8, 'name': 'Breakfast'}},
                {'categories': {'id': 9, 'name': 'Lunch'}},
                {'categories': {'id': 10, 'name': 'Dinner'}},
                {'categories': {'id': 11, 'name': 'Pubs & Bars'}},
                {'categories': {'id': 13, 'name': 'Pocket Friendly Delivery'}},
                {'categories': {'id': 14, 'name': 'Clubs & Lounges'}}]}
banglore = {
  "location_suggestions": [
    {
      "id": 4,
      "name": "Bengaluru",
      "country_id": 1,
      "country_name": "India",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_1.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 1,
      "is_state": 0,
      "state_id": 0,
      "state_name": "",
      "state_code": ""
    }
  ],
  "status": "success",
  "has_more": 0,
  "has_total": 0
}

hyderabad = {
  "location_suggestions": [
    {
      "id": 6,
      "name": "Hyderabad",
      "country_id": 1,
      "country_name": "India",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_1.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 1,
      "is_state": 0,
      "state_id": 0,
      "state_name": "",
      "state_code": ""
    }
  ],
  "status": "success",
  "has_more": 0,
  "has_total": 0
}

delhi = {
  "location_suggestions": [
    {
      "id": 1,
      "name": "Delhi NCR",
      "country_id": 1,
      "country_name": "India",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_1.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 1,
      "is_state": 0,
      "state_id": 0,
      "state_name": "",
      "state_code": ""
    },
    {
      "id": 3515,
      "name": "Delhi, ON",
      "country_id": 37,
      "country_name": "Canada",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_37.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 0,
      "is_state": 0,
      "state_id": 124,
      "state_name": "Ontario",
      "state_code": "ON"
    },
    {
      "id": 7987,
      "name": "Delhi, CA",
      "country_id": 216,
      "country_name": "United States",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_216.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 0,
      "is_state": 0,
      "state_id": 73,
      "state_name": "California",
      "state_code": "CA"
    },
    {
      "id": 4968,
      "name": "Delhi, IA",
      "country_id": 216,
      "country_name": "United States",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_216.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 0,
      "is_state": 0,
      "state_id": 80,
      "state_name": "Iowa",
      "state_code": "IA"
    },
    {
      "id": 5888,
      "name": "Delhi, LA",
      "country_id": 216,
      "country_name": "United States",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_216.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 0,
      "is_state": 0,
      "state_id": 86,
      "state_name": "Louisiana",
      "state_code": "LA"
    },
    {
      "id": 7791,
      "name": "Delhi, NY",
      "country_id": 216,
      "country_name": "United States",
      "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_216.png",
      "should_experiment_with": 0,
      "discovery_enabled": 0,
      "has_new_ad_format": 0,
      "is_state": 0,
      "state_id": 103,
      "state_name": "New York State",
      "state_code": "NY"
    }
  ],
  "status": "success",
  "has_more": 0,
  "has_total": 0
}
establishment_type = {
  "establishments": [
    {
      "establishment": {
        "id": 21,
        "name": "Quick Bites"
      }
    },
    {
      "establishment": {
        "id": 23,
        "name": "Dessert Parlour"
      }
    },
    {
      "establishment": {
        "id": 20,
        "name": "Food Court"
      }
    },
    {
      "establishment": {
        "id": 16,
        "name": "Casual Dining"
      }
    },
    {
      "establishment": {
        "id": 31,
        "name": "Bakery"
      }
    },
    {
      "establishment": {
        "id": 291,
        "name": "Sweet Shop"
      }
    },
    {
      "establishment": {
        "id": 1,
        "name": "Café"
      }
    },
    {
      "establishment": {
        "id": 7,
        "name": "Bar"
      }
    },
    {
      "establishment": {
        "id": 6,
        "name": "Pub"
      }
    },
    {
      "establishment": {
        "id": 18,
        "name": "Fine Dining"
      }
    },
    {
      "establishment": {
        "id": 61,
        "name": "Dhaba"
      }
    },
    {
      "establishment": {
        "id": 304,
        "name": "Mess"
      }
    },
    {
      "establishment": {
        "id": 41,
        "name": "Beverage Shop"
      }
    },
    {
      "establishment": {
        "id": 5,
        "name": "Lounge"
      }
    },
    {
      "establishment": {
        "id": 8,
        "name": "Club"
      }
    },
    {
      "establishment": {
        "id": 161,
        "name": "Microbrewery"
      }
    },
    {
      "establishment": {
        "id": 4,
        "name": "Kiosk"
      }
    },
    {
      "establishment": {
        "id": 307,
        "name": "Bhojanalya"
      }
    },
    {
      "establishment": {
        "id": 191,
        "name": "Confectionery"
      }
    },
    {
      "establishment": {
        "id": 81,
        "name": "Food Truck"
      }
    },
    {
      "establishment": {
        "id": 308,
        "name": "Paan Shop"
      }
    },
    {
      "establishment": {
        "id": 51,
        "name": "Butcher Shop"
      }
    },
    {
      "establishment": {
        "id": 303,
        "name": "Irani Cafe"
      }
    },
    {
      "establishment": {
        "id": 278,
        "name": "Wine Bar"
      }
    }
  ]
}

