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
    # Analyze GC content for RNA files
    hiv1_file = "data/hiv1.fna"
    hiv2_file = "data/hiv2.fna"

    ids_hiv1, gc_hiv1 = compute_gc_content(hiv1_file)
    ids_hiv2, gc_hiv2 = compute_gc_content(hiv2_file)

    # Create a DataFrame for visualization
    data = {
        "Type": ["HIV-1"] * len(gc_hiv1) + ["HIV-2"] * len(gc_hiv2),
        "GC Content": gc_hiv1 + gc_hiv2,
    }

    df = pd.DataFrame(data)

    # Boxplot comparison
    plt.figure(figsize=(8, 6))
    sns.boxplot(x="Type", y="GC Content", data=df, palette="Set2")
    plt.title("GC Content Comparison of RNA Sequences")
    plt.ylabel("GC Content (%)")
    plt.xlabel("HIV Type")
    plt.savefig("results/gc-content-comparison-rna-boxplot.png")
    plt.show()

    # Histogram comparison
    plt.figure(figsize=(8, 6))
    sns.histplot(df, x="GC Content", hue="Type", kde=False, bins=15, palette="Set1", alpha=0.7)
    plt.title("GC Content Distribution by HIV Type")
    plt.ylabel("Frequency")
    plt.xlabel("GC Content (%)")
    plt.savefig("results/gc-content-comparison-rna-histogram.png")
    plt.show()

    # KDE plot comparison
    plt.figure(figsize=(8, 6))
    sns.kdeplot(data=df, x="GC Content", hue="Type", fill=True, common_norm=False, palette="Set3", alpha=0.5)
    plt.title("GC Content Density by HIV Type")
    plt.ylabel("Density")
    plt.xlabel("GC Content (%)")
    plt.savefig("results/gc-content-comparison-rna-kde.png")
    plt.show()

    print("GC Content for HIV-1 RNA Sequences:")
    for seq_id, gc in zip(ids_hiv1, gc_hiv1):
        print(f"ID: {seq_id}, GC Content: {gc:.2f}%")

    print("\nGC Content for HIV-2 RNA Sequences:")
    for seq_id, gc in zip(ids_hiv2, gc_hiv2):
        print(f"ID: {seq_id}, GC Content: {gc:.2f}%")
