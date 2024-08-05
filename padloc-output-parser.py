import pandas as pd
import os
import argparse
import re

def process_file(filepath, all_seqids):
    # Extract the full filename with extension
    filename = os.path.basename(filepath)
    original_filename = filename

    # Specific string to remove from the filename
    string_to_remove = '.fasta_padloc.csv'

    # Remove the specific substring from the filename, if present
    if string_to_remove in filename:
        filename = filename.replace(string_to_remove, '')

    # Load the table from a CSV file
    df = pd.read_csv(filepath, sep=',')  # Adjust the separator if needed

    # Replace the 'seqid' column with the modified filename
    df['seqid'] = filename

    # Save the modified table to a new CSV file
    new_filepath = filepath.replace(original_filename, filename + '_final_modified.csv')
    df.to_csv(new_filepath, sep=',', index=False)
    print(f"File '{filepath}' processed and saved as '{new_filepath}'.")

    # For aggregation: Correctly transform 'seqid' to "Accession[tab]Start[tab]Stop" format
    # Use regex to replace the last two underscores between numbers with a tab
    transformed_seqid = re.sub(r'_(?=\d)', '\t', filename, 2)
    all_seqids.add(transformed_seqid)

def process_all_files(directory):
    # Set to store all unique transformed 'seqid'
    all_seqids = set()

    # List all CSV files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]
    print(f"Found {len(files)} files to process.")

    # Process each file
    for file in files:
        process_file(file, all_seqids)

    # After all files are processed, save the unique seqids to a single CSV file
    unique_seqids_file = os.path.join(directory, 'aggregated_unique_seqids.tsv')  # Use TSV for tab-separated values
    with open(unique_seqids_file, 'w') as f:
        for seqid in all_seqids:
            f.write(seqid + '\n')
    print(f"All unique seqids aggregated and saved to '{unique_seqids_file}'.")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process all CSV files in a directory, replace 'seqid' with filenames, and aggregate unique seqid transformations.")
    # Add an argument for the directory path
    parser.add_argument('directory', type=str, help="The directory containing the CSV files to process.")

    # Parse the arguments
    args = parser.parse_args()

    # Process all files in the provided directory
    process_all_files(args.directory)

if __name__ == "__main__":
    main()
