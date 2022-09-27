def hello_world():
    print("Hello, world!")


def get_sum(l: list):
    return sum(l)


hello_world()
print(get_sum([int(x) for x in input().split()]))
