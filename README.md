## Project : Create a local API endpoint using Django Backend Server create in Django REST Framework


**Please read the whole document carefully before getting on to work. In case of any issue or confusion, please contact us ASAP.**

### Description

The Server we are going to create is a wrapper on an open source weather API.
We want to expose an API endpoint, which underneath
Makes an API call to the open source weather API
Gets the response in json format
Returns the same json data received above and send it to the API caller

### Project Guidelines

The API endpoint will have a url “/weather_data/”
The endpoint “/weather_data/” takes one Http parameter
Parameter name : city
Variable type : string
What does the Server do when “/weather_data/” endpoint is hit
Make a call to “api.openweathermap.org/data/2.5/weather?q={city}&appid={API key}”
Receive the response
Return this response to the caller as if it was our Server’s response
To summarize, The Server will make an API call to an open API service and return the response back to the User calling the API

### NOTE:
Use this API key = dfd763dcff52ad64fddb4e8b8a5502f0

### Project Keywords

- Django REST Framework
- Request
- Response
- Query Params
- For Python installation check the post at https://docs.python-guide.org/starting/installation/
- For creating virtual environment, use venv OR pipenv
- Essential/Helpful Python packages
  - Django
  - djangorestframework
  - Requests
- HTTP
- API
- JSON


### Spending too much time on installation?

Use this project as your base and build on top of it.

You can create a branch and push all your code into it, please don’t touch other candidate’s branches.

You can also make a zip of your project and mail it to ….@gmail.com
