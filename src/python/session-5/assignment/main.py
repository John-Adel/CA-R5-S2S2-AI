import EmailValidationDecoder as ED
from NumberGames import NumberGames
number = NumberGames()
print(number.isPrime(100))
print(number.dec_to_bin(100))
number.euclid_euler(100)
number.multi_table(100)
print(number.prime_factor(100))
number.twin_prime()

email = ED.EmailValidation("Amit_ml@gmail.edu")
print(email.__str__())
print(email.is_valid())

encoded = ED.Decoder("###!!@EmocleW EPGTQ!!!6789")
print(encoded.decode())

