from bottle import Bottle
from src.config import DB_NAME, DB_USER, DB_PASS
import bottle_pgsql

def get_pg_installed_app():
    app = Bottle()
    plugin = bottle_pgsql.Plugin('dbname={} user={} password={}'.format(DB_NAME, DB_USER, DB_PASS))
    app.install(plugin)
    return app
