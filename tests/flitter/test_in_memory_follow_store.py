from flitter.in_memory_follow_store import InMemoryFollowStore


def test_get_followees_for_returns_a_list():
    follow_store = InMemoryFollowStore()

    assert type(follow_store.get_followees_for('alice')) == list


def test_get_followess_for_returns_the_followees_for_a_user():
    follow_store = InMemoryFollowStore()

    follow_store.add(follower='alice', followee='bob')
    follow_store.add(follower='alice', followee='charlie')
    follow_store.add(follower='bob', followee='alice')

    alices_followees = follow_store.get_followees_for('alice')

    assert 'bob' in alices_followees
    assert 'charlie' in alices_followees
    assert 'alice' not in alices_followees
