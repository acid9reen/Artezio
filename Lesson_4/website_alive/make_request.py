'''Make request'''

import requests


def make_request_(url):
    '''Return request object'''

    return requests.get(url)
