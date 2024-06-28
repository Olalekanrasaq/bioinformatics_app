def CountingNuc(sequence):
    C, G, A, T = 0, 0, 0, 0
    for nuc in sequence:
        if nuc == 'C':
            C += 1
        elif nuc == 'G':
            G += 1
        elif nuc == 'T':
            T += 1  
        elif nuc == 'A':
            A += 1
    sum_of_nuc = C + G + T + A
    return C, A, G, T, sum_of_nuc

def ValidateSeq(sequence):
    nucleotides = ['A', 'C', 'G', 'T']
    invalid_nuc = ''
    for nuc in sequence:
        if nuc not in nucleotides:
            invalid_nuc += nuc + ','
    if invalid_nuc:
        message = 'Sequence is not valid.  \nInvalid nucleotides: ' + invalid_nuc
    else:
        message = 'Sequence is valid'
    return message

def GC_content(sequence):
    result = CountingNuc(sequence)
    C, A, G, T, sum_of_nuc = result[0], result[1], result[2], result[3], result[4]
    GC = G + C
    perc_GC = (GC / sum_of_nuc) * 100
    return perc_GC

def Complement(sequence):
    basepairs = {'A' : 'T', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
    complement = ''
    for char in sequence:
        complement += basepairs.get(char)
    return complement

def transcription(sequence):
    basepairs = {'A' : 'U', 'C' : 'G', 'G' : 'C', 'T' : 'A'}
    RNA = ''
    for char in sequence:
        RNA += basepairs.get(char)
    return RNA

def translation(RNA_seq):
    DNA_codon={
        'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
        'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu','AUU':'Ile',
        'AUC':'Ile','AUA':'Ile','AUG':'Met','GUU':'Val','GUC':'Val',
        'GUA':'Val','GUG':'Val','UCU':'Ser','UCC':'Ser','UCA':'Ser',
        'UCG':'Ser','CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
        'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr','GCU':'Ala',
        'GCC':'Ala','GCA':'Ala','GCG':'Ala','UAU':'Tyr','UAC':'Tyr',
        'UAA':'STOP','UAG':'STOP','CAU':'His','CAC':'His','CAA':'Gln',
        'CAG':'Gln','AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
        'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu','UGU':'Cys',
        'UGC':'Cys','UGA':'STOP','UGG':'Trp','CGU':'Arg','CGC':'Arg',
        'CGA':'Arg','CGG':'Arg','AGU':'Ser','AGC':'Ser','AGA':'Arg',
        'AGG':'Arg','GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly'}
    protein = ''
    for i in range(0, len(RNA_seq), 3):
        codon = RNA_seq[i:i+3]
        try:
            amino_acid = DNA_codon.get(codon)
            protein += amino_acid + '-'
        except TypeError:
            pass
    return protein

def translationDNA(DNA_seq):
    RNA_seq = transcription(DNA_seq)
    protein = translation(RNA_seq)
    return protein

def HammingDist(seq1, seq2):
    d = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            d += 1
    return d

def PatternMatching(Pattern, Genome):
    positions = []
    for i in range(len(Genome)- len(Pattern) + 1):
        if Genome[i:i+len(Pattern)] == Pattern:
            pos = i + 1
            positions.append(pos)
    sum_pos = len(positions)
    return sum_pos, positions

def PairwiseSeqAlign(seq1, seq2):
    char_list = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            char = i
            char_list.append(char)
    align = '|'*len(seq1)
    temp = list(align)
    for idx in char_list:
        temp[idx] = '-'
    res = ''.join(temp)
    return seq1, seq2, res