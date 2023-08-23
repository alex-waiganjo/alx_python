#!/usr/bin/env python3
import requests  # Import the requests module for making HTTP requests
import sys      # Import the sys module for accessing command-line arguments

# Get the letter from the command-line argument, or set it to an empty string if not provided
letter = sys.argv[1] if len(sys.argv) > 1 else ""

# URL for the POST request
url = 'http://0.0.0.0:5000/search_user'

# Create a dictionary containing the letter parameter
data = {'q': letter}

# Make an HTTP POST request to the URL with the letter parameter
response = requests.post(url, data=data)

# Try to parse the response body as JSON
try:
    json_data = response.json()
    # Check if the JSON data is empty
    if not json_data:
        print("No result")
    else:
        print("[{}] {}".format(json_data['id'], json_data['name']))
# Handle cases where the response is not valid JSON
except ValueError:
    print("Not a valid JSON")