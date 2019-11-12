# 제어된 버블소트
data = [8,50,2,3,6,40,23,45]

cnt = 0 #28
for i in range(len(data) - 1):  # 0 ~ 4
    sw = 0
    for j in range(len(data) - 1 - i):
        cnt += 1
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            sw = 1
            # t = data[j]
            # data[j] = data[j+1]
            # data[j+1] = t
    if sw == 0: break
print(data, "roof count : ", cnt)