import re
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
seq_count=seq.split('ATG')[1]
count1=len(re.findall(r'TAA',seq_count))
count2=len(re.findall(r'TAG',seq_count))
count3=len(re.findall(r'TGA',seq_count))  
#calculate how coding subsequence in this sequence ends with stop codons respectively
print(count1+count2+count3)
#calculate and output the number of total sequence  
