# Write a program to move 2 disks to source to destination with given conditions:
# 1.only one disk we can move at a time 
# 2.we should not place larger disk above the smaller one 
# take 3 disks and 3 pins to complete the task

def towerOfHanoi(n, a, b, c):
    if n == 1:
        print(f"Move disk 1 from {a} to {c}")
        return
    towerOfHanoi(n - 1, a, c, b)
    print(f"Move disk {n} from {a} to {c}")
    
    towerOfHanoi(n - 1, b, a, c)

n = 3
towerOfHanoi(n, 'A', 'B', 'C')
