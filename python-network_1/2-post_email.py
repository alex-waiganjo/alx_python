#!/usr/bin/env python3
import requests  # Import the requests module for making HTTP requests
import sys      # Import the sys module for accessing command-line arguments

# Get the URL and email from the command-line arguments
url = sys.argv[1]
email = sys.argv[2]

# Create a dictionary containing the email parameter
data = {'email': email}

# Make an HTTP POST request to the URL with the email parameter
response = requests.post(url, data=data)

# Display the body of the response
print(response.text)