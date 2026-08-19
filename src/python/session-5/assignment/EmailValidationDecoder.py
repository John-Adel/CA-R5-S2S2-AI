'''  This module has a primitive email validation class and a primitive decoder class

'''


class EmailValidation():
    '''  This is a primitive email validation class, it uses an if condition with special email validation crtiria




    Attributes:
        email: The email that will be used by the class's function
    
    '''
    def __init__(self, email: str):
        self.email = email
    def is_valid(self) -> bool:
        '''  A boolean function that checks if the email is correct or not
        
        
        
        
        Returns:
            True if the email checks the critria, false otherwise
        '''
        return True if (self.email.count("@") == 1 and self.email.count(".") >= 1 and "." not in self.email[: self.email.index("@")]) else False
    def __str__(self):
        if self.email.endswith(".com"):
            placeholder = "Commerial Domain\n"
        elif self.email.endswith(".edu"):
            placeholder = "Educaitonal Domain\n"
        else:
            placeholder = "Other Domain\n"
        
        username = self.email[: self.email.index("@")]
        domain = self.email[self.email.index("@") + 1 : self.email[::-1].find(".") * -1 - 1]
        return f"Username: {username}\nDomain: {domain}\nType: {placeholder}\n"
            
    


class Decoder():
    '''  This is a primitive decoder that decodes a string with a specific type of encoded format


    

    Attributes:
        string: This is the encoded message
    '''
    def __init__(self, string: str):
        self.string = string
    def decode(self) -> str:
        '''  This is the only method in the class, it takes the string from the constructor


        

        Returns:
            The decoded message
        '''
        extract = []
        for letter in self.string:
            if letter.isalpha():
                extract.append(letter)
            elif letter.isspace():
                break
        reversed_word = "".join(extract)
        decoded_word = reversed_word[::-1].capitalize()
        return f"{decoded_word}"
