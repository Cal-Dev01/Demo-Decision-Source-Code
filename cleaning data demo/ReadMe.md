Application Overview:
The provided Flask application is designed to clean and transform customer data in JSON format. It exposes a simple web interface to upload and clean customer data, and it also offers an API endpoint to process the data programmatically.

Getting Started:

Installation:

To run the application, you need to have Python and Flask installed on your system. If you haven't already installed Flask, you can do so using pip:

```pip install Flask```

Running the Application:

You can start the Flask application by running the app.py script:


```python app.py```

This will start a local development server, and you can access the application in your web browser at http://localhost:5000.

**Application Structure:**

* app.py: This is the main application file that defines the Flask web application.
* cleandata.html: This HTML template is used to render the web interface for data cleaning.


Functionality:

Web Interface:

When you access the application in your web browser, it points to the cleandata.html template, which provides a simple web form for uploading JSON data. After submitting the form, the data is cleaned and transformed, and the cleaned data is displayed on the web page.

**Data Cleaning Function:**

The core data cleaning logic is defined in the clean_customer_data function in app.py. This function takes a list of customer data in JSON format as input and performs the following cleaning operations:

* It checks if the JSON object contains a 'name' field and ensures that it is a string.
* It strips leading and trailing spaces from the 'name' field.
* It splits the 'name' field into first and last names.
* It capitalizes the first letter of the first and last names.

It introduces new fields in the JSON object, including 'first_name', 'last_name', 'full_name', and 'creation_date'.
'full_name' is set to the cleaned name.
'creation_date' is set to the current date and time.


**API Endpoint:**

The application also provides an API endpoint at /clean_customers. This endpoint accepts POST requests with JSON data for cleaning. You can send JSON data to this endpoint, and it will return the cleaned data in JSON format. If there are any errors during the cleaning process, it will return an error message.

**Usage:**

To use the web interface, access the application in your web browser, upload a JSON file, and click the "Clean Data" button.
To use the API endpoint, send a POST request with JSON data to http://localhost:5000/clean_customers (when the application is running). The API will return the cleaned data.

**Note:**

This application is intended for educational purposes and demonstrates data cleaning techniques using Flask.
The application is not production-ready and should be further secured and optimized for real-world use.

**_if you have any difficulties running the demo do well to email me: `caleb.eghan@law.ac.uk`_**