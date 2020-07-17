alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encoder (message: str) ->str:
  pass

def shift (message: str, key: int) ->str:
  alpha1 = alphabet[key%26:] + alphabet[:key%26]
  encoded_message = ''
  for letter in message:
    if letter in alphabet:
      position = alphabet.index(letter)
      encoded_message += alpha1[position]
    else:
      encoded_message += letter 
  return encoded_message

def substitution (message: str) -> str:
  pass
