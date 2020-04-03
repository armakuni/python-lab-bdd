def before_scenario(context, step):
    context.errorMessage = 'Unimplemented step. ' + \
                           'Please provide the implementation.'
