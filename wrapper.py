import requests

URL = "http://tour-pedia.org/api/"

def places_statistics() -> dict:
    response = requests.get(URL + "getPlacesStatistics")
    return response.json()

def places(location: str, category: str, name: str) -> dict:
    response = requests.get(URL + "getPlaces" + "?location=" + location + "&category=" + category + "&name=" + name)
    return response.json()

def place_details(id: str) -> dict:
    response = requests.get(URL + "getPlaceDetails" + "?id=" + id)
    return response.json()

def places_by_area(S: str, N: str, W: str, E: str, category: str) -> dict:
    response = requests.get(URL + "getPlacesByArea" + "?S=" + S + "&N=" + N + "&W=" + W + "&E=" + E + "&category=" + category)
    return response.json()

def reviews(location: str, category: str, language: str, source: str, keyword: str, minWords: str, maxWords: str, startDate: str, endDate: str) -> dict:
    """
    Queries among the reviews of the places.

    :param location: The location of the places reviewed . Currently we have 8 possible locations: Amsterdam, Barcelona, Berlin, Dubay, London, Paris, Rome, Tuscany.
    :param category: Defines the type of the places reviewed such as accomodation, attraction, restaurant, poi (point of interest)
    :param language: The language of the review, for example: "en"
    :param source: Search the places reviews recovered by only a source. A source can be: Booking, Facebook, Foursquare, GooglePlaces
    :param keyword: The text string to search inside the reviews text, for example: "Camino de Santiago"
    :param minWords: Defines the minimum number of words of the reviews
    :param maxWords: Defines the maximum number of words of the reviews
    :param startDate: Establish that the date of the review must to be greater than the value of startDate
    :param endDate: Establish that the date of the review must to be lower than the value of startDate
    """
    response = requests.get(URL + "getReviews" + "?location=" + location + "&category=" + category + "&language=" + language + "&source=" + source + "&keyword=" + keyword + "&minWords=" + minWords + "&maxWords=" + maxWords + "&startDate=" + startDate + "&endDate=" + endDate)
    return response.json()