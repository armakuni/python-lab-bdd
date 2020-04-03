class InMemoryFollowStore:
    def __init__(self):
        self.followees = []

    def add(self, follower, followee):
        self.followees.append(dict(follower=follower, followee=followee))

    def get_followees_for(self, user):
        return [follow['followee']
                for follow in self.followees
                if follow['follower'] == user]
