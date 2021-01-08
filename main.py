from flask import Flask

config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 60 * 20
}
app = Flask(__name__)
app.config.from_mapping(config)

from controller import *
from dbhelper import *

if __name__ == "__main__":
    create_connection(r"pythonsqlite.db")
    app.run()

