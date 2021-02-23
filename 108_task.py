# read file to variables
with open('input.txt', 'r') as file:
    inp_str = file.read()

# prepare variables
# a = map(int, inp_str.split())
a = int(inp_str)
# solution


# prepare string for output
res = str(a)


# write the solution to file
with open('output.txt', 'w') as file:
    file.write(res)
