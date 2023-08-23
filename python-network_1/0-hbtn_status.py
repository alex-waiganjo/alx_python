#!/usr/bin/env python3
import requests  # Import the requests module for making HTTP requests

# URL to fetch
url = 'https://alu-intranet.hbtn.io/status'

# Make an HTTP GET request to the URL
response = requests.get(url)

# Display the body response in the specified format
print("Body response:")
# Display the type of the response content
print("\t- type: {}".format(type(response.text)))
# Display the content of the response
print("\t- content: {}".format(response.text))