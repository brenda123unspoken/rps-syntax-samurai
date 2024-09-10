from .game_resource import GameResource
from .player_resource import PlayerResource
from .score_resource import ScoreResource



# Initialize resources with appropriate arguments
game_resource = GameResource(game_id=1)
player_resource = PlayerResource(player_id=1, name="Test Player", score=0)
score_resource = ScoreResource(player_id=1, score=0)