import requests

URL = "http://tour-pedia.org/api/"

def places_statistics() -> dict:
    """
    Get the statistics of the places.

    :return: JSON object with the statistics of the places
    """
    response = requests.get(URL + "getPlacesStatistics")
    return response.json()

def places(location: str = None, category: str = None, name: str = None, source: str = None) -> dict:
    """
    Queries among the places.

    :param location: The location of the places. Currently, we have 8 possible locations: Amsterdam, Barcelona, Berlin, Dubai, London, Paris, Rome, Tuscany.
    :param category: Defines the type of the places such as accommodation, attraction, restaurant, poi (point of interest)
    :param name: The text string on which to search among the names of all the places, for example: "Hotel Bologna"
    :param source: Search the places recovered by only a source. A source can be: Booking, Facebook, Foursquare, GooglePlaces
    :return: JSON object with the places that match the query
    """
    valid_locations = ["Amsterdam", "Barcelona", "Berlin", "Dubai", "London", "Paris", "Rome", "Tuscany"]
    valid_categories = ["accommodation", "attraction", "restaurant", "poi"]
    valid_sources = ["Booking", "Facebook", "Foursquare", "GooglePlaces"]

    if not (location or category or name):
        raise ValueError("At least one of 'location', 'category', or 'name' must be defined")

    if location and location not in valid_locations:
        raise ValueError("Invalid location")
    if category and category not in valid_categories:
        raise ValueError("Invalid category")
    if source and source not in valid_sources:
        raise ValueError("Invalid source")

    query_params = {
        "location": location,
        "category": category,
        "name": name,
        "source": source
    }
    response = requests.get(URL + "getPlaces", params={k: v for k, v in query_params.items() if v})
    return response.json()

def place_details(place_id: str) -> dict:
    """
    Get the details of a place.

    :param place_id: The ID of the place
    :return: JSON object with the details of the place
    """
    response = requests.get(URL + "getPlaceDetails", params={"id": place_id})
    return response.json()

def places_by_area(s: str, n: str, w: str, e: str, category: str) -> dict:
    """
    Get the places in a given area.

    :param s:
    :param n:
    :param w:
    :param e:
    :param category: Defines the type of the places such as accommodation, attraction, restaurant, poi (point of interest)
    :return: JSON object with the places that match the query
    """
    valid_categories = ["accommodation", "attraction", "restaurant", "poi"]
    if category not in valid_categories:
        raise ValueError("Invalid category")

    query_params = {
        "S": s,
        "N": n,
        "W": w,
        "E": e,
        "category": category
    }
    response = requests.get(URL + "getPlacesByArea", params=query_params)
    return response.json()

def reviews_statistics() -> dict:
    """
    Get the statistics of the reviews.

    :return: JSON object with the statistics of the reviews
    """
    response = requests.get(URL + "getReviewsStatistics")
    return response.json()

def reviews(location: str, category: str, language: str, source: str, keyword: str, min_words: str, max_words: str, start_date: str, end_date: str) -> dict:
    """
    Queries among the reviews of the places.

    :param location: The location of the places reviewed. Currently, we have 8 possible locations: Amsterdam, Barcelona, Berlin, Dubai, London, Paris, Rome, Tuscany.
    :param category: Defines the type of the places reviewed such as accommodation, attraction, restaurant, poi (point of interest)
    :param language: The language of the review, for example: "en"
    :param source: Search the places reviews recovered by only a source. A source can be: Booking, Facebook, Foursquare, GooglePlaces
    :param keyword: The text string to search inside the reviews text, for example: "Camino de Santiago"
    :param min_words: Defines the minimum number of words of the reviews
    :param max_words: Defines the maximum number of words of the reviews
    :param start_date: Establish that the date of the review must be greater than the value of startDate
    :param end_date: Establish that the date of the review must be lower than the value of startDate
    :return: JSON object with the reviews that match the query
    """
    valid_locations = ["Amsterdam", "Barcelona", "Berlin", "Dubai", "London", "Paris", "Rome", "Tuscany"]
    valid_categories = ["accommodation", "attraction", "restaurant", "poi"]
    valid_sources = ["Booking", "Facebook", "Foursquare", "GooglePlaces"]

    if location not in valid_locations:
        raise ValueError("Invalid location")
    if category not in valid_categories:
        raise ValueError("Invalid category")
    if source not in valid_sources:
        raise ValueError("Invalid source")

    query_params = {
        "location": location,
        "category": category,
        "language": language,
        "source": source,
        "keyword": keyword,
        "minWords": min_words,
        "maxWords": max_words,
        "startDate": start_date,
        "endDate": end_date
    }
    response = requests.get(URL + "getReviews", params={k: v for k, v in query_params.items() if v})
    return response.json()
