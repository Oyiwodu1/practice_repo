def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return "The price should be a number"
    if not isinstance(discount, (int, float)):
        return "The discount should be a number"
    elif price <= 0:
        return "The price should be greater than 0"
    elif discount <0 or discount > 100:
        return "The discount should be between 0 and 100"
    elif discount == 100:
        return 0
    else:
        return price - (price * discount / 100)
apply_discount(100, 20)
apply_discount(200, 50)
apply_discount(50, 0)
apply_discount(74.5, 20.0)


alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
text = 'hello world'
encrypted_text = text.translate(translation_table)
print(alphabet)
print(shifted_alphabet)
print(encrypted_text)