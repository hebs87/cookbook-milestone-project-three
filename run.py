import os
from cookbook import create_app, mongo
from cookbook.config import Config

app = create_app(Config)

# Run the app
if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
            port=int(os.getenv("PORT", "5000")),
            debug=True)
