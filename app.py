# Import request module from flask
from flask import Flask, request
import requests
from bs4 import BeautifulSoup

# Tells Flask to use current script(module) as the application
app = Flask(__name__)

# Define the endpoint and HTTP request method
@app.route("/extract", methods=["GET"])
def extract_text():
  # grab url from query parameter of GET request
  url = request.args.get("url")
  print(request.args)
  
  # send GET request to url, returning the HTML response
  response = requests.get(url)
  print(response)

  # Retrieve text and parse it with BeautifulSoup
  soup = BeautifulSoup(response.text, "html.parser")

  # Extract plain text
  text = soup.get_text()
  return text

if __name__ == "__main__":
  app.run()


# Notes:
# 1. What does @app.route allow us to do?
# 2. What is app?
# 3. On which line is `request` defined?

# 1. The @app.route decorator is used to bind a function to a specific URL route. 
# 2. Instance of the flask class and the main entry point for Flask application
# 3. 1