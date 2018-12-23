# Okra mission 

# Set up web project in an  development environment

 - Initialize project: Create project directory mkdir okra-mission
 - Initialize git repository git init
 - Set up a virtual environment to use for the applicationw with the aim of creating isolating environment for Python projects.
    * install virtual environment tool with pip if don't have pip3 installed: pip install virtualenv in case pip3 installed the venv module should be already installed
    * to create a virtual environment inside the application directory run: 
     Python 2:  $ virtualenv env
     Python 3: $ python -m venv env
     this will create a directory env
    * execute activate file located in bin or libraries folder
     create readme.md .gitignore requirements.txt app.py readme.md
     pip install Flask==1.0.2
     update requierements file pip freeze > requirements.txt
 - Run the application
      * set flask_env=development
      * set flaks_app=app.py
      * flask run
 - Configure debug in visual studio code.

 - Configure github integration with visual studio code

# Set up web project in prodcution and staging environment
 - type nul > Procfile (windows) / touch Procfile (unix)   
 - add followinf file to teh created file web: gunicorn app:app
 - install gunicorn and add it to requirements file
      * pip install gunicorn==19.4.5
      * pip freeze > requirements.txt
 - specify the python version for that create a file called runtime.txt and type the 
 Python version to use.
 - commit changes in git
    

   