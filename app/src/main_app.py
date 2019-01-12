from config import DEBUG, HOST, PORT
from src.util.utils import get_pg_installed_app
from src.controllers import (users)

def get_app():
    app  = get_pg_installed_app()
    app.mount('/user/', users.get_app())

    return app

if __name__ == "__main__":
    app = get_app()
    app.run(host=HOST, port=PORT, debug=DEBUG)
