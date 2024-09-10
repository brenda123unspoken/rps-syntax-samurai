import pytest
from server import app, db
from server.models import Player

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

def test_player_creation(client):
    player = Player(name='Alice')
    db.session.add(player)
    db.session.commit()

    retrieved_player = Player.query.filter_by(name='Alice').first()
    assert retrieved_player is not None
    assert retrieved_player.name == 'Alice'

def test_player_name_unique(client):
    player1 = Player(name='Bob')
    player2 = Player(name='Bob')  # Same name
    db.session.add(player1)
    db.session.commit()

    with pytest.raises(Exception):  # Or specific exception type if using unique constraint
        db.session.add(player2)
        db.session.commit()
