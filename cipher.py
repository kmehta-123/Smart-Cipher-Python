alpha = 'abcdefghijklmnopqrstuvwxyz'

def encode(text, offset):
    to_return = ''
    for char in text:
        if char not in alpha:
            to_return += char
        else:
            to_return += alpha[(alpha.find(char) + offset) % len(alpha)]
    
    return to_return

def decode(text, offset):
    to_return = ''
    for char in text:
        if char not in alpha:
            to_return += char
        else:
            to_return += alpha[(alpha.find(char) - offset + len(alpha)) % len(alpha)]
    return to_return
