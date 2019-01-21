# Combat Comm Fit

![CombatCommFit](static/img/SS_GABC.png?raw=true "CombatCommFit")

#### CONTEXT: While deployed, my commander asked me to provide a workout schedule for our team. This is an application meant for just that.

#### NOTE: This app was originally meant to display newspaper articles, hence the repo/project name.

#### HOW  TO CONTRIBUTE:

###### Contributions are always welcome!  Whether you are new to Django or web development in general (like me) or you're more experienced, you are more than welcome to contribute!

STEP 1: Clone the project (in the terminal): ```git clone git@github.com:tjdolan121/newspaper_proj.git```

STEP 1a: Remove /venv/ directory and .idea file in cloned repo.

STEP 2: Create a new virtual environment in a folder outside the main project folder: ```virtualenv env```

STEP 3: Activate the virtual environment: ```source env/bin/activate```

STEP 4: Navigate to the project directory (should contain "manage.py" file) and install requirements: ```pip install -r requirements.txt```

STEP 5: Obtain a SECRET_KEY: https://www.miniwebtool.com/django-secret-key-generator/

STEP 5: Create a .env file in the project directory

STEP 6: Add a secret key environment variable (in .env): ```SECRET_KEY=(paste key here)```

STEP 6a: In settings.py, comment out SECURE_SSL_REDIRECT and SECURE_PROXY_SSL_HEADER. Be sure to add them back in before committing.

STEP 7: Run migrations (while in project directory): ```python manage.py migrate```

STEP 8: Create a superuser account: ```python manage.py createsuperuser```

STEP 9: Run server: ```python manage.py runserver```

STEP 10: Navigate to http://127.0.0.1:8000/admin in browser, log in with your super user account, and create some data.

#### Commits to master are set to auto-deploy to the staging app, found here: https://combatcommfit.herokuapp.com

### Feel free to message me if you have any questions!
