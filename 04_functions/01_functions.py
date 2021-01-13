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


def suma(num1, num2) -> float:
    return num1 + num2


result = suma(2, 3)

print(f"The answer is: {result}")

# *args and **kwargs


def super_function(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


print(super_function(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, num1=5, num2=10))


# Example to CarbonApp and <super> docstring. :D

def largest_even(number_list) -> float:
    """
    This function receives a list of numbers 
    and return the largest even value.

    Parameters
    ----------
    number_list : list
        list of numbers

    Returns 
    ----------
    float
        the largest even value
    """

    evens = []
    for i in number_list:
        if i % 2 == 0 and i not in evens:
            evens.append(i)
    return max(evens)


print(largest_even([10, 2, 3, 4, 8, 11]))
