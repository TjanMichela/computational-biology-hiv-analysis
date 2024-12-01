from Bio import SeqIO


"""
PARSE FILES
"""

# Function to parse the fasta files
def parse_fasta(file_path):
    """
    Parse fasta files and store the sequences
    """
    sequences = []
    for record in SeqIO.parse(file_path, "fasta"):
        sequences.append({"id": record.id, "sequence": str(record.seq)})
    return sequences


if __name__ == "__main__":
    hiv1_sequences = parse_fasta("data/hiv1-protein.fasta")
    hiv2_sequences = parse_fasta("data/hiv2-protein.fasta")

    with open("results/hiv1-protein-parsed.txt", "w") as f:
        for seq in hiv1_sequences:
            f.write(f">{seq["id"]}\n{seq["sequence"]}\n")

    with open("results/hiv2-protein-parsed.txt", "w") as f:
        for seq in hiv2_sequences:
            f.write(f">{seq["id"]}\n{seq["sequence"]}\n")