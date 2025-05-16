# mcdo-api
Just provides a JSON file that contains all the McDonald's locations in Japan for now.

# API list
## Get all locations:
https://k1832.github.io/mcdo-api/api/v1/store-location.json

The id's format in the response JSON is `{latitude}+{longitude}`.  
I decided NOT to use the id from the original McDonald's API because I found that the ID for the same store could change over time. (Example: see [this diff](https://github.com/k1832/mcdo-api/commit/d0e5b1c5969d0c7ab885000485fe6337ddab7d1d))
