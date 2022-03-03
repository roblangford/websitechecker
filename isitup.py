#!/usr/bin/env python3
"""
Simple script to test if a website is online.

Usage:
    python3 isitup.py <URL>

Args:
    URL: Full url of the website to check.
"""

# Libraries
import sys
import requests

def isitup(url):
    """
    Send a get request to url and return response code

    Args:
        URL: Full url of the website to check.
    
    Returns:
        Response Object:
        Parameter/Method - Description
        apparent_encoding - Returns the apparent encoding
        close() - Closes the connection to the server
        content - Returns the content of the response, in bytes
        cookies - Returns a CookieJar object with the cookies sent back from the server
        elapsed - Returns a timedelta object with the time elapsed from sending the request to the arrival of the response
        encoding - Returns the encoding used to decode r.text
        headers - Returns a dictionary of response headers
        history - Returns a list of response objects holding the history of request (url)
        is_permanent_redirect - Returns True if the response is the permanent redirected url, otherwise False
        is_redirect - Returns True if the response was redirected, otherwise False
        iter_content() - Iterates over the response
        iter_lines() - Iterates over the lines of the response
        json() - Returns a JSON object of the result (if the result was written in JSON format, if not it raises an error)
        links - Returns the header links
        next - Returns a PreparedRequest object for the next request in a redirection
        ok - Returns True if status_code is less than 400, otherwise False
        raise_for_status() - If an error occur, this method returns a HTTPError object
        reason - Returns a text corresponding to the status code
        request - Returns the request object that requested this response
        status_code - Returns a number that indicates the status (200 is OK, 404 is Not Found)
        text - Returns the content of the response, in unicode
        url - Returns the URL of the response
    """
    response = requests.get(url)

    return(response)


def main(url):
    # Call the isitup function, passing the input url
    response = isitup(input_url)
    print(response.reason, response.status_code)



if __name__ == '__main__':
    # Check if there has been an input argument
    try:
        # default input argument is 2nd item in the list
        input_url = sys.argv[1]
    except:
        # if no argument provided ask for a website url to check
        input_url = input("Please input a URL to check: ")
    # call main function with either calling url or user input url
    main(input_url)