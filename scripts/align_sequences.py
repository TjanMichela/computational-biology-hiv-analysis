from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from parse_fasta import parse_fasta
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


"""
HIV1 VS HIV2 PROTEIN SEQUENCES ALIGNMENT
"""

# Function to align sequences
def align_sequences(seq_list1, seq_list2, output_file, fasta_output_file):
    """
    Inputs two sequence lists, aligns them, and outputs results to text and FASTA files
    """
    with open(output_file, "w") as out:
        fasta_records = [] 

        for seq1 in seq_list1:
            for seq2 in seq_list2:
                # Perform global alignment
                alignments = pairwise2.align.globalxx(seq1["sequence"], seq2["sequence"])
                best_alignment = alignments[0] 

                # Write the formatted alignment to the output file
                out.write(f"Alignment between {seq1['id']} and {seq2['id']}:\n")
                out.write(format_alignment(*best_alignment) + "\n")
                out.write("-" * 80 + "\n")

                # Create SeqRecord objects for FASTA output
                aligned_seq1 = SeqRecord(
                    Seq(best_alignment.seqA),
                    id=f"{seq1['id']}_aligned_to_{seq2['id']}",
                    description="Aligned sequence 1"
                )
                aligned_seq2 = SeqRecord(
                    Seq(best_alignment.seqB),
                    id=f"{seq2['id']}_aligned_to_{seq1['id']}",
                    description="Aligned sequence 2"
                )
                fasta_records.extend([aligned_seq1, aligned_seq2])

        # Write aligned sequences to a FASTA file
        SeqIO.write(fasta_records, fasta_output_file, "fasta")


if __name__ == "__main__":
    # Parse input sequences
    hiv1_sequences = parse_fasta("data/hiv1-protein.fasta")
    hiv2_sequences = parse_fasta("data/hiv2-protein.fasta")

    # Perform alignment and generate outputs
    align_sequences(
        hiv1_sequences,
        hiv2_sequences,
        "results/hiv1-vs-hiv2-protein-alignments.txt",
        "aligned_sequences/aligned-hiv1-hiv2-protein.fasta"
    )