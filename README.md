# Comparative Genomic Analysis of HIV-1, HIV-2, and SIV Samples

This project focuses on analyzing and comparing gene sequences of different virus types (HIV-1, HIV-2, and SIV). The goal is to uncover genetic differences that may explain variations in viral behavior, pathogenicity, and potential interactions with host genomes.  

This project aims to answer the following question:
*What are the key genetic differences between HIV-1, HIV-2, and SIV that contribute to their distinct characteristics, and how do these differences manifest in terms of sequence conservation, variability, and compositional properties of their protein-coding genes?*

## Features  
- Differences in gene sequences between HIV-1, HIV-2, and SIV
- Mutation patterns and genetic variations within and between the three virus types.  
- Structural and functional implications of these differences.  


## File Structure  
- `data/`: Input genomic sequence data.  
- `scripts/`: Analysis and preprocessing scripts.  
- `results/`: Output files, including visualizations and reports.  

## Dependencies  
- Python 3.8+  
- pandas  
- numpy  
- matplotlib  
- seaborn  
- scikit-learn  
- biopython

# Instructions
Run the scripts in the following order:
```
python scripts/parse_protein_fasta.py
python scripts/align_protein_sequences.py
python scripts/protein_analysis.py
python scripts/analyze_gc.py
python scripts/rna_hiv1_hiv2.py
python scripts/rna_hiv1_siv.py
python scripts/rna_hiv2_siv.py
python scripts/vpu_vpx_content.py
```


## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## Acknowledgments  
Special thanks to the computational biology and bioinformatics communities for their tools and resources that made this project possible.  