lst = [i for i in range(1, int(input()) + 1)]
k = int(input())
last = 0

def circle_run(lenght):
    for i in range(0, lenght, k):
        global last
        print(lst, last)
        if last + k - 1 < lenght:
            del lst[last + k - 1]
            last += k
        else:
            while len(lst) != 1:
                lenght_1 = len(lst)
                circle_run(lenght_1)

    print(lst)


#while len(lst) != 1:
circle_run(len(lst))