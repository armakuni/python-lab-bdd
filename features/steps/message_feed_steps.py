from behave import given, when, then


@given('{author} has posted a message "{message}"')
def post_message(context, author, message):
    context.app.post(author=author, message=message)


@given('{follower} follows {followee}')
def follow(context, follower, followee):
    context.app.follow(follower=follower, followee=followee)


@given('{follower} is not following {followee}')
def do_not_follow(context, follower, followee):
    pass  # Do nothing


@when('{user} views their feed')
def view_feed(context, user):
    context.feed = context.app.get_feed_for(user)


@then('they can see the message "{message}" by {author}')
def assert_can_see_message(context, message, author):
    feed = context.feed
    expected = dict(author=author, message=message)

    assert expected in feed, f'{expected} should be in {feed}'


@then('they cannot see the message "{message}" by {author}')
def assert_cannot_see_message(context, message, author):
    feed = context.feed
    expected = dict(author=author, message=message)

    assert expected not in feed, f'{expected} should not be in {feed}'
