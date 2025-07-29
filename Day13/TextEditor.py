# Redo And Undo Operation in text editors :
undo_stack=[] 
redo_stack=[] 
current_state=None 

def perform_action(action):
    global current_state 
    if current_state is not None: 
        undo_stack.append(current_state)
    current_state=action 
    print(f"performed :{current_state}")

# redo operation 
def redo():
    global current_state 
    if not redo_stack:
        print("Nothing to redo.")
        return 
    undo_stack.append(current_state)
    current_state=redo_stack.pop() 
    print(f"Redo :{current_state}")
    
def undo():
    global current_state 
    if not undo_stack: 
        print("Nothing To Undo")
        return 
    redo_stack.append(current_state) 
    current_state=undo_stack.pop() 
    print(f"Undo:{current_state}") 
perform_action("Type 'Hello'")
perform_action("TYpe'world'") 
undo()
redo()