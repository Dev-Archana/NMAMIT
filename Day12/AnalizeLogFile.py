def analyze_log_file(filename="logs.txt"):
    error_count = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                try:

                    if "ERROR" in line:
                        error_count += 1
                except UnicodeDecodeError:
                    print(f"Skipping unreadable line {line_number} due to decoding error.")

        print(f"\nTotal lines containing 'ERROR': {error_count}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found. Please check the file path.")
    except UnicodeDecodeError:
        print("Error: File contains unreadable characters. Try opening with a different encoding.")
    except IOError as e:
        print(f"IOError occurred: {e}")


analyze_log_file()
