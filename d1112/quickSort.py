#QuickSort.py


def qsort(a, low, high):
    if low < high:
        pivot = partition(a, low, high)
        qsort(a, low, pivot - 1)  # pivot 기준으로 양분돼 있기 때문에 두번 재귀
        qsort(a, pivot + 1, high) # pivot 기준으로 양분돼 있기 때문에 두번 재귀


def partition(a, pivot, high):
    i = pivot + 1
    j = high
    while True:
        while i < high and a[i] < a[pivot]:  # 아직 확인하지 않은 데이터가 있고, 피봇보다 큰 경우까지 반복
            i += 1  # Low부터 출발해서 피봇보다 큰 값이 있을 때까지 이동.
        while j > pivot and a[j] > a[pivot]:
            j -= 1

        if i >= j:  # 탐색이 끝났다는 의미
            break

        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    a[pivot], a[j] = a[j], a[pivot]
    return j

a = [52, 58, 42, 22, 14, 68, 11, 40, 33, 35, 80, 40, 90, 23, 64, 30, 22]
print("정렬전 : ")
print(a)
qsort(a, 0, len(a)-1)
print("정렬 후 :")
print(a)