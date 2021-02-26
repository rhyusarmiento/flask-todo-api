# flask todo api

## Dependency Docs
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [Flask Marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/)
- [Marshmallow-sqlalchemy](https://marshmallow-sqlalchemy.readthedocs.io/en/latest/)
- [flask-cors](https://flask-cors.readthedocs.io/en/latest/)

## routes

### Create a single todo:
```json
{
    "method": "POST",
    "url": "http://localhost:5000/api/add-todo",
    "body": {
        "title": "Buy Food",
        "done": false
    },
    "Content-Type": "application/json"
}
```
### GET all todos:
```json
{
    "method": "GET",
    "url": "http://localhost:5000/api/get-all-todos",
}
```
### PATCH a single todo:
```json
{
    "method": "PATCH",
    "url": "http://localhost:5000/api/edit-done/TODO_ID",
    "body": {
        "done": true
    },
    "Content-Type": "application/json"
}
```
### DELETE a single todo:
```json
{
    "method": "DELETE",
    "url": "http://localhost:5000/api/delete-todo/TODO_ID",
}
```

## Installing the server
- While in the `app` folder, run the following commands in your terminal 
```
$ pipenv install
```
- Or 
```
$ pipenv --three
```

## Starting the server
- While in the `app` folder, run the following commands in your terminal 
```
$ pipenv shell
(app) python app.py
```

## Create DataBase
- If you need to setup your database you will need to do the following inside a python repl while in your pipenv shell.
- Make sure to be within the `app` folder directory
```
>>> from app import db
>>> db.create_all()
```
- This will then add an app.sqlite file to your local computer