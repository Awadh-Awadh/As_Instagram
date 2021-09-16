# As InstaClone
This is an Independent project for Moringa Core Django module, september 10 2021.

## Author
Awadh Said

### Description
This a clone of Instagram. But it's not exactly as Instagram just a simple application that looks same as instagram where users can be able to see posts there and comment on different posts. Users can also edit their profiles and check their specific posts.

### features
- The home page allows users to see various posts
- User can see all comments
- Users can also search for username
- Admin can edit their profile
- Users can also edit their profile

### Deployed link
https://awadhinsta.herokuapp.com/

##### Cloning the repository:

https://github.com/Awadh-Awadh/As_Instagram.git

#### Install and activate Virtual
 ```bash 
-  - pipenv shell 
```  

##### Navigate into the folder and install requirements  
 ```bash 
cd gallery pipenv  install -r requirements.txt 
#### Install Dependencies  
 ```bash 
 pipenv install -r requirements.txt 
```  
##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations <database name>
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 

### run app
 ```bash 
 python manage.py runserver 
```  
##### Runing the application 
 ```bash 
 python manage.py runserver
```
Open the application on your browser `127.0.0.1:8000`.  

## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.1](https://docs.djangoproject.com/en/3.0/) 
* [Heroku](https://heroku.com)  
* [Git](for version control)

## License

- Licensed under[MIT license](license).
