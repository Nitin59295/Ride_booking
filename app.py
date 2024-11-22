from flask import Flask 
from flask_migrate import Migrate
from routes import main
from config import Config
from models import db


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(main)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
