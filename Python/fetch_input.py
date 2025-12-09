import requests
import http.cookiejar as cookiejar
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
def fetchOnline(year, day):
    if year < 2015 or year > 2026 or day < 1 or day > 25:
        print("Invalid year or day")
        return

    # Set the session cookie : get manually from the browser
    session_cookie = open(f'{dir_path}/session_cookie.txt', "r").read()
    print(session_cookie)
    cookie = cookiejar.CookieJar()
    cookie.set_cookie(cookiejar.Cookie(version=0, name='session',
                                       value=session_cookie,
                                       port=None, port_specified=False, domain='.adventofcode.com',
                                       domain_specified=True, domain_initial_dot=True, path='/', path_specified=True,
                                       secure=False, expires=None, discard=True, comment=None, comment_url=None,
                                       rest=None))

    
    

    # Fetch the input data for Day day
    url = str.format('https://adventofcode.com/{year}/day/{day}/input', year=year, day=day)
    response = requests.get(url, cookies=cookie)
    
    # Check the response status code
    if response.status_code != 200:
        print('Session cookie is invalid.')
        return
    
    # Print the input data
    return response.text
