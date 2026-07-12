def read_dna_from_txt(file_path: str) -> dict[str, str]: # Reads FASTA-formatted DNA sequences into id: sequence
    sequences: dict[str, str] = {} # Create an empty dictionary for pairs
    current_id = "" # Create empty variable for the current ID
    with open(file_path) as f: # Open the file for reading
        for line in f:
            cleaned = line.strip() # Remove leading/trailing whitespace
            if not cleaned:
                continue
            if cleaned.startswith(">"):  # Check if this line is a FASTA header
                current_id = cleaned[1:]
                sequences[current_id] = ""
            else:
                sequences[current_id] += cleaned.upper() # Uppercase only the sequence bases
    return sequences


def compute_gc_content(sequence: str) -> float: # Returns the percentage of C and G bases in the sequence
    gc_count = sequence.count("C") + sequence.count("G") # Counts how many times C and G appeared in the string
    return round(gc_count / len(sequence) * 100, 6) # Turn the number into the percent and round it to the 6th decimal points


def find_highest_gc_content(sequences: dict[str, str]) -> tuple[str, float]: # Returns the ID, gc_content pair with the highest GC content
    best_id = "" # Empty variable for the ID of the highest GC Content
    best_gc = -1.0  # Starts below any possible GC content, so the first sequence checked always becomes the initial best
    for seq_id, sequence in sequences.items():
        gc = compute_gc_content(sequence)
        if gc > best_gc: # Comparison between different pairs with the constant update of the highest GC Content
            best_gc = gc
            best_id = seq_id
    return best_id, best_gc # Return the highest GC Content


def main(): # Runs the overall program: reads file, finds highest GC content, prints result
    sequences = read_dna_from_txt("rosalind_gc.txt")
    best_id, best_gc = find_highest_gc_content(sequences)
    print(best_id)
    print(f"{best_gc:.6f}") #


if __name__ == "__main__": # Entry point of the code
    main()
