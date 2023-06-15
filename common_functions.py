def clean_input(input):
    input = input.lower()
    if input[0] == " ":
        input = input[1:]
    if input[len(input) -1] == " ":
        input = input[:len(input)-2]
    return input