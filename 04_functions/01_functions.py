""" 
This is a functions
"""


def is_man() -> None:
    """
    def is_man() -> None
    """
    print("is a man.")


is_man()


def is_even(number) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


for i in range(10):
    print(is_even(i))


def new_user(name, last_name, age, /, games, *, nickname):
    print(f"""
    name: {name}
    last_name: {last_name}
    age: {age}
    games: {games}
    nickname: {nickname}
    """)


new_user('frank', 'muniz', 38, games=['javascript',
                                      'python'], nickname='janobourian')

new_user('andrei', 'robles', 31, games=['javascript',
                                        'python'], nickname='janobourian')
