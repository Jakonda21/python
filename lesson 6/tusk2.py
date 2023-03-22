big = int(input())

for i in range(1, big + 1):
    for j in range(1, big + 1):
        print(i * j, end='\t')
    print()