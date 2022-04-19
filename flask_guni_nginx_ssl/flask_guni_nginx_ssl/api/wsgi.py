# Non docker-compose version
#from app import app
# Docker-compose version
from .app import app


if __name__ == "__main__":
    app.run()
