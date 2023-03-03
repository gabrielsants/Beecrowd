data = int(input())

hour = data // 3600
minutes = (data % 3600) // 60
seconds = (data % 3600) % 60

print("%d:%d:%d" %(hour, minutes, seconds))