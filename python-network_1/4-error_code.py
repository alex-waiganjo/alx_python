#!/usr/bin/env python3
import requests  # Import the requests module for making HTTP requests
import sys      # Import the sys module for accessing command-line arguments

# Get the URL from the command-line argument
url = sys.argv[1]

# Make an HTTP GET request to the URL
response = requests.get(url)

# Display the body of the response
print(response.text)

# Check if the HTTP status code is greater than or equal to 400 (error)
if response.status_code >= 400:
    print("Error code: {}".format(response.status_code))