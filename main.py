
# Import the necessary libraries
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

# Create a Flask app
app = Flask(__name__)

# Configure the database connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@host:port/database_name'
db = SQLAlchemy(app)

# Create a model for the Player table
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)

# Define the home route
@app.route('/')
def index():
    # Query the database for all players
    players = Player.query.all()
    
    # Return the player_list.html template with the players data
    return flask.render_template('player_list.html', players=players)

# Run the app
if __name__ == '__main__':
    app.run()
