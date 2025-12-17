data = [10,20,20,30,20,60,50,40]
print(data)
#calculating mean
mean = sum(data)/ len(data)
print("Mean:", mean)
#caluclating median
data.sort()
n=len(data)
if n%2==0:
    median = (data[n//2-1] + data[n//2])/2
else:
    median = data[n//2]
    print("Median:", median)
#caluclating mode
mode = max(data, key=data.count)
print("Mode:", mode)
#calculating variance
variance = sum((x - mean) ** 2 for x in data) / len(data)
print("Variance:", variance)
#calculating standard deviation
std_deviation = variance ** 0.5
print("standard deviation:", std_deviation)







