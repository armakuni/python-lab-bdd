import pytest

from flitter.in_memory_message_store import InMemoryMessageStore
from flitter.message import Message


@pytest.fixture
def message_store():
    return InMemoryMessageStore()


def test_fetch_by_returns_a_list(message_store):
    assert type(message_store.fetch_by('bob')) is list


def test_fetch_by_returns_the_messages_by_a_given_user(message_store):
    message1 = Message(author='bob', text='hi1')
    message2 = Message(author='bob', text='hi2')
    message_store.add(message1)
    message_store.add(message2)

    messages = message_store.fetch_by('bob')

    assert message1 in messages
    assert message2 in messages


def test_fetch_by_does_not_return_message_by_other_users(message_store):
    message = Message(author='bob', text='hi')
    message_store.add(message)

    messages = message_store.fetch_by('alice')

    assert message not in messages


def test_fetch_mentioning_returns_a_list(message_store):
    assert type(message_store.fetch_mentioning('bob')) is list


def test_fetch_mentioning_returns_messages_mentioning_the_user(message_store):
    message = Message(author='bob', text='@alice is great')
    message_store.add(message)

    messages = message_store.fetch_mentioning('alice')

    assert message in messages


def test_fetch_mentioning_does_return_messages_without_mentions(message_store):
    message = Message(author='bob', text='no mentions')
    message_store.add(message)

    messages = message_store.fetch_mentioning('alice')

    assert message not in messages
