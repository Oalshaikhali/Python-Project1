int_input = 76542

int_input_list = []

for x in str(int_input):
    int_input_list.append(int(x))



int_array = []

for item in int_input_list:
    int_array.append(item)

int_array.sort()

str_array = []
for item in int_array:
    str_array.append(str(item))



print("".join(str_array))
