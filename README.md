Dataducks
===

## The project 🧙
That is a project that was created to help scientists to figure out how they can help ducks. There is a form that consists of a bunch of questions needed to find parameters, where a user will be able to inform his/her routine feeding ducks and an administrative area where scientists can log, check information registered using different filters, getting/generating reports about these searches.

It is hosted in HEROKU and can be checked here: [Dataducks](https://demo-dataducks.herokuapp.com/)

* Started on 16/04/2020
* Finished on 19/04/2020

## Stack 💻
* Python
* Django
* Google Recaptcha to avoid bots
* Google Maps to get address in a friendly way
* Material Design
* Django Rest Framework to support extensions to other cools things like React or Angular. 

## Browser Support (tested on) 🌎
* Chrome latest
* Firefox latest
* Brave latest

## Features ⭐️
* Home
  * Fill the form, which validates the data.
  
* Admin 
  * Uses the information, generating reports. The module has access to all other modules, being able to CRUD all the data.
  
* RESTFUL 
  * Offers a REST API to all models registered being easy to extend the functionalities. 

## How to install? 🔧
STEPS TO INSTALL THE APP in your local

- Clone the repo
- Run in cmd "source dataducks-venv/bin/activate" to enable the venv
- Run pip3.7 install -r requirements.txt to install dependencies in venv
- Create db config to your Postgresql (DB_NAME, DB_USER, DB_PASS, PORT)
- Rename .env.example to .env and check the keys in .env, adding their values
- Run in cmd "python manage.py migrate --run-syncdb" to update db with some app dependencies, synchronizing even if your cache not helps you
- Create a superuser to make it easier to create and check data, using the cmd "python manage.py createsuperuser" and follow the instructions

## Approach ⚙️
The project started with the mission of create some technical support in the given challenge to build a web app that was able to generate a form and some reports about that data.

In a first moment a lot of techs could be used, but the decision was based with the tools that the software could use taking less time as possible. I wondered a little bit about how to attend the points giving a good relevance to important points like security, good access to data using REST, authentication. 

All of that using a tool where I could reach great performance, talking about time and delivery. I also thought about the possibility of data being used by a scientist, becoming important to choose some technologies with support to that kind of extension, which influenced my decision. 

So, I decided to use Django/Python and Mongo. I changed that to Postgresql because of Heroku's deployment, but that options looks great since the support to extend the app to DataScience apps just become better using Postgresql and Python. 

## What I'd do differently 🔮💣️
1. I would create a better layout, using more images, background and probably some animation.

2. I would love to use React, Angular or Vue, increasing more reactivity concepts. In a first moment I checked this, installing webpack and things like that but after a while I realized it was unnecessary, since I would use just a single page to the form. Anyways short deadlines requires taking some shortcuts.

3. Having more time I probably would think in how to increment the functionalities. 

4. I wouldn't use Mongo in a Heroku project since I faced unexpected problems to config that there, wasting a time where other things could be done.

5. I would dev thinking more about the tests, but Django does a lot of work alone, which is a good and bad thing, at the same time.

6. I would like to adapt and use an amazing boilerplate that I've found, created by great souls. It uses a lot of good things like CI, Docker, Celery, Sentry, React, completely architecture separation, all already configurated, which sounds really nice. Open [https://github.com/vintasoftware/django-react-boilerplate](https://github.com/vintasoftware/django-react-boilerplate) to check!

7. I would have created a tokenized endpoint to access online the data using third party apps. It would be amazing put this to run in React Native, as example.

## Final notes 📔
I am really happy with the results! This was a graceful experience!

___

