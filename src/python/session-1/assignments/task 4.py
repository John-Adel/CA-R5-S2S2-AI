encoded_message = "##$$$@!yalpstcejorp EPUVT****9887"

#extract
core_message = []
for letter in encoded_message:
    if letter.isalpha() or letter.isspace():
        core_message.append(letter)
core_message = "".join(core_message)
print(f"Core Message: {core_message}")

#reverse
first_word_reversed = core_message.split()[0][::-1]
print(f"First Word: {first_word_reversed}")

#shifting
second_word = core_message.split()[1].replace("E", "A").replace("U", "O")
print(f"Second Word: {second_word}")

#result
output = first_word_reversed + " " + second_word
print(f"Final Decoded Message: {output}")