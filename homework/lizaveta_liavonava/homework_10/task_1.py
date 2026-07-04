def finish_me(func):

    def wrapper(*args, **kwargs):
        func(*args)
        print('finished')

    return wrapper


@finish_me
def example(text):
    print(text)


example('print me')
