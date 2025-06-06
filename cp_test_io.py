# Single integer input
n = int(input())

# Multiple integers on the same line
a, b, c = map(int, input().split())

# String input
s = input()

# List input (from a line of space-separated integers)
arr = list(map(int, input().split()))

# List input (multiple lines)
num_lines = int(input())
matrix = []
for _ in range(num_lines):
    row = list(map(int, input().split()))
    matrix.append(row)