# seed.py

from server.app import create_app
from server.extensions import db
from server.models.game import Game
from server.models.player import Player
from server.models.score import Score
import uuid

# Create an application context
app = create_app()
app.app_context().push()

def seed_data():
    # Add game data
    game1 = Game(id=uuid.uuid4(), name="Game 1", result="Win")
    game2 = Game(id=uuid.uuid4(), name="Game 2", result="Lose")
    
    # Add player data
    player1 = Player(id=uuid.uuid4(), name="Player 1", score=0)
    player2 = Player(id=uuid.uuid4(), name="Player 2", score=0)
    
    # Add score data
    score1 = Score(id=uuid.uuid4(), player_id=player1.id, score=100)
    score2 = Score(id=uuid.uuid4(), player_id=player2.id, score=150)
    
    # Add to session and commit
    db.session.add_all([game1, game2, player1, player2, score1, score2])
    db.session.commit()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully.")
