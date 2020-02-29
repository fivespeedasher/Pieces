scale = eval(input('setting rows and lines'))
ls = [[]for i in range(scale)]
for row in range (scale):
    for word in range (scale):
        ls[row].append(eval(input('element')))
print(ls)
mul = 1
for i in range(scale):
    mul *= ls[i][i]
print(mul)


# matrix = [[0 for i in range(3)]for i in range(3)]
# matrix[0][1]=1
# print(matrix)
#
# ls = [[]for i in range(3)]
# ls[0].append(1)
# ls.append(3)
# print(ls)

# a = []
# sum = 0.0
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[i].append(float(raw_input("input num:\n")))