# loginapp-tki
This is a django application with login functionlaity handled by session handling.If the user is authenticated user that exsists in our database they will be redirected to profile page else the error is displayed.

 Instructions to run the setup locally-
1. Make sure you have cloned the project.
2. Install the packages provided in requirements.txt file.
3. Before starting the server please provide the databse details in settings.py-
 DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql',
      'NAME': 'loginapp', //schema
      'USER': 'root', //user name
      'PASSWORD': 'Shruti@123', //password
      'HOST':'localhost', //host
      'PORT':'3306', //port
  }

 }
 4. After successfully connecting your project to the db, rune migrations-
Python manage.py makemigrations (this will make new migrations if any db model is changed, ie. models.py)
Python manage.py migrate (For now this will make all db changes to your schema that are present in the branch as of now)
5.After all these steps are done start your django server using the cmd- Python manage.py runserver
