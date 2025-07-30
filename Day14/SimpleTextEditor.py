# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of operations
Q = int(input())

# Initialize editor content and stack for undo operations
editor = []
history = []

for _ in range(Q):
    operation = input().split()
    op_type = operation[0]

    if op_type == '1':
        # Append string
        s = operation[1]
        history.append(('1', s))  # Save the operation for undo
        editor.extend(s)

    elif op_type == '2':
        # Delete last k characters
        k = int(operation[1])
        deleted = editor[-k:]
        history.append(('2', deleted))  # Save deleted characters for undo
        editor = editor[:-k]

    elif op_type == '3':
        # Print the kth character
        k = int(operation[1])
        print(editor[k - 1])

    elif op_type == '4':
        # Undo the last append or delete
        if history:
            last_op = history.pop()
            if last_op[0] == '1':
                # Undo append -> remove appended characters
                for _ in last_op[1]:
                    editor.pop()
            elif last_op[0] == '2':
                # Undo delete -> re-add deleted characters
                editor.extend(last_op[1])
