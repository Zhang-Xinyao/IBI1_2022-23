#define a calculator that could calculate the protein-coding capability of a sequence
def calculator(sequence):
    #change all the letters in the string into upper case
    sequence=sequence.upper()
    #calculate the distance between the start codon and end codon
    distance=sequence.find('TGA')-sequence.find('ATG')-3
    print(distance/len(sequence))
    #judge the sequence is a protein-coding sequence or non-coding sequence or an unclear sequence
    if distance/len(sequence)>0.5:
         print('protein-coding')
    elif distance/len(sequence)<0.1:
         print('non-coding')
    else:
         print('unclear')

#the example    
sequence="ATGTTTagaTCCCactacggactACGTgA"
calculator(sequence)
