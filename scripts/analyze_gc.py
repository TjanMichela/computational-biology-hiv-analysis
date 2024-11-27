from parse_fasta import parse_fasta
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


"""
COMPUTE KEY DIFFERENCES
"""
def gc_content(sequence):
    """
    Compute GC content for a given sequence
    """
    g = sequence.count("G")
    c = sequence.count("C")
    return (g + c) / len(sequence) * 100

if __name__ == "__main__":
    hiv1_sequences = parse_fasta("data/hiv1-protein.fasta")
    hiv2_sequences = parse_fasta("data/hiv2-protein.fasta")

    gc_hiv1 = [gc_content(seq["sequence"]) for seq in hiv1_sequences]
    gc_hiv2 = [gc_content(seq["sequence"]) for seq in hiv2_sequences]

    data = {
        "Type": ["HIV-1"] * len(gc_hiv1) + ["HIV-2"] * len(gc_hiv2),
        "GC Content": gc_hiv1 + gc_hiv2
    }

    df = pd.DataFrame(data)
    sns.boxplot(x="Type", y="GC Content", data=df)
    plt.title("GC Content Comparison")
    plt.savefig("results/gc-content-comparison.png")
    plt.show()