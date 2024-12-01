from Bio import SeqIO, Align

"""
RNA HIV2 VS SIV ANALYSIS
"""

hiv2_fna_file = "data/hiv2_1.fasta"
hiv2_fasta_records = SeqIO.parse(hiv2_fna_file, 'fasta')

hiv2_fasta = {
    'id': None,
    'name': None,
    'description': None,
    'sequence': None
}
for record in hiv2_fasta_records:
    hiv2_fasta['id'] = record.id
    hiv2_fasta['name'] = record.name
    hiv2_fasta['description'] = record.description
    hiv2_fasta['sequence'] = str(record.seq)

SIV_file = "data/siv_1.fasta"
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

hiv2 = hiv2_fasta["sequence"]
SIV = SIV_fasta["sequence"]

print(f"HIV-1's genome is {len(hiv2)} base pairs long.")
print(f"SIV's genome is {len(SIV)} base pairs long.")

aligner = Align.PairwiseAligner()
alignments = aligner.align(hiv2, SIV)

alignments[0].score

print(alignments[0])

with open(f"results/rna-hiv2-siv.txt", "w") as f:
    f.write(f"HIV-2's genome is {len(hiv2)} base pairs long.")
    f.write(f"SIV's genome is {len(SIV)} base pairs long.")
    f.write(str(alignments[0]))