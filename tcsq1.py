#input = aaabbbbccceeeee
#output = a3b4c3e5

input_string = "aaabbbbccceeeee"
output_string = ""
count = 1
for i in range(len(input_string)-1):
    if input_string[i] == input_string[i+1]:
        count += 1
    else:
        output_string += input_string[i] + str(count)
        count = 1
output_string += input_string[-1] + str(count)
print(output_string)