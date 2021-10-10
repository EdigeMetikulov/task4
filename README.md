# Courses
---
API for users to view information about courses and manage it.
# Getting started
---
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
# Prerequisites
This is a project written using Python, Django and Django Rest Framework
Clone the repository
```
https://github.com/EdigeMetikulov/task4.git
```
Create the virtual enviroment
 ```
python3 -m venv venv
source venv/scripts/activate
```
Install the requirements
```
pip install -r requirements.txt
```
In your terminal:
```
python manage.py makemigrations
python manage.py migrate
```
8. Create a new superuser
```
python manage.py createsuperuser
```
9. Run the server
```
python manage.py runserver
```
# Built With

> ### `Django` - The framework used
> ### `Django Rest Framework` - The toolkit used to build API
> ### `Apiary` - for API documentation
# Apiary

Go to: 
https://courses312.docs.apiary.io/