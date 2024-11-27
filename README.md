# Comparative Genomic Analysis of HIV-1 and HIV-2 Samples

This project focuses on analyzing and comparing gene sequences of different HIV types (HIV-1 and HIV-2). The goal is to uncover genetic differences that may explain variations in viral behavior, pathogenicity, and potential interactions with host genomes.  

## Features  
- Differences in gene sequences between HIV-1 and HIV-2.
- Mutation patterns and genetic variations within and between HIV types.  
- Structural and functional implications of these differences.  


## File Structure  
- `data/`: Input genomic sequence data.  
- `scripts/`: Analysis and preprocessing scripts.  
- `results/`: Output files, including visualizations and reports.  
- `aligned_sequences/`: Contains the sequences that have been aligned.

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
python scripts/parse_fasta.py
python scripts/align_sequences.py
python scripts/analyze_gc.py
```

## Maintainers
[@TjanMichela](https://github.com/TjanMichela), [@ZayerWang](https://github.com/ZayerWang), [@jacobssmyth](https://github.com/jacobssmyth), [@qxz313](https://github.com/qxz313)    

### Contributors  
This project exists thanks to all the people who contribute. [@TjanMichela](https://github.com/TjanMichela), [@ZayerWang](https://github.com/ZayerWang), [@jacobssmyth](https://github.com/jacobssmyth), [@qxz313](https://github.com/qxz313)   

## License  
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.  

## Acknowledgments  
Special thanks to the computational biology and bioinformatics communities for their tools and resources that made this project possible.  