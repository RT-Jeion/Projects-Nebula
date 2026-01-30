import random

while True:
    head = 0
    tail = 0

    select = input()
    if select == "q":
        break
    else:
        for i in range(5):
            a = random.randint(0,1)
            if a == 1:
                head = head + 1
            else:
                tail = tail + 1

    print(f"Head: {head}")
    print(f"Tail: {tail}")