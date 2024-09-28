import requests

URL = "http://tour-pedia.org/api/"
VALID_LOCATIONS = ["Amsterdam", "Barcelona", "Berlin", "Dubai", "London", "Paris", "Rome", "Tuscany"]
VALID_CATEGORIES = ["accommodation", "attraction", "restaurant", "poi"]
VALID_SOURCES = ["Booking", "Facebook", "Foursquare", "GooglePlaces"]


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
    if not (location or category or name):
        raise ValueError("At least one of 'location', 'category', or 'name' must be defined")

    if location and location not in VALID_LOCATIONS:
        raise ValueError("Invalid location")
    if category and category not in VALID_CATEGORIES:
        raise ValueError("Invalid category")
    if source and source not in VALID_SOURCES:
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

    :param s: The southern latitude of the area
    :param n: The northern latitude of the area
    :param w: The western longitude of the area
    :param e: The eastern longitude of the area
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


def reviews(location: str = None, category: str = None, language: str = None, source: str = None, keyword: str = None, min_words: str = None, max_words: str = None, start_date: str = None, end_date: str = None) -> dict:
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
    if location and location not in VALID_LOCATIONS:
        raise ValueError("Invalid location")
    if category and category not in VALID_CATEGORIES:
        raise ValueError("Invalid category")
    if source and source not in VALID_SOURCES:
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


def review_details(review_id: str) -> dict:
    """
    Get the details of a review.

    :param review_id: The ID of the review
    :return: JSON object with the details of the review
    """
    response = requests.get(URL + "getReviewDetails", params={"id": review_id})
    return response.json()


def review_by_place(place_id: str) -> dict:
    """
    Get the reviews of a place.

    :param place_id: The ID of the place
    :return: JSON object with the reviews of the place
    """
    response = requests.get(URL + "getReviewsByPlaceID", params={"placeId": place_id})
    return response.json()


def opinions(location: str = None, category: str = None, language: str = None, source: str = None, keyword: str = None, min_words: str = None, max_words: str = None, start_date: str = None, end_date: str = None) -> dict:
    """
    Queries among the opinions of the places.

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
    if location and location not in VALID_LOCATIONS:
        raise ValueError("Invalid location")
    if category and category not in VALID_CATEGORIES:
        raise ValueError("Invalid category")
    if source and source not in VALID_SOURCES:
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
    response = requests.get(URL + "getOpinions", params={k: v for k, v in query_params.items() if v})
    return response.json()


def opinions_by_place(place_id: str) -> dict:
    """
    Get the opinions of a place.

    :param place_id: The ID of the place
    :return: JSON object with the opinions of the place
    """
    response = requests.get(URL + "getOpinionsByPlace", params={"id": place_id})
    return response.json()


def entities(location: str = None, category: str = None, language: str = None, source: str = None, keyword: str = None, min_words: str = None, max_words: str = None, start_date: str = None, end_date: str = None) -> dict:
    """
    Queries among the entities of the places.

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
    if location and location not in VALID_LOCATIONS:
        raise ValueError("Invalid location")
    if category and category not in VALID_CATEGORIES:
        raise ValueError("Invalid category")
    if source and source not in VALID_SOURCES:
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
    response = requests.get(URL + "getEntities", params={k: v for k, v in query_params.items() if v})
    return response.json()


def entities_by_place(place_id: str) -> dict:
    """
    Get the entities of a place.

    :param place_id: The ID of the place
    :return: JSON object with the entities of the place
    """
    response = requests.get(URL + "getEntitiesByPlace", params={"id": place_id})
    return response.json()
