
def clean(message):
    message = [x if x.isalpha() or x.isdigit() else ' ' for x in message]
    return ''.join(message)
