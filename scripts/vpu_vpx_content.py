from Bio import SeqIO

"""
VPU AND VPX GENE CONTENT IN HIV1 HIV2 SIV
"""

for n in range(1, 5):
    hiv1_file = f"data/hiv1_{n}.gb"
    hiv2_file = f"data/hiv2_{n}.gb"
    siv_file = f"data/siv_{n}.gb"

    hiv1 = SeqIO.read(hiv1_file, "genbank")
    hiv2 = SeqIO.read(hiv2_file, "genbank")
    siv = SeqIO.read(siv_file, "genbank")

    records = [hiv1, hiv2, siv]
    names = ["hiv1", "hiv2", "siv"]

    for i, record in enumerate(records):
        for feature in record.features:
            if feature.type == "gene" and "vpu" in feature.qualifiers.get("gene", []):
                with open(f"results/{names[i]}-{n}-vpu-vpx.txt", "w") as f:
                    f.write(f"Vpu gene found at: {feature.location}")
                    f.write(f"Sequence: {feature.extract(record.seq)}")
            elif feature.type == "gene" and "vpx" in feature.qualifiers.get("gene", []):
                with open(f"results/{names[i]}-{n}-vpu-vpx.txt", "w") as f:
                    f.write(f"Vpx gene found at: {feature.location}")
                    f.write(f"Sequence: {feature.extract(record.seq)}")