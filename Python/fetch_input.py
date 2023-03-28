import requests
import http.cookiejar as cookiejar


def fetchOnline(year, day):
    if year < 2015 or year > 2022 or day < 1 or day > 25:
        print("Invalid year or day")
        return

    # Set the session cookie : get manually from the browser
    session_cookie = open("../../session_cookie.txt", "r").read()
    print(session_cookie)
    cookie = cookiejar.CookieJar()
    cookie.set_cookie(cookiejar.Cookie(version=0, name='session',
                                       value=session_cookie,
                                       port=None, port_specified=False, domain='.adventofcode.com',
                                       domain_specified=True, domain_initial_dot=True, path='/', path_specified=True,
                                       secure=False, expires=None, discard=True, comment=None, comment_url=None,
                                       rest=None))

    # Make a request to the URL with the session cookie
    response = requests.get("https://adventofcode.com/2015/day/1/input", cookies=cookie)

    # Check the response status code
    if response.status_code != 200:
        print('Session cookie is invalid.')
        return

    # Fetch the input data for Day 1
    url = str.format('https://adventofcode.com/{year}/day/{day}/input', year=year, day=day)
    response = requests.get(url, cookies=cookie)

    # Print the input data
    return response.text
