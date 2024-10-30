# the mean of 40 numbers is 38. Later on it was detected the number 56 was missread as 36. Find the correct mean of given numbers.

n = 40 
mean = 38
missread = 36
correct = 56

# sum = mean * n 
Givensum = mean * n 

correctsum = Givensum - missread + correct

correctmean = correctsum / n 

print(f" The correct mean of the given numbers is { correctmean}")


