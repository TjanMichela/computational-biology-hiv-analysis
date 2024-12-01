import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from Bio import SeqIO
from Bio.SeqUtils import gc_fraction


"""
COMPUTE KEY DIFFERENCES
"""

def compute_gc_content(file_path):
    """
    Compute GC content for RNA sequences in a FASTA file
    """
    gc_contents = []
    sequence_ids = []

    for record in SeqIO.parse(file_path, "fasta"):
        rna_seq = record.seq
        gc_content_rna = gc_fraction(rna_seq) * 100
        gc_contents.append(gc_content_rna)
        sequence_ids.append(record.id)

    return sequence_ids, gc_contents


if __name__ == "__main__":
    for n in range(1, 5):
        # Analyze GC content for RNA files
        hiv1_file = f"data/hiv1_{n}.fasta"
        hiv2_file = f"data/hiv2_{n}.fasta"
        siv_file = f"data/siv_{n}.fasta"

        ids_hiv1, gc_hiv1 = compute_gc_content(hiv1_file)
        ids_hiv2, gc_hiv2 = compute_gc_content(hiv2_file)
        ids_siv, gc_siv = compute_gc_content(siv_file)

        # Create a DataFrame for visualization
        data = {
            "Type": ["HIV-1"] * len(gc_hiv1) + ["HIV-2"] * len(gc_hiv2) + ["SIV"] * len(gc_siv),
            "GC Content": gc_hiv1 + gc_hiv2 + gc_siv,
        }

        df = pd.DataFrame(data)

        # Boxplot comparison
        plt.figure(figsize=(8, 6))
        sns.boxplot(x="Type", y="GC Content", data=df, palette="Set2")
        plt.title("GC Content Comparison of RNA Sequences")
        plt.ylabel("GC Content (%)")
        plt.xlabel("Virus Type")
        plt.savefig(f"results/gc-hiv1-2-siv-{n}-rna-boxplot.png")
        plt.show()

        # Histogram comparison
        plt.figure(figsize=(8, 6))
        sns.barplot(df, x="Type", y="GC Content", palette="Set1")
        plt.title("GC Content Distribution by Virus Type")
        plt.ylabel("GC Content (%)")
        plt.xlabel("Virus Type")
        plt.savefig(f"results/gc-hiv1-2-siv-{n}-rna-histogram.png")
        plt.show()

        print("GC Content for HIV-1 RNA Sequences:")
        for seq_id, gc in zip(ids_hiv1, gc_hiv1):
            print(f"ID: {seq_id}, GC Content: {gc:.2f}%")

        print("\nGC Content for HIV-2 RNA Sequences:")
        for seq_id, gc in zip(ids_hiv2, gc_hiv2):
            print(f"ID: {seq_id}, GC Content: {gc:.2f}%")

        print("\nGC Content for SIV RNA Sequences:")
        for seq_id, gc in zip(ids_siv, gc_siv):
            print(f"ID: {seq_id}, GC Content: {gc:.2f}%")
