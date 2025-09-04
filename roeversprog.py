# [[file:README.org::*Udvikling af logik][Udvikling af logik:1]]
# Dette er et modul til oversættelse mellem almindelige sprog og røversprog

vowel_l = "aeiouyæøå"
consonants = "bcdfghjklmnpqrstvwz"

def oversaet_til_roeversprog(inputtekst):
    outputtekst = ""

    

    
    

    for i in inputtekst:
        if i.lower() in vowel_l:
            outputtekst += i
        elif i.lower() in consonants:
            outputtekst += i + "o" + i


    return outputtekst


def oversaet_fra_roeversprog_til_andet_sprog(inputtekst):
    outputtekst = ""
    
    skip = 0

    for i in (inputtekst):
        if skip > 0:
            skip -= 1
            
        else:
            if i.lower() in consonants:
                outputtekst += i
                skip = 2
            elif i.lower() in vowel_l:
                outputtekst += i

    return outputtekst
# Udvikling af logik:1 ends here 

#print(oversaet_til_roeversprog("tAEst"))
#print(oversaet_fra_roeversprog_til_andet_sprog("totAEsostot"))