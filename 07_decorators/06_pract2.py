# Decorator 'Authenticated'

def verify_auth(func):
    def wrapper(*args, **kwargs):
        if args[0]['auth']:
            return func(*args, **kwargs)
    return wrapper


user = {
    'name': 'Sonia',
    'auth': False
}


@verify_auth
def message_friend(user):
    print("Hi, hi!")


message_friend(user)
