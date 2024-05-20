with open("file1.txt","r") as f1:
    l1 = [num for num in f1.read().splitlines()]

with open("file2.txt","r") as f2:
    l2 = [num for num in f2.read().splitlines()]

result = [num for num in l1 if num not in l2]

print(result)
