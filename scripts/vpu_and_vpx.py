from Bio import SeqIO

"""
VPU AND VPX GENE CONTENT IN HIV1 HIV2 SIV
"""

genome_file = "hiv1.gb"
record = SeqIO.read(genome_file, "genbank")

for feature in record.features:
    if feature.type == "gene" and "vpu" in feature.qualifiers.get("gene", []):
        print(f"Vpu gene found at: {feature.location}")
        print(f"Sequence: {feature.extract(record.seq)}")

genbank_file = "hiv2.gb"
record = SeqIO.read(genbank_file, "genbank")

for feature in record.features:
    if feature.type == "gene" and "vpx" in feature.qualifiers.get("gene", []):
        print(f"Vpx gene found at: {feature.location}")
        print(f"Sequence: {feature.extract(record.seq)}")