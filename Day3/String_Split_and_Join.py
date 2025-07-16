

def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    line = split_and_join(line)
    print(line)
# String Split and Join
# This code takes a string input, splits it by spaces, and then joins it with hyphens.