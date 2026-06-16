from logic_utils import check_guess


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _message = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _message = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _message = check_guess(40, 50)
    assert outcome == "Too Low"


def test_hint_message_direction_matches_outcome():
    # Regression test for the bug we fixed: the hint text used to contradict
    # the outcome (e.g. "Too High" paired with "Go HIGHER!"). A "Too High"
    # outcome must tell the player to go LOWER, and vice versa.
    high_outcome, high_message = check_guess(60, 50)
    assert high_outcome == "Too High"
    assert "LOWER" in high_message.upper()
    assert "HIGHER" not in high_message.upper()

    low_outcome, low_message = check_guess(40, 50)
    assert low_outcome == "Too Low"
    assert "HIGHER" in low_message.upper()
    assert "LOWER" not in low_message.upper()
