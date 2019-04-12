				Python/Django App Creation Steps

Installing and Running Python:

Step 1: Install Python https://www.python.org/downloads/

Step 2: In Command Line: Navigate to: C:\Windows\System32>
Note: Command Line Previous Folder Command: CD ..
Note: Command Line First Folder Command: CD \
Note: Check Directory: dir
Note: Make Folder: mkdir newfolder
Note: Disconnect Server Command Line: Ctrl + C


Step 3: Check python version in the command line: 
C:\Windows\System32>
Check Version: python –version
Mac Check Version: python3 --version
Version Details: python –

Step 4: Check PIP (Python Package Management) version in the command line: 
C:\Windows\System32>pip --version
Note: (Update Pip): C:\Windows\System32>python -m pip install --upgrade pip
Installing Pip on Mac: easy_install pip
Installing Pip with Admin permissions: sudo easy_install pip

Step 5: Install Virtual Environment: 
C:\Windows\System32>pip install virtualenvwrapper-win

Step 6: Navigate to the folder where you want to create a Virtual Environment:
C:\Users\ahmed\OneDrive\Desktop\Website-Python>mkvirtualenv python1
Note: Switch virtual environments by using: workon python1

Step 7: Install Django in the virtual Environment: (Installs Globally)
(python1) C:\Users\ahmed\OneDrive\Desktop\Website-Python>pip install django

Step 8: Create Django Project
(python1) C:\Users\ahmed\OneDrive\Desktop\Website-Python>django-admin startproject djangoproject
Note: creates Folder and Directory called “djangoproject” in this example.
 

Step 9: Navigate to djangoproject folder:
(python1) C:\Users\ahmed\OneDrive\Desktop\Website-Python>cd djangoproject


Step 10: Open project with Visual Studio Code:
(python1) C:\Users\ahmed\OneDrive\Desktop\Website-Python\djangoproject>code .

Step 11: Install Python Extension (Debugging & Intellisense)
 

Step 12: Run Python Webserver: C:\Users\ahmed\OneDrive\Desktop\Website-Python\djangoproject>python manage.py runserver

(Congratulations on your First Django-powered page!)


Setting up Databases:

Step 13: C:\Users\ahmed\OneDrive\Desktop\Website-Python\djangoproject>pip install mysqlclient
Note: Setting up a bigger database
Shortcut: Comment/Uncomment out Section of Code with Ctrl+/

Step 14: Launch XAMPP and start “Apache” along with the “MYSQL” Service. Then go to localhost/phpMyAdmin and create your database such as one called “djangoproject”  

Step 15: Go to Settings.py and Change Databases to the following:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djangoproject',
        'USER': 'root',
        'PASSWORD' : '',
        'HOST' : 'localhost',
        'PORT' : ''
    }
}


Applying Migrations (Related To Data):
Step 16: C:\Users\ahmed\OneDrive\Desktop\Website-Python\python manage.py migrate


Creating a Super User:
Step 17 C:\Users\ahmed\OneDrive\Desktop\Website-Python\python manage.py createsuperuser --username=ahmed --email=ahmedakhtar@yahoo.com
Note*: Enter Password.
Note*: Go to localhost.com/8000/admin to Log in to the Admin Area.

Creating an App:
Step 18 C:\Users\ahmed\OneDrive\Desktop\Website-Python\python manage.py startapp posts
Note: Creates an App called “posts” 

Step 19: Add App Name to settings.py
INSTALLED_APPS = [
    'posts'
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

