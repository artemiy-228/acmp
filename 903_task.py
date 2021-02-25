# read file to variables
with open('input.txt', 'r') as file:
    inp_str = file.read()

# prepare variables
a = (int, inp_str.split())

# solution
b = int(a + 1)

# prepare string for output
res = str(b)


# write the solution to file
with open('output.txt', 'w') as file:
    file.write(res)