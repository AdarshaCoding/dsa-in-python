# if __name__ == "__main__":
#     N = int(input())
#     list = []
#     for i in range(N):
#         opt, *args = input().split()
#         if opt == "append":
#             list.append(int(args[0]))

#         if opt == "remove":
#             list.remove(int(args[0]))

#         if opt == "sort":
#             list.sort()

#         if opt == "reverse":
#             list.sort(reverse=True)

#         if opt == "pop":
#             list.pop()

#         if opt == "print":
#             print(list)

#         if opt == "insert":
#             i, e = int(args[0]), int(args[1])
#             list.insert(i, e)


def append_element(lst, e):
    lst.append(int(e))


def remove_element(lst, e):
    lst.remove(int(e))


def sort_list(lst):
    lst.sort()


def reverse_list(lst):
    lst.reverse()


def pop_element(lst):
    lst.pop()


def insert_element(lst, i, e):
    lst.insert(int(i), int(e))


if __name__ == "__main__":
    N = int(input())
    lst = []

    operations = {
        "append": append_element,
        "remove": remove_element,
        "sort": sort_list,
        "reverse": reverse_list,
        "pop": pop_element,
        "insert": insert_element,
    }

    for _ in range(N):

        args = input().split()

        op = args[0]

        if op == "insert":
            operations[op](lst, args[1], args[2])
        elif op != "print":
            operations[op](lst, *args[1:])

        if op == "print":
            print(lst)
