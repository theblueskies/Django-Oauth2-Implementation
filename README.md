# Django-Oauth2-Implementation


This is an implementation of Django with django-oauth-toolkit to provide an Oauth2 token service. The main objective is to have a working example of a protecting an endpoint and how to access it with a generated token.



## Explanation and Demo

1. Start the server with python manage.py runserver
..a. The admin user is: test_admin. the password is also: test_admin
..b. Logging in as admin is necessary before you can get access to 127.0.0.1:8000/o/applications

2. Next, access the registered application at: 127.0.0.1:8000/o/applications. There should be a registered application called "ZAuth". Feel free to register a new one. Be sure to note down the **CLIENT ID** and **CLIENT SECRET**. You will need the Client ID and Client Secret to get a token. 

3. The example protected endpoint is: 127.0.0.1:8000/list_user. Try accessing it with a get request over the browser, or with a regular command line get request with your favorite library. You should get a 401 Error for unauthorized access.

4. To access that protected endpoint, api_access_example.py shows a working connection. It first calls 
127.0.0.1:8000/o/token with the user id and password to retrieve a token. This token is then passed in 
as an Authorization header to access the endpoint /list_user. /list_user maps to the class **RestrictedListUserEndpoint** in views.py. (I have prepopulated db.sqlite with two users:
test_user1 and test_user2. the passwords are the same as the usernames.)

5. Now go and write your own protected endpoints. The **RestrictedListUserEndpoint** endpoint in views.py should be what you need to be on your way!!

