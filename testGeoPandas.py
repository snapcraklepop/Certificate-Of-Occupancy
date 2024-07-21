from uszipcode import SearchEnginesearch

SearchEnginesearch.SearchEngine(simple_zipcode = False)
metro_nyc = search.by_coordinates(lat = 40.73, lng = -73.99, radius = 75, returns = 500)