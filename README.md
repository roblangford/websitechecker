# websitechecker

This is a quick project to create an simple website monitor in Python3, this will being with a simple uptime check to ensure that the website is up and is returning status 200 (ok).

I currently work exclusively in AWS and will likely create a simple Lambda to regularly execute these checks and record the results.
This is to allow monitoring of both public and private endpoints and I plan on documenting this as the intended deployment.

## Planned Features

- Response time
- Date/Time Stamps 
- Certificate checks 
- Custom Headers 


## Research

### Requests
Python3 has a simple requests library to make HTTP/1.1 requests without all the hassle of crafting query strings or form-encoding.

```Python3
# import requests module
import requests

# Making a get request
response = requests.get('https://github.com/')

# print request status code and response
print(response.status_code, response.reason)

```


### HTTP protocol client
https://docs.python.org/3/library/http.client.html

## IsItUp

This is a simple script to send a get request to a url and print the reason and status code.

Execution: 

```bash
python3 isitup.py https://www.github.com
OK 200

python3 isitup.py
Please input a URL to check: https://github.com
OK 200

```