from flitter.message import Message


def test_is_by_checks_if_author_matches_user():
    message = Message(author='charlie', text='hello')

    assert message.is_by('charlie')
    assert not message.is_by('bob')
