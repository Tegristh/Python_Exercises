with open("Input/Letters/starting_letter.txt", mode="r") as start:
    starting_letter = start.read()


with open("Input/Names/invited_names.txt", mode="r") as names:
    names_list = names.readlines()

format_names = []
for name in names_list:
    if name.endswith('\n'):
        new_name = name[:-1]
        format_names.append(new_name)
    else:
        format_names.append(name)

for name in format_names:
    new_letter = starting_letter.replace('[name]', name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as output:
        output.write(new_letter)


