Python Tutorial

Installing and Running Python:

Step 1: Install Python https://www.python.org/downloads/

Step 2: In Command Line. Navigate to: C:\Windows\System32>
Note: Command Line Previous Folder Command: CD ..
Note: Command Line First Folder Command: CD \

Step 3: Check python version in the command line: 
C:\Windows\System32>python --version

Step 4: Check PIP (Python Package Management) version in the command line: 
C:\Windows\System32>pip --version

Step 5: Install Virtual Environment: 
C:\Windows\System32>pip install virtualenvwrapper-win

Step 6: Navigate to the folder where you want to create a Virtual Environment:
C:\Users\ahmed\OneDrive\Desktop\Website-Python>mkvirtualenv python1
Note: Switch virtual environments by using: workon python1

Step 7: Install Django in the virtual Environment:
(python1) C:\Users\ahmed\OneDrive\Desktop\Website-Python>pip install django

Step 8: Start Django Project
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






