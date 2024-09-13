# # # seed.py

# # from server.app import create_app
# # from server.extensions import db
# # from server.models.game import Game
# # from server.models.player import Player
# # from server.models.score import Score
# # import uuid

# # # Create an application context
# # app = create_app()
# # app.app_context().push()

# # def seed_data():
# #     # Add game data
# #     game1 = Game(result="Win")
# #     game2 = Game(result="Lose")
    
# #     # Add player data
# #     player1 = Player(id=uuid.uuid4(), name="Player 1", score=0)
# #     player2 = Player(id=uuid.uuid4(), name="Player 2", score=0)
    
# #     # # Add score data
# #     # score1 = Score(id=uuid.uuid4(), player_id=player1.id, score=100)
# #     # score2 = Score(id=uuid.uuid4(), player_id=player2.id, score=150)
    
# #      # Add score data
# #     score1 = Score(player_id=player1.id, wins=10, losses=5, draws=2)
# #     score2 = Score(player_id=player2.id, wins=8, losses=7, draws=3)
    
# #     # Add to session and commit
# #     db.session.add_all([game1, game2, player1, player2, score1, score2])
# #     db.session.commit()

# # if __name__ == "__main__":
# #     seed_data()
# #     print("Database seeded successfully.")
# from server.app import create_app
# from server.extensions import db
# from server.models.game import Game
# from server.models.player import Player
# from server.models.score import Score
# import uuid

# # Create an application context
# app = create_app()
# app.app_context().push()

# def seed_data():
#     # Add game data
#     game1 = Game(result="Win")
#     game2 = Game(result="Lose")
    
#     # Add player data
#     player1 = Player(id=str(uuid.uuid4()), name="Player 1", score=0)
#     player2 = Player(id=str(uuid.uuid4()), name="Player 2", score=0)
    
#     # Add score data
#     score1 = Score(player_id=player1.id, wins=10, losses=5, draws=2)
#     score2 = Score(player_id=player2.id, wins=8, losses=7, draws=3)
    
#     # Add to session and commit
#     db.session.add_all([game1, game2, player1, player2, score1, score2])
#     db.session.commit()

# if __name__ == "__main__":
#     seed_data()
#     print("Database seeded successfully.")
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
    # Check for existing data to avoid duplicates
    existing_players = {p.name for p in Player.query.all()}

    # Add game data
    game1 = Game(result="Win")
    game2 = Game(result="Lose")

    # Add player data, ensuring no duplicates
    players = [
        {'id': str(uuid.uuid4()), 'name': "Player 1", 'score': 0},
        {'id': str(uuid.uuid4()), 'name': "Player 2", 'score': 0}
    ]
    
    for player_data in players:
        if player_data['name'] not in existing_players:
            player = Player(id=player_data['id'], name=player_data['name'], score=player_data['score'])
            db.session.add(player)
            existing_players.add(player_data['name'])  # Update the set of existing player names
    
    # Add score data
    scores = [
        {'player_id': players[0]['id'], 'wins': 10, 'losses': 5, 'draws': 2},
        {'player_id': players[1]['id'], 'wins': 8, 'losses': 7, 'draws': 3}
    ]
    
    for score_data in scores:
        score = Score(player_id=score_data['player_id'], wins=score_data['wins'], losses=score_data['losses'], draws=score_data['draws'])
        db.session.add(score)

    # Add to session and commit
    db.session.add_all([game1, game2])
    db.session.commit()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully.")

