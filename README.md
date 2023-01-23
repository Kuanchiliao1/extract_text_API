# Extract Text API

This is a simple API that takes a website URL as input and returns the plain text of the website.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.x
- Flask
- requests
- beautifulsoup4

### Installing

1. Clone the repository
```
git clone https://github.com/<your-username>/extract-text-api.git
```

2. Navigate to the project directory
```
cd extract-text-api
```

3. Install the dependencies
```
pip install -r requirements.txt
```


### Running the app

To run the app, use the following command:
```
python app.py
```

The app will be running on http://localhost:5000/

### Testing the app

You can test the app by sending a GET request to the endpoint with a website URL as a query parameter.
For example, you can use the following curl command to test the app:
```
curl http://localhost:5000/extract?url=http://example.com
```

## Built With

* [Flask](https://flask.palletsprojects.com/en/2.1.x/) - The web framework used
* [requests](https://requests.readthedocs.io/en/latest/) - Used to send HTTP requests
* [beautifulsoup4](https://beautiful-soup-4.readthedocs.io/en/latest/) - Used to parse HTML