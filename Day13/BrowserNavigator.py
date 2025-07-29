# Two stacks for back and forward navigation
back_stack = []
forward_stack = []
current_page = None

def visit(page):
    global current_page
    if current_page is not None:
        back_stack.append(current_page)
    current_page = page
    forward_stack.clear()  # Clear forward history on new visit
    print(f"Visited: {current_page}")

def go_back():
    global current_page
    if not back_stack:
        print("No pages in back history")
        return
    forward_stack.append(current_page)
    current_page = back_stack.pop()
    print(f"Back to: {current_page}")

def go_forward():
    global current_page
    if not forward_stack:
        print("No pages in forward history")
        return
    back_stack.append(current_page)
    current_page = forward_stack.pop()
    print(f"Forward to: {current_page}")

def show_status():
    print("\n--- Browser Status ---")
    print(f"Current Page: {current_page}")
    print(f"Back Stack: {back_stack}")
    print(f"Forward Stack: {forward_stack}")
    print("----------------------\n")

# Simulating browser activity
visit("google.com")
visit("github.com")
visit("stackoverflow.com")
show_status()

go_back()
show_status()

go_back()
show_status()

go_forward()
show_status()

visit("chat.openai.com")
show_status()
