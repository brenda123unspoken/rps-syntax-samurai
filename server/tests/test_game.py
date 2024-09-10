import pytest
from server.game_logic import determine_winner, get_user_choice

def test_determine_winner():
    # Test various game outcomes
    assert determine_winner(0, 0) == "It's a draw"
    assert determine_winner(0, 1) == "Player 2 wins!"
    assert determine_winner(0, 2) == "Player 1 wins!"
    assert determine_winner(1, 2) == "Player 2 wins!"
    assert determine_winner(2, 1) == "Player 1 wins!"

def test_get_user_choice(monkeypatch):
    # Mock input to return a specific choice
    def mock_input(prompt):
        return '0'
    
    monkeypatch.setattr('builtins.input', mock_input)
    choice = get_user_choice("Player")
    assert choice == 0

    # Test invalid input handling
    def mock_input_invalid(prompt):
        return 'invalid'
    
    monkeypatch.setattr('builtins.input', mock_input_invalid)
    choice = get_user_choice("Player")
    assert choice == None  # or whatever the default behavior is for invalid input
