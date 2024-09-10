import pytest
from server import app, db
from server.models import Player
from server.services.game_service import play_game, get_or_create_player, update_scores

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

def test_get_or_create_player(client):
    player = get_or_create_player('Alice')
    assert player.name == 'Alice'
    assert player.id is not None

def test_update_scores(client):
    player1 = get_or_create_player('Alice')
    player2 = get_or_create_player('Bob')
    update_scores(player1, player2, 'Player 1 wins!')
    
    assert player1.score == 1
    assert player2.score == 0

def test_play_game(client):
    result = play_game('Alice', 'Bob')
    assert result in ['Player 1 wins!', 'Player 2 wins!', "It's a draw"]
