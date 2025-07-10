from flask import Flask
from routes import bp as routes_bp
from database import init_db

app = Flask(__name__)
app.register_blueprint(routes_bp)

# Call DB init immediately
init_db()

if __name__ == '__main__':
    app.run(debug=True)