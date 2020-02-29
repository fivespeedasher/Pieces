def hello_world():
    print('hello other world')


def three_hellos():
    for i in range(3):
        hello_world()


if __name__ == '__main__':
    three_hellos()
else:
    hello_world()