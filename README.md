# Face Auth

Implement a Facebook app with the following features :

* Please use Python / Django. Make sure to implement a clean, well-structured and high-performance database scheme;
* The user should connect/login with Facebook (logout accordingly) (Note: Plugins can be used);
* The Facebook app should simply provide the following output: the name and profile picture of the logged-in user;
* The token, which will be stored for the user in the database, should be a long living access token;
* If the user removes the Facebook app, the user shall be marked as "is_active = false" in the database (Note: Facebook DeAuth callback);
* Please be efficient when writing your code and commit your code in a github.com repository. Pay attention to clean commits.


https://developers.facebook.com/docs/facebook-login/access-tokens

https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/v2.4

https://developers.facebook.com/docs/facebook-login/manually-build-a-login-flow/v2.1#deauth-callback




# Introduction

This is a demo repository for signup with facebook in Django using the social_django library with minimal configuration.

Facebook Facebook DeAuth callback URL : http:localhost:8000/deauthtication/

## Requirements
    pip install -r requirement.txt

## Database
    sqlite3

## Running the application
    Clone the project to your machine [https://github.com/Varnan/faceauth.git]
    Navigate into the diretory [cd faceauth]
    Create a virtualenv
    Install the dependencies on virtaulenv [pip install -r requirement.txt]
    Update the local_settings.py file with your keys from Facebook.
    Navigate into the faceauth directory [cd faceauth]
    Start the backend server [python manage.py runserver]
    Visit the application on the browser - http:localhost:8000

## Built With
    Python - A programming language that lets you work quickly and integrate systems more effectively.
    Django - A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
