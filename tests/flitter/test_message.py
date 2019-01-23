from flitter.message import Message


def test_is_by_checks_if_author_matches_user():
    message = Message(author='charlie', text='hello')

    assert message.is_by('charlie') is True
    assert message.is_by('bob') is False


def test_mentions_returns_false_if_a_user_is_not_mentioned():
    message = Message(author='alice', text='no mentions')

    assert message.mentions('bob') is False


def test_mentions_returns_true_if_the_user_is_mentioned():
    message = Message(author='alice', text='hello @bob')

    assert message.mentions('bob') is True


def test_mentions_returns_false_if_the_mention_does_not_start_with_at_symbol():
    message = Message(author='alice', text='hello bob')

    assert message.mentions('bob') is False


def test_mentions_returns_false_if_the_user_is_a_substring_of_a_mention():
    message = Message(author='alice', text='where is @charliebrown?')

    assert message.mentions('charlie') is False


def test_mentions_ignores_case():
    message = Message(author='alice', text='hi @ChArLiE')

    assert message.mentions('CHARlie') is True
