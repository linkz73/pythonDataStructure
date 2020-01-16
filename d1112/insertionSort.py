data = [8,50,6,40,23]

for i in range(len(data)):
    for j in range(i, 0, -1):
        if data[j - 1] > data[j]:
            data[j], data[j - 1] = data[j - 1], data[j]

print(data)
