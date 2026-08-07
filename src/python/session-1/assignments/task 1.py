# User Input
email = input("Enter your Email\n>>> ")

# Input Validation
if (
    email.count("@") == 1
    and email.count(".") >= 1
    and "." not in email[: email.index("@")]
):
    print("Valid Email\n")
    # Username extraction
    username = email[: email.index("@")]
    print(f"Username: {username}\n")

    # Domain Extraction
    domain = email[email.index("@") + 1 : email[::-1].find(".") * -1 - 1]
    print(f"Domain: {domain}\n")

    #Domain Ending
    if email.endswith(".com"):
        print("Commerial Domain\n")
    elif email.endswith(".edu"):
        print("Educaitonal Domain\n")
    else:
        print("Other Domain\n")
else:
    print("Invalid Email\n")

