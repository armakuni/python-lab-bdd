from flitter.message import Message


class Flitter:
    def __init__(self, message_store, follow_store):
        self.message_store = message_store
        self.follow_store = follow_store

    def post(self, author, message):
        """
        Post a message

        :param author: The user name of the author
        :type author: string
        :param message: The message to be posted
        :type message: string
        :return: nothing
        :rtype: void
        """

        self.message_store.add(Message(author=author, text=message))

    def get_feed_for(self, user):
        """
        Get messages in a users feed.

        :param user: The user to get messages for
        :type user: string
        :return: All the messages as a list of dicts with author and message
        :rtype: list(dict(author=string, message=string))
        """

        feed = self._fetch_messages_by_user(user)

        feed += self._fetch_messages_by_followees_of_user(user)

        return [dict(author=msg.author, message=msg.text) for msg in feed]

    def follow(self, follower, followee):
        """
        Make one user follow another
        :param follower: The user who is following
        :type follower: string
        :param followee:  The user being followed
        :type followee: string
        :return: nothing
        :rtype: void
        """

        self.follow_store.add(follower=follower, followee=followee)

    def _fetch_messages_by_user(self, user):
        return self.message_store.fetch_by(user)

    def _fetch_messages_by_followees_of_user(self, user):
        messages = []

        for followee in self.follow_store.get_followees_for(user):
            messages += self._fetch_messages_by_user(followee)

        return messages
