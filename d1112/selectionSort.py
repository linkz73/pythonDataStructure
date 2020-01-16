# 숙제 : 완성하시오

data = [35,3,8,50,6,40,23,30]
for i in range(len(data)):
    for j in range(0,i):
        if data[i] < data[j]:
            data[i], data[j] = data[j], data[i]

print(data)