from Bio import SeqIO, Align

"""
RNA HIV1 VS HIV2 ANALYSIS
"""

hiv1_fna_file = "data/hiv1_1.fasta"
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

hiv1 = hiv1_fasta["sequence"]
hiv2 = hiv2_fasta["sequence"]

print(f"HIV-1's genome is {len(hiv1)} base pairs long.")
print(f"HIV-2's genome is {len(hiv2)} base pairs long.")

aligner = Align.PairwiseAligner()
alignments = aligner.align(hiv1, hiv2)

alignments[0].score

print(alignments[0])

with open(f"results/rna-hiv1-hiv2.txt", "w") as f:
    f.write(f"HIV-1's genome is {len(hiv1)} base pairs long.")
    f.write(f"HIV-2's genome is {len(hiv2)} base pairs long.")
    f.write(str(alignments[0]))