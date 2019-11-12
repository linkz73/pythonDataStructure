data = [8,50,6,40,23]
for i in range(len(data)):
    for j in range(0,i):
        if data[i] < data[j]:
            data[j] = data[j+1]

print(data)