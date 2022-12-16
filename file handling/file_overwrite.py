file = open('sample4.txt', 'r')
input_content = file.read()
file.close()
print(input_content)

output_content = input_content.replace('Python', 'Java')
print(output_content)

file = open('sample4.txt', 'w')
file.write(output_content)
file.close()
