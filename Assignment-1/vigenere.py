occurences = {}

ciphered_text = "This is a super text that I should take now"

for N in range(1,14):
    for i in range(0, len(ciphered_text)):
        if N == 0 or i % N == 0:
            l = ciphered_text[i]
            if occurences.get(l):
                occurences[l] += 1
            else:
                occurences[l] = 1
    distribution = 0
    for l in occurences:
        distribution += (occurences[l] * occurences[l]) / (26*26)
    print('N = ' + str(N) + ': ' + str(distribution))
    occurences = {}
