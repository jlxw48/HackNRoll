from flask import Flask
from flask_caching import Cache
import os
import psycopg2

DATABASE_URL = os.environ.get("DATABASE_URL")

config = {
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 60 * 20  # 20 minutes expiry for session ids
}
app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

from controller import *

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
