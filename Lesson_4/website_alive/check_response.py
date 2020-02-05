'''Check response'''

from website_alive.make_request import make_request_


def check_response_(url):
    '''Return True if response is 200 else False'''

    request = make_request_(url)

    return request.status_code == 200
