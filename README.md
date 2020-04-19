# DATADUCKS

STEPS TO INSTALL THE APP in your local

- Clone the repo
- Run in cmd "source dataducks-venv/bin/activate" to enable the venv
- Run pip3.7 install -r requirements.txt to install dependencies in venv
- Create a db named "dataducks" in your Mongo
- Rename .env.example to .env and check the keys in .env, adding their values
- Run in cmd "python manage.py migrate" 
- Run in cmd "python manage.py makemigrations"
- Run again in cmd "python manage.py migrate"
- Create a superuser to make it easier create and check data, using the cmd "python manage.py createsuperuser" and follow the instructions

