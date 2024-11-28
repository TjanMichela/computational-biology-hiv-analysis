from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


"""
PROMOTER ANALYSIS
"""
# Function to analyze promoter features in two sets of sequences
def analyze_promoter(seq_list1, seq_list2, output_file):
    """
    Analyze two sets of sequences for promoter features (e.g., TATA box, CAAT box).
    :param seq_list1: List of sequences (dict with 'id' and 'sequence') from the first set.
    :param seq_list2: List of sequences (dict with 'id' and 'sequence') from the second set.
    :param output_file: Path to save analysis results in text format.
    """
    # Promoter features to search for
    promoter_features = {
        "TATA_box": "TATA",
        "CAAT_box": "CAAT",
        "GC_rich_region": "GGGCGG"
    }

    with open(output_file, "w") as out:
        # Compare each sequence in the two lists
        for seq1 in seq_list1:
            for seq2 in seq_list2:
                out.write(f"Analysis between {seq1['id']} and {seq2['id']}:\n")
                out.write(f"Sequence 1: {seq1['sequence']}\n")
                out.write(f"Sequence 2: {seq2['sequence']}\n")
                
                # Search for promoter features in both sequences
                for feature_name, feature_seq in promoter_features.items():
                    # Search in Sequence 1
                    positions1 = find_feature_positions(seq1["sequence"], feature_seq)
                    if positions1:
                        out.write(f"  {feature_name} in Sequence 1: Found at positions {positions1}\n")
                    else:
                        out.write(f"  {feature_name} in Sequence 1: Not found\n")
                    
                    # Search in Sequence 2
                    positions2 = find_feature_positions(seq2["sequence"], feature_seq)
                    if positions2:
                        out.write(f"  {feature_name} in Sequence 2: Found at positions {positions2}\n")
                    else:
                        out.write(f"  {feature_name} in Sequence 2: Not found\n")
                
                out.write("-" * 80 + "\n")


# Helper function to find positions of a feature in a sequence
def find_feature_positions(sequence, feature_seq):
    """
    Find all positions of a feature in a sequence.
    :param sequence: The sequence to search.
    :param feature_seq: The feature sequence to find.
    :return: List of positions where the feature is found.
    """
    positions = []
    start = 0
    while True:
        start = sequence.find(feature_seq, start)
        if start == -1:
            break
        positions.append(start)
        start += 1  # Move past the current match
    return positions


if __name__ == "__main__":
    # Parse input sequences
    def parse_fasta(file_path):
        """
        Parse FASTA files and store the sequences.
        :param file_path: Path to the FASTA file.
        :return: List of sequences (dict with 'id' and 'sequence').
        """
        sequences = []
        for record in SeqIO.parse(file_path, "fasta"):
            sequences.append({"id": record.id, "sequence": str(record.seq)})
        return sequences

    # Load sequences from two FASTA files
    seq_list1 = parse_fasta("hiv1-protein.fasta")
    seq_list2 = parse_fasta("hiv2-protein.fasta")

    # Perform promoter analysis and save results
    analyze_promoter(
        seq_list1,
        seq_list2,
        "results/promoter_analysis.txt"
    )