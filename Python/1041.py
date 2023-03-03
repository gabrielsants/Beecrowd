# __Author__ Gabriel Santos - Federal University of Goiás
points = input().split()
px = float(points[0])
py = float(points[1])

if px == 0 and py == 0:
    print('Origem')
elif x == 0 and y != 0:
    print('Eixo Y')
elif x !=0 and y == 0:
    print('Eixo X')
elif x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0:
    print('Q4')