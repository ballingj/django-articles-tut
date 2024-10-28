## This Django project was built inside a VM using vagrant
### Workflow
1. start from a project directory in your dev PC
  -- mine is /e/courses/django-vagrant
2. setup git and github
3. Create the Vagrantfile, but replace the content with the link in Vagrant section below
4. Start and connect to vagrant VM
5. Initiate venv in home directory and activate
6. Install dependencies via requirements.txt
7. Start a project and start an app
8. Update settings.py
9. Start developing

### Vagrant 
Install and initiate vagrant
```sh
vagrant init ubuntu/jammy64
```
replace the Vagrantfile content with this content
https://raw.githubusercontent.com/ballingj/drf_userprofile/main/Vagrantfile

Start the VM
```sh
vagrant up
```

Connect to vagrant
```sh
vagrant ssh
cd /vagrant   #/vagrant is synchronized with PC's project folder
```

disconnect from VM
```sh
exit
```

### initiate venv inside vagrant and activate venv
venv needs to go to home directory which is /home/vagrant: we do this because we don't want to synchronize venv files with local machine.
```sh
python -m venv ~/venv
source ~/venv/bin/activate
```

### Install dependencies vie requirements.txt
contents of requirements.txt:
django=5.0.4
djangorestframework=3.15.1

```sh
pip install -r requirements.txt
```

#### Start project
```sh
django-admin startproject my_project .
```

#### Start a new App
```sh
python manage.py startapp my_app
```

### Update settings.py
```python
INSTALLED_APPS = [
# ...
'rest_framework',
'rest_framework.authtoken',  # for authorization
'profiles_api.apps.ProfilesApiConfig',
# ...
]
```

### Start Developing
#### Start server in VM using the exposed ip setup in vagrant file
```sh
python manage.py runserver 0.0.0.0:8000
```

#### Configue the custom user model
at the botom of settings.py add
```
AUTH_USER_MODEL = 'profiles_api.UserProfile'
```

### CORS
Ref - https://www.stackhawk.com/blog/django-cors-guide/

1. Install CORS: 
```sh
pip install django-cors-headers
```

2. Update settings.py and add corsheader in istalled apps and middleware section
```python
INSTALLED_APPS = [
...
'corsheaders',
...
]

MIDDLEWARE = [
...,
'corsheaders.middleware.CorsMiddleware',
'django.middleware.common.CommonMiddleware',
...,
]

```

3. Set allowed origins
```python
 CORS_ALLOWED_ORIGINS = ['http://127.0.0.1'] 

 ```
