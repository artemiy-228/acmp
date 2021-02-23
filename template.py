# read file to variables
with open('input.txt', 'r') as file:
    inp_str = file.read()

# prepare variables
a, b = map(int, inp_str.split())

# solution
c = a + b

# prepare string for output
res = str(c)


# write the solution to file
with open('output.txt', 'w') as file:
    file.write(res)
