import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")


phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


while True:
    try:
        entry = input("Enter a word: ").upper()
        result = [phonetic_dict[letter] for letter in entry]
        print(result)
        break
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
