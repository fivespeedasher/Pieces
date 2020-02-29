original_list = ['1', '9', '10', '5', '6', '7', '2', '3', '5', '4', '7']#input("Enter a set of Numbers separated by Spaces").split(" ")
for i in range(len(original_list)):
    if i >= len(original_list)/2:
        break
    original_list[i],original_list[-(i+1)] = original_list[-(i+1)],original_list[i]
print(original_list)