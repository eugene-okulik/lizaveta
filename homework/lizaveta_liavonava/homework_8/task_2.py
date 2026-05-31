def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

fib_gen = fib_generator()
targets = [5, 200, 1000, 100000]
current_pose = 1

for target in targets:
    steps = target - current_pose

    for _ in range(steps):
        next(fib_gen)
    results = next(fib_gen)
    print(f"{target}th number: {results}")
    current_pose = target
