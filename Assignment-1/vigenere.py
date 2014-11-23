#!/usr/bin/env python3
import binascii

max_key_length = 14
CHARACTERS_LENGTH = 256
FILENAME = 'ciphertext.txt'

with open(FILENAME) as file:
    ciphertext = file.read()

ciphertext = binascii.unhexlify(ciphertext)

# occurences is an array of length 256
# each position is the number of occurences of byte i
def init(occurences):
    occurences.clear()
    for i in range(CHARACTERS_LENGTH):
        occurences.append(0)

def display(occurences):
    for i in range(CHARACTERS_LENGTH):
        print(str(i) + ':' + str(occurences[i]))

def compute_distribution(occurences):
    distribution = 0
    for i in range(len(occurences)):
        distribution += (occurences[i] / CHARACTERS_LENGTH) ** 2
    return distribution

occurences = []
for N in range(1, max_key_length):
    init(occurences)
    for i in range(len(ciphertext)):
        if i % N == 0:
            l = ciphertext[i]
            occurences[l] += 1
    distribution = compute_distribution(occurences) * N
    print('N = ' + str(N) + ': ' + str(distribution))
