from Bio import SeqIO, Align

"""
RNA HIV1 VS SIV ANALYSIS
"""

hiv1_fna_file = "data/hiv1.fna"
hiv1_fasta_records = SeqIO.parse(hiv1_fna_file, 'fasta')

hiv1_fasta = {
    'id': None,
    'name': None,
    'description': None,
    'sequence': None
}
for record in hiv1_fasta_records:
    hiv1_fasta['id'] = record.id
    hiv1_fasta['name'] = record.name
    hiv1_fasta['description'] = record.description
    hiv1_fasta['sequence'] = str(record.seq)

SIV_file = "data/SIV.fasta"
SIV_records = SeqIO.parse(SIV_file, 'fasta')

SIV_fasta = {
    'id': None,
    'name': None,
    'description': None,
    'sequence': None
}

for record in SIV_records:
    SIV_fasta['id'] = record.id
    SIV_fasta['name'] = record.name
    SIV_fasta['description'] = record.description
    SIV_fasta['sequence'] = str(record.seq)

hiv1 = hiv1_fasta["sequence"]
SIV = SIV_fasta["sequence"]

print(f"HIV-1's genome is {len(hiv1)} base pairs long.")
print(f"SIV's genome is {len(SIV)} base pairs long.")

aligner = Align.PairwiseAligner()
alignments = aligner.align(hiv1, SIV)

alignments[0].score

print(alignments[0])