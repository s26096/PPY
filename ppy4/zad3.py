def caesar_cipher(data, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    data = str.lower(data)
    output = ""
    for d in data:
        if d not in alphabet:
            output += d
            continue
        for i, letter in enumerate(alphabet):
            if letter == d:
                offset = (i+key) % 26
        d = alphabet[offset]
        output += d
    return output


text = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
print(caesar_cipher(text, 5))
