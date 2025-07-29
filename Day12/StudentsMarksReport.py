def read_marks_file(filename="marks.txt"):
    try:
        with open(filename, 'r') as file:
            print("Student Marks Report:\n")
            for line in file:
                
                line = line.strip()
                if line: 
                    try:
                        name, mark = line.split(',')
                        print(f"Name: {name.strip()}, Marks: {mark.strip()}")
                    except ValueError:
                        print(f"Skipping invalid line format: {line}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        print("Please check the file path or create the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Call the function
read_marks_file()
