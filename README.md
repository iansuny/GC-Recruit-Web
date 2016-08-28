GC-Recruit-Web
====

### Installation

+ Clone the repository and cd into the folder of this repo (GC-Recruit-Web).

+ Create your own virtual environment and install Django. You can put your virtualenv folder under ENV/, the .gitignore file contains this folder.
```
virtualenv ENV/ -p python3
```
+ Since we use python3, please add '-p python3' to make a virtual environment for python3. Then activate the virtual environment.
```
source ENV/bin/activate
```
+ After activating virtual environment, install Django in your virtualenv.
```
pip3 install django
```
+ Install ```psycopg2```.
```
pip3 install psycopg2
```
+ Add your own secret key for django server in recruitsite/secret.py. This file should contain one line.
```
DJANGO_SECRET_KEY = '<your own django secret key>'
```
This file will be automatically ignored by git and be included by other files which need the secret key.

+ After all the above settings are done, you can run the server with the following command:
```
python3 manage.py runserver 127.0.0.1:8080
```
This command will let the server listen 8080 port. If this port is already in use, please change it to any port > 1024 which is not in use.

If your server starts correctly, you can open your browser and visit http://localhost:8080 or http://127.0.0.1:8080.
Https is not supported by the current version.
