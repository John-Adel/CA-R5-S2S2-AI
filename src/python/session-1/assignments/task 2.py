encoded_message = "###!!@mocleW EPGTQ!!!6789"

# Core Extraction
core_message = []
for letter in encoded_message:
    if letter.isalpha() or letter.isspace():
        core_message.append(letter)
core_message = "".join(core_message)
print(f"Core Message: {core_message}\n")

# first word reversed
first_word_reversed = core_message.split()[0][::-1] + core_message.split()[1][0].lower()
print(f"Reversed First Word: {first_word_reversed}\n")

# Final answer
second_word = core_message.split()[1][1:]
print(f"Final Decoded Message: {first_word_reversed} {second_word}")
