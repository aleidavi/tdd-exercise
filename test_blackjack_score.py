from main import blackjack_score
import pytest

# @pytest.mark.skip(reason="no way of currently testing this")
def test_score_for_pair_of_number_cards():
  # Arrange
  hand = [3, 4]
  result = 7
  # Act
  score = blackjack_score(hand)

  # Assert <-- Write assert statement here
  assert score == result

@pytest.mark.skip(reason="no way of currently testing this")
def test_facecards_have_values_calculated_correctly():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_11_where_it_does_not_go_over_21():
  pass


@pytest.mark.skip(reason="no way of currently testing this")
def test_calculates_aces_as_1_where_11_would_bust():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_invalid_cards():
  pass


@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_invalid_for_list_length_greater_than_5():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_bust_for_scores_over_21():
  pass

@pytest.mark.skip(reason="no way of currently testing this")
def test_returns_12_for_ace_ace_king():
  pass

@pytest.mark.skip(reason="logic not yet implemented")
def test_returns_14_for_ace_ace_ace_ace():
    pass