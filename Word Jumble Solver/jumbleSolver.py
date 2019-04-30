#   jumbleSolver.py
#   Colin Kee
#   2019-03-10


from nltk.corpus import words

# Premutation function
def permutations(s):
    if len(s) < 2:
        yield s
    else: 
        for pos in range (len(s)):
            s1 = s[pos]
            s2 = s[:pos] + s[pos+1:]
            for prm in permutations(s2):
                yield s1 + prm

# Loop to get and validate input. Validates length, converts input to lower case and confirms input to be alpha only.               
def getInput():
    valid = False
    while not valid:
        s = input("Enter word jumble (type q to exit): ")
        s = s.lower()
        if len(s) < 1:
            print("Error: Please enter at least one letter")
        elif not s.isalpha():
            print("Error: Please enter letters only")
        else:
            valid = True
            return s

def jumbleSolver():
    jumble = getInput()
    while jumble != "q":
        wordMatches = []
        count = 0
        for perm in permutations(jumble):
            if perm.lower() in w:
                if perm not in wordMatches:
                    wordMatches.append(perm)
                    count += 1
                    print(perm)
        if count is 1:            
            print("{0} word match found for jumble \"{1}\"\n".format(count, jumble))
        else:
            print("{0} word matches found for jumble \"{1}\"\n".format(count, jumble))
        jumble = getInput()

# Main 

w = set(wrd.lower().strip() for wrd in words.words())
jumbleSolver()
