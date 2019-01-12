from bottle import request
from src.util.utils import get_pg_installed_app
from src.models.users import LoginSignUp

def get_app():
    app = get_pg_installed_app()

    app.post('/register', callback=register_user)
    app.post('/login', callback=login_user)
    app.post('/update', callback=update_user)
    app.post('/delete', callback=delete_user)
    app.get('/<username>', callback=get_user)
    app.get('/', callback=get_all_users)

    return app

def register_user(db):
    return LoginSignUp(db).register_user(request.json['username'], request.json['email'], request.json['password'])

def login_user(db):
    return LoginSignUp(db).login_user(request.json['username'],  request.json['password'])

def get_all_users(db):
    return LoginSignUp(db).get_all_users()

def get_user(db, username):
    return LoginSignUp(db).get_user(username)

def update_user(db):
    return LoginSignUp(db).update_user(request.json['username'], request.json['email'], request.json['password'])

def delete_user(db):
    return LoginSignUp(db).delete_user(request.json['username'])
