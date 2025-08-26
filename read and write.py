# File Read & Write Challenge

try:
    # Open the original file for reading
    with open("input.txt", "r") as infile:
        content = infile.read()

    # Modify content (example: make everything uppercase)
    modified_content = content.upper()

    # Write modified content to a new file
    with open("output.txt", "w") as outfile:
        outfile.write(modified_content)

    print("File successfully read and modified! Check 'output.txt'.")

except FileNotFoundError:
    print("Error: The file 'input.txt' was not found.")
except Exception as e:
    print("An error occurred:", e)
