import os
import requests
os.environ["TMDB_API_KEY"] = "8a925434a1b5ae1cb23a5c78daeabb4c"
TMDB_API_KEY = os.environ.get('TMDB_API_KEY', None)

class APIKeyMissingError(Exception):
    pass

if TMDB_API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://developers.themoviedb.org/3/getting-started/introduction "
        "for how to retrieve an authentication token from "
        "The Movie Database"
    )
session = requests.Session()
session.params = {}
session.params['api_key'] = TMDB_API_KEY

from .tv import TV