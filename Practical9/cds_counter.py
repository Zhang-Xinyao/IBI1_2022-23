import re
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
count1=len(re.findall('^ATG.+TAA',seq))
count2=len(re.findall('^ATG.+TAG',seq))
count3=len(re.findall('^ATG.+TGA',seq))
#calculate how coding subsequence in this sequence ends with stop codons respectively
print(count1+count2+count3)
#calculate and output the number of total sequence 
