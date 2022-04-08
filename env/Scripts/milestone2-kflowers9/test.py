import os
import requests
import base64
import random
import json

from decouple import config

# load_dotenv(find_dotenv())

movie_id = 157336
response = requests.get(
    f"https://api.themoviedb.org/3/movie/{movie_id}",
    params={
        "api_key": config("TMDB_API_KEY"),
    },
)
retval = response.json()
first = json.dumps(retval, indent=4, sort_keys=True)
print(retval)

some = {
    "user": 28,
    "person": "Kwaku Flowers",
    "lazy": "power",
}
