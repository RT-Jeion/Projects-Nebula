import random

final = []
gap = []
for a in range(1,5): # if the range goes upto 7 then it takes a long time to compute...    rang = 10**a
    print(f"\n\nTrail no.{a}, Result of {rang} toss")
    head_1= 0
    tail_1 = 0
    for b in range(5):
        head_counter = 0
        tail_counter = 0
        total = 0
        for i in range(rang):
            a = random.randint(0,1)
            if a == 1:
                head_counter += 1
                total += 1
            else:
                tail_counter += 1
                total += 1
        head_1 = head_1 + head_counter
        tail_1 = tail_1 + tail_counter


        head_percent = head_counter/total * 100
        tail_percent = tail_counter/total * 100
        print(f"\nResult of Trail no.{b+1} for {total} toss..")
        print(f"Total: {total}, Head: {head_counter}, Tail: {tail_counter}")
        print("Head percent: " + str(head_percent) + "%")
        print("Tail percent: " + str(tail_percent) + "%")

    total = rang * 5
    ava_head = head_1 / total * 100
    ava_tail = tail_1 / total * 100
    gap = abs(ava_head - ava_tail)
    final.append((f"Head: {ava_head:.3f}", f"Tail: {ava_tail:.3f}", f"Gap: {gap:.3f}"))

    print("\nAverage head: " + str(ava_head))
    print("Average tail: " + str(ava_tail))

print("\n")
trail = 0
for i in final:
    print(f"Result of Trail no.{trail+1}")
    print(i)
   # print("Gap: ",j)
    trail += 1