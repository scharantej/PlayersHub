## Flask Application Design

### HTML Files

**player_list.html:**

- This file will display the table of hockey player data.
- It should include a header with a title and navigation bar.
- The table should be generated dynamically based on the data retrieved from the database.
- It should include headers that are sortable by clicking on them.
- It should have a text input field for filtering the data by player name.
- It should have dropdown filters for selecting specific metrics to display in the table.

### Routes

**app.py:**

- This file will contain the Flask app definition and the routes.

```python
import flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:password@host:port/database_name'
db = SQLAlchemy(app)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)

@app.route('/')
def index():
    players = Player.query.all()
    return flask.render_template('player_list.html', players=players)

if __name__ == '__main__':
    app.run()
```