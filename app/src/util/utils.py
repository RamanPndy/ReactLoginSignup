from bottle import Bottle, response
from app.src.config import DB_NAME, DB_USER, DB_PASS
import bottle_pgsql

def enableCORSGenericRoute():
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'

def get_pg_installed_app():
    app = Bottle()
    plugin = bottle_pgsql.Plugin('dbname={} user={} password={}'.format(DB_NAME, DB_USER, DB_PASS))
    app.install(plugin)
    app.route('/<:re:.*>', method='OPTIONS', callback=enableCORSGenericRoute)
    app.add_hook("after_request", enableCORSGenericRoute)
    return app
