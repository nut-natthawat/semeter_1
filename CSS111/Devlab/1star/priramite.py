max = 0
count = 0
while True :
  num = input().split()
  count += 1
  if num == 0 :
    break 
a = input()
for i in range(count):
    if num[i] > num[i+1]:
      max = num[i]
print(max)
    
  