from flask import Flask, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__, template_folder='template')

# Define SQLAlchemy engine and session
engine = create_engine('mysql://root:password@localhost/games')
Session = sessionmaker(bind=engine)
session = Session()

# Define SQLAlchemy Base
Base = declarative_base()

# Define UserScore model
class UserScore(Base):
    __tablename__ = 'users_scores'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    score = Column(Integer)

# Create all tables defined in Base
Base.metadata.create_all(engine)

def score_server(name):
    if not isinstance(name, str):
        return "Name must be a string."

    # Query the database for the user's score
    user_score = session.query(UserScore).filter_by(name=name).first()

    if user_score:
        score = user_score.score
        return render_template('score_template.html', SCORE=score)
    else:
        return render_template('name_not_exist.html')

@app.route('/score/<name>')
def get_score(name):
    return score_server(name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
