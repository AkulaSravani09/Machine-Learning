data = [10,20,20,30,20,60,50,40]
print(data)
#calculating mean
mean = sum(data)/ len(data)
print("Mean:", mean)
#calculating median
data.sort()
n=len(data)
if n%2==0:
    median = (data[n//2-1] + data[n//2])/2
else:
    median = data[n//2]
    print("Median:", median)
#calculating mode
mode = max(data, key=data.count)
print("Mode:", mode)
#calculating variance
variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance:", variance)
#calculating standard deviation
std_deviation = variance ** 0.5
print("standard deviation:", std_deviation)
#calculating median using bubble sort technique
arr = [22, 11, 44, 24, 56, 77, 89, 88]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

sorted_arr = bubble_sort(arr.copy())
n = len(sorted_arr)

if n % 2 == 0:
    median_bubble = (sorted_arr[n//2 - 1] + sorted_arr[n//2]) / 2
else:
    median_bubble = sorted_arr[n//2]

print("Median using Bubble Sort:", median_bubble)







