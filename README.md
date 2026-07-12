# Computing GC Content

## OVERVIEW
This program reads multiple DNA sequences in FASTA format from a text file, computes the GC content for each sequence, and prints the ID and GC content of the sequence with the highest GC content.
It is a solution to the **"Computing GC Content"** Rosalind problem **(ID: GC)**. The tool is simple, efficient, and ideal for practicing file handling and string processing in Python.

---

## FEATURES
- Reads multiple FASTA-formatted DNA sequences from a file <u>(rosalind_gc.txt)</u>
- Parses sequence IDs and concatenates multi-line sequences
- Automatically converts input to uppercase
- Computes GC content (percentage of C and G bases) for each sequence, rounded to 6 decimal places
- Finds and reports the sequence with the highest GC content
- Clean, well-commented code with proper functions and type hints

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input FASTA file with name rosalind_gc.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_gc.txt):
```
>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT
```
**Output:**
```
Rosalind_0808
60.919540
```

---

## HOW IT WORKS
1. The program reads the FASTA file and builds a dictionary mapping each sequence ID to its full sequence
2. For each sequence, it computes the GC content: `(count of C + count of G) / length * 100`, rounded to 6 decimal places
3. It compares the GC content across all sequences to find the highest
4. Finally, it prints the ID of the sequence with the highest GC content, followed by that GC content on the next line

---

## TECHNOLOGIES USED
- **Python**
- **FASTA / TXT File**
