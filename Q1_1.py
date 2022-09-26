array = [12, 75, 150, 180, 145, 525, 50]


for item in array:
    if item > 150:
        if item > 500:
            break
        continue
    if item % 5 == 0:
        print(item)

# for item in array:
#     if item > 500:
#         break
#     elif item > 150:
#         continue
#     elif item % 5 == 0:
#         print(item)
