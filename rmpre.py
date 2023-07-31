import os
import argparse

def remove_prefix_from_filenames(directory, prefix):
    # Get the current working directory if no directory path is provided
    if not directory:
        directory = os.getcwd()

    # Get a list of all files in the specified directory
    files = os.listdir(directory)

    # Loop through each file and check if it starts with the given prefix
    for filename in files:
        if filename.startswith(prefix):
            # Generate the new filename by removing the prefix from the beginning
            new_filename = filename[len(prefix):]

            # Get the full paths for the old and new filenames
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_filename)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {filename} to {new_filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Remove a specified prefix from filenames in a directory.")
    parser.add_argument("directory", nargs="?", help="The directory containing the files. If not provided, the current working directory will be used.")
    parser.add_argument("prefix", help="The prefix to remove from filenames.")
    args = parser.parse_args()

    remove_prefix_from_filenames(args.directory, args.prefix)
