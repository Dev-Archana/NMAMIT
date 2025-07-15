# hackerrank Python Challenge
# Task: Perform various list operations based on user input.


if __name__ == '__main__':
    N = int(input())
    my_list = []

    for _ in range(N):
        val = input().strip().split()
        cmd = val[0]

        if cmd == 'insert':
            index = int(val[1])
            value = int(val[2])
            my_list.insert(index, value)
        elif cmd == 'print':
            print(my_list)
        elif cmd == 'remove':
            value = int(val[1])
            my_list.remove(value)
        elif cmd == 'append':
            value = int(val[1])
            my_list.append(value)
        elif cmd == 'sort':
            my_list.sort()
        elif cmd == 'pop':
            my_list.pop()
        elif cmd == 'reverse':
            my_list.reverse()
