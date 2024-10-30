import random

print("Welcome to the Dice Roll Tracker")

n = int(input("How many roll?: "))

noofrollsfor1 = 0 
noofrollsfor2 = 0 
noofrollsfor3 = 0 
noofrollsfor4 = 0 
noofrollsfor5 = 0 
noofrollsfor6 = 0 

for i in range(n):
    no = random.randint(1,6)
    if no == 1:
        noofrollsfor1 += 1
    elif no == 2:
        noofrollsfor2 += 1
    elif no == 3:
        noofrollsfor3 += 1
    elif no == 4:
        noofrollsfor4 += 1
    elif no == 5:
        noofrollsfor5 += 1
    elif no == 6:
        noofrollsfor1 += 1

perfor1 = (noofrollsfor1/n)*100
perfor2 = (noofrollsfor2/n)*100
perfor3 = (noofrollsfor3/n)*100
perfor4 = (noofrollsfor4/n)*100
perfor5 = (noofrollsfor5/n)*100
perfor6 = (noofrollsfor6/n)*100

print(f"1 was rolled:{noofrollsfor1} times, or {perfor1}%")
print(f"2 was rolled:{noofrollsfor2} times, or {perfor2}%")
print(f"3 was rolled:{noofrollsfor3} times, or {perfor3}%")
print(f"4 was rolled:{noofrollsfor4} times, or {perfor4}%")
print(f"5 was rolled:{noofrollsfor5} times, or {perfor5}%")
print(f"6 was rolled:{noofrollsfor6} times, or {perfor6}%")



