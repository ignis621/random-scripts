print("This program will remove lines from a file that do NOT contain a specified word or words.")

input_file_path = input("Enter the input file path: ")
output_file_path = input("Enter the output file name: ")

user_input = input("Enter a list of strings separated by pipes (|): ")
words_to_keep = user_input.split('|')

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        if any(word in line for word in words_to_keep):
            print(line)
            output_file.write(line)

print(f"Lines containing specified words have been saved to {output_file_path}")