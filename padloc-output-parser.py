import pandas as pd
import os
import argparse

def process_file(filepath):
    # Extract the filename without the extension to use as the new seqid
    filename = os.path.splitext(os.path.basename(filepath))[0]
    
    # Load the table from a CSV file
    df = pd.read_csv(filepath, sep=',')  # Adjust the separator if needed
    
    # Replace the 'seqid' column with the filename
    df['seqid'] = filename
    
    # Save the modified table to a new CSV file
    new_filepath = filepath.replace('.csv', '_modified.csv')  # Save as a new file to avoid overwriting the original
    df.to_csv(new_filepath, sep=',', index=False)
    print(f"File '{filepath}' processed and saved as '{new_filepath}'. 'seqid' updated with '{filename}'.")

def process_all_files(directory):
    # List all CSV files in the directory
    files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith('.csv')]
    print(f"Found {len(files)} files to process.")
    
    # Process each file
    for file in files:
        process_file(file)

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Process all CSV files in a directory and replace 'seqid' with the filename.")
    # Add an argument for the directory path
    parser.add_argument('directory', type=str, help="The directory containing the CSV files to process.")
    
    # Parse the arguments
    args = parser.parse_args()
    
    # Process all files in the provided directory
    process_all_files(args.directory)

if __name__ == "__main__":
    main()
