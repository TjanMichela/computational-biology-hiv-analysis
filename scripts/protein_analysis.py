from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

"""
PROTEIN ANALYSIS
"""

filepaths = ["data/hiv1-protein.fasta","data/hiv2-protein.fasta"]
filenames = ["hiv1", "hiv2"]

for i, file in enumerate(filepaths): 
    for record in SeqIO.parse(file, "fasta"):
        amino_acid_seq = str(record.seq)
        
        analysis = ProteinAnalysis(amino_acid_seq)
        amino_acid_composition = analysis.get_amino_acids_percent()
        
        print(f"Protein ID: {record.id}")
        print("Amino Acid Composition (Percentage):")
        for aa, percent in amino_acid_composition.items():
            print(f"{aa}: {percent:.2%}")

        with open("results/{filenames[i]}-protein-analysis.txt", "w") as f:
            f.write(f"Protein ID: {record.id}\n")
            f.write(f"Amino Acid Composition (Percentage):")
            for aa, percent in amino_acid_composition.items():
                f.write(f"{aa}: {percent:.2%}")