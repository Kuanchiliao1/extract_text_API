# Import request module from flask
from flask import Flask, request
import requests
from bs4 import BeautifulSoup

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