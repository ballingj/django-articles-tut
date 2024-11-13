# Django Application demonstrating different ways to implement the MVT Patterns

1. Articles is the first app is done here following a tut by Teclado.  App and Pages are done with Class Based Views (CBV)
https://www.udemy.com/course/full-stack-django/

2. The Todo app is done with Function Based Views (FBV).  This was added after looking a way to deploy the app via Docker instead of Vagrant.  Here is the tut:
https://github.com/betterstack-community/django-todo-app/


3. Build the docker image and run -- make sure to be in the project directory
  a. Build the image 
  ``` sh
  docker docker build -t django-salvatierra-tut . 
  ```
  b. run the image
  ``` sh
  docker run -p 8005:8000 --name django-salvatierra-tut -v "(pwd):/app" django-salvatierra-tut
  ```
