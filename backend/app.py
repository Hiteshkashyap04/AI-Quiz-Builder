from flask import Flask
from routes.quiz_routes import quiz_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.register_blueprint(quiz_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
