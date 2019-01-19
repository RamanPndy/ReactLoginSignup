from app.src.config import OK_STATUS_CODE, INTERNAL_SERVER_ERROR, ALREADY_EXIST, NOT_EXIST, PROVIDE_USER_INPUT

class LoginSignUp(object):

    def __init__(self, db):
        self.db = db

    def get_result_code(self, code):
        return {'result' : code}

    def register_user(self, username, email, password):
        if username and email and password:
            result = self.get_user(username).get('result', [])
            if result == NOT_EXIST:
                register_query = "INSERT INTO public.users (username, email, password) VALUES ('{}', '{}', '{}')".format(username, email, password)
                self.db.execute(register_query)
                return self.get_result_code(OK_STATUS_CODE)
            else:
                return self.get_result_code(ALREADY_EXIST)
        else:
            return self.get_result_code(PROVIDE_USER_INPUT)

    def login_user(self, username, password):
        result = self.get_user(username).get('result', [])
        if result != NOT_EXIST:
            login_query = "SELECT username, email FROM public.users WHERE username = '{}' AND password = '{}'".format(username, password)
            self.db.execute(login_query)
            r = self.db.fetchone()
            if r:
                return self.get_result_code(OK_STATUS_CODE)
            else:
                return self.get_result_code(NOT_EXIST)
        else:
            return self.get_result_code(NOT_EXIST)

    def get_all_users(self):
        users_query = "SELECT username, email FROM public.users"
        self.db.execute(users_query)
        rows = self.db.fetchall()
        if rows:
            return self.get_result_code(rows)
        else:
            return self.get_result_code(INTERNAL_SERVER_ERROR)

    def get_user(self, username):
        user_query = "SELECT username, email FROM public.users WHERE username = '{}'".format(username)
        self.db.execute(user_query)
        row = self.db.fetchone()
        if row:
            return self.get_result_code(row)
        else:
            return self.get_result_code(NOT_EXIST)

    def update_user(self, username, email, password):
        result = self.get_user(username).get('result', [])
        if result == NOT_EXIST:
            self.get_result_code(NOT_EXIST)
        else:
            if email and not password:
                email_query = "UPDATE pubilc.users SET email = '{}' WHERE username= '{}'".format(email, username)
                self.db.execute(email_query)
                self.get_result_code(OK_STATUS_CODE)
            if password and not email:
                password_query = "UPDATE pubilc.users SET password = '{}' WHERE username= '{}'".format(password, username)
                self.db.execute(password_query)
                self.get_result_code(OK_STATUS_CODE)
            if password and email:
                email_password_query = "UPDATE pubilc.users SET email = '{}', password = '{}' WHERE username= '{}'".format(email, password, username)
                self.db.execute(email_password_query)
                self.get_result_code(OK_STATUS_CODE)

    def delete_user(self, username):
        result = self.get_user(username).get('result', [])
        if result == NOT_EXIST:
            self.get_result_code(NOT_EXIST)
        else:
            delete_query = "DELETE FROM public.users WHERE username = '{}'".format(username)
            self.db.execute(delete_query)
            self.get_result_code(OK_STATUS_CODE)
