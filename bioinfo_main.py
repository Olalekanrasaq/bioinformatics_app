from bioinformatics import *
import streamlit as st

st.title('Bioinformatics App')
st.markdown('This app contains bioinformatics algorithms that can execute molecular biology tasks such as:')
st.markdown(
    """
    * Counting Nucleotides
    * Transcription
    * Translation
    * Finding Gene pattern
    * Mutation
    * Sequence Alignment; and more
    """
)
st.markdown('#### Check the sidebar to select a function.')
st.sidebar.markdown('## Bioinformatics Functions')
selection = st.sidebar.selectbox('Pick one', ['Functions', 'Counting DNA Nucleotides', 'Validating Sequence', 'GC Content',
'DNA Complement', 'Transcription (DNA-RNA)', 'Translation(from RNA)', 'Translation(from DNA)', 'Hamming Distance',
'DNA Pattern Matching', 'Sequence Alignment'])

if selection == 'Counting DNA Nucleotides':
    text = st.subheader('Count Nucleotides')
    seq = st.text_input('Paste your Sequence here')
    if seq:
        counts = CountingNuc(seq)
        st.write(f'C = {counts[0]}; A = {counts[1]}; G = {counts[2]}; T = {counts[3]};  \nTotal Counts = {counts[4]}')
elif selection == 'Validating Sequence':
    text = st.subheader('Validate Sequence')
    seq = st.text_input('Paste your Sequence here')
    if seq:
        message = ValidateSeq(seq)
        st.write(f'{message}')
elif selection == 'GC Content':
    text = st.subheader('GC Content')
    seq = st.text_input('Paste your Sequence here')
    if seq:
        per_CG = GC_content(seq)
        st.write(f'Percentage GC = {per_CG:.2f}')
elif selection == 'DNA Complement':
    text = st.subheader('DNA Complement')
    direction = st.radio('Pick a direction', ['5 to 3 strand', '3 to 5 strand'])
    seq = st.text_input('Paste your Sequence here')
    if seq:
        complement = Complement(seq)
        if direction == '5 to 3 strand':
            st.write(f"DNA complement: 3' {complement} 5'")
        else:
            st.write(f"DNA complement: 5' {complement} 3'")
elif selection == 'Transcription (DNA-RNA)':
    text = st.subheader('Transcribe DNA to RNA')
    direction = st.radio('Pick a direction', ['5 to 3 strand', '3 to 5 strand'])
    seq = st.text_input('Paste your Sequence here')
    if seq:
        if direction == '3 to 5 strand':
            RNA = transcription(seq)
            st.write(f'RNA Sequence: {RNA}')
        else:
            RNA = Complement(seq)
            RNA = transcription(RNA)
            st.write(f'RNA Sequence: {RNA}')
elif selection == 'Translation(from RNA)':
    text = st.subheader('Translate RNA to Protein')
    seq = st.text_input('Paste your Sequence here')
    if seq:
        protein = translation(seq)
        st.write(f'Protein: {protein}')
elif selection == 'Translation(from DNA)':
    text = st.subheader('Translate DNA to Protein')
    seq = st.text_input('Paste your Sequence here')
    if seq:
        protein = translationDNA(seq)
        st.write(f'Protein: {protein}')
elif selection == 'Hamming Distance':
    text = st.subheader('Determine Hamming Distance')
    caption = st.caption('Hamming distance is the number of bases by which two sequences differ. It determines level of mutation between two gene sequences.')
    seq1 = st.text_input('Paste first sequence here')
    seq2 = st.text_input('Paste second sequence here')
    if seq2:
        hd = HammingDist(seq1, seq2)
        st.write(f'Hamming Distance =  {hd}')
elif selection == 'DNA Pattern Matching':
    text = st.subheader('DNA Pattern Matching')
    caption = st.caption('To find the locations of particular DNA subsequences in a DNA sequence')
    DNA_seq = st.text_input('Paste DNA sequence here')
    DNA_subseq = st.text_input('Paste the pattern to find here')
    if DNA_subseq:
        position = PatternMatching(DNA_subseq, DNA_seq)
        st.write(f'Number of times pattern found:  {position[0]}  \nPositions:   {position[1]}')
elif selection == 'Sequence Alignment':
    text = st.subheader('Pairwise Sequence Alignment')
    caption = st.caption('Compare two DNA sequences of the same length')
    seq1 = st.text_input('Paste first DNA sequence here')
    seq2 = st.text_input('Paste second DNA sequence here')
    if seq2:
        align = PairwiseSeqAlign(seq1, seq2)
        st.write(f'{align[0]}  \n{align[2]}  \n{align[1]}')