import pytest
from server import app, db
from server.models import Player, Score

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_score_creation(client):
    player = Player(name='Alice')
    db.session.add(player)
    db.session.commit()
    
    score = Score(player_id=player.id, score=10)
    db.session.add(score)
    db.session.commit()

    retrieved_score = Score.query.filter_by(player_id=player.id).first()
    assert retrieved_score is not None
    assert retrieved_score.score == 10
