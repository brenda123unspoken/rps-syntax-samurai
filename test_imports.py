import sys
import os

# Adjust the PYTHONPATH to include the root of your project
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'server')))

def test_imports():
    try:
        from server.app import create_app
        print("Successfully imported create_app from server.app")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.resources.game_resource import bp as game_bp
        print("Successfully imported game_bp from server.resources.game_resource")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.resources.player_resource import bp as player_bp
        print("Successfully imported player_bp from server.resources.player_resource")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.resources.score_resource import bp as score_bp
        print("Successfully imported score_bp from server.resources.score_resource")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.models.game import Game
        print("Successfully imported Game from server.models.game")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.models.player import Player  # Fixed typo here
        print("Successfully imported Player from server.models.player")
    except ImportError as e:
        print(f"Import failed: {e}")

    try:
        from server.models.score import Score
        print("Successfully imported Score from server.models.score")
    except ImportError as e:
        print(f"Import failed: {e}")

if __name__ == "__main__":
    test_imports()
