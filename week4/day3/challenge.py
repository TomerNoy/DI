message = input('enter a message below:\n')

shift = int(input(
    'for encryption enter the shift number and for decryption enter a negative shift number:\n'))

cypher_text = ''
for letter in message:
    cypher_text += chr(ord(letter) + shift)

print(f'your message is "{cypher_text}"')
