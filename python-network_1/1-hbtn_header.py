#!/usr/bin/env python3
import requests  # Import the requests module for making HTTP requests
import sys      # Import the sys module for accessing command-line arguments

# Get the URL from the command-line argument
url = sys.argv[1]

# Make an HTTP GET request to the URL
response = requests.get(url)

# Get the value of the 'X-Request-Id' header from the response
x_request_id = response.headers.get('X-Request-Id')

# Display the value of the 'X-Request-Id' header
print(x_request_id)