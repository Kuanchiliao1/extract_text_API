from flask import Flask
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Add something here about method action and endpoint
@app.route('/extract', methods['GET'])

def extract()
  url = request.args.get("URL")
  
  request = request.get(url)
  
  # Retrieve text and parse it
  text = request(request.text, "parse-text")
  return text


app.run()