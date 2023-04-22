# pseudocode

# make user enter their string
input_str = input("Enter your string: ")
output_str = ""

# check every character
for i in range(len(input_str)):

    # if *, change a
    if input_str[i] == "*":
        output_str += "a"
    # else, if &, change e
    elif input_str[i] == "&":
        output_str +="e"
    # else, if #, change i
    elif input_str[i] == "#":
        output_str +="i"
    # else, if +, change o
    elif input_str[i] == "+":
        output_str +="o"
    # else, if !, change u
    elif input_str[i] == "!":
        output_str +="u"
    else:
        output_str += input_str[i]

# print output
print(output_str)