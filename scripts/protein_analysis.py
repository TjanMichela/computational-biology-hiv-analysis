from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""
PROTEIN ANALYSIS
"""

filepaths = ["data/hiv1-protein.fasta","data/hiv2-protein.fasta"]
filenames = ["hiv1", "hiv2"]

amino_acid_data = []

for i, file in enumerate(filepaths): 
    for record in SeqIO.parse(file, "fasta"):
        amino_acid_seq = str(record.seq)
        
        analysis = ProteinAnalysis(amino_acid_seq)
        amino_acid_composition = analysis.get_amino_acids_percent()

        for aa, percent in amino_acid_composition.items():
            amino_acid_data.append({
                "Virus Type": filenames[i],
                "Protein ID": record.id,
                "Amino Acid": aa,
                "Percentage": percent * 100
            })

        with open(f"results/{filenames[i]}-protein-analysis.txt", "w") as f:
            f.write(f"Protein ID: {record.id}\n")
            f.write(f"Amino Acid Composition (Percentage):")
            for aa, percent in amino_acid_composition.items():
                f.write(f"{aa}: {percent:.2%}")

df_amino_acid = pd.DataFrame(amino_acid_data)

plt.figure(figsize=(14, 8))
sns.boxplot(x="Amino Acid", y="Percentage", hue="Virus Type", data=df_amino_acid, showmeans=True)
plt.title("Amino Acid Composition Comparison: HIV-1 vs HIV-2")
plt.xlabel("Amino Acid")
plt.ylabel("Composition Percentage")
plt.xticks(rotation=45)
plt.legend(title="Virus Type")
plt.tight_layout()

plt.savefig("results/hiv1_vs_hiv2_amino_acid_composition.png")
plt.show()