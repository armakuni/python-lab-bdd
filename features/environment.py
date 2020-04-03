from flitter.flitter import Flitter
from flitter.in_memory_follow_store import InMemoryFollowStore
from flitter.in_memory_message_store import InMemoryMessageStore


def before_scenario(context, step):
    context.errorMessage = 'Unimplemented step. ' + \
                           'Please provide the implementation.'

    context.app = Flitter(message_store=InMemoryMessageStore(),
                          follow_store=InMemoryFollowStore())
