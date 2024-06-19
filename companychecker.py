import re

def read_words_from_file(file_path):
    """Read words from a file and return them as a list."""
    with open(file_path, 'r') as file:
        words = file.read().split()
    return words

def get_words_from_text(text):
    """Extract a set of whole words from the text."""
    return set(re.findall(r'\b\w+\b', text))

def get_common_words(file1_path, file2_path):
    """Get the common words that exactly match in both files."""
    with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
        words1 = get_words_from_text(file1.read())
        words2 = get_words_from_text(file2.read())
        
    common_words = words1.intersection(words2)
    return common_words

def write_words_to_file(words, file_path):
    """Write the words to a file."""
    with open(file_path, 'w') as file:
        for word in words:
            file.write(word + '\n')

# Full paths to the input and output files
word_list_file = r'C:\Users\adees\Desktop\Mausaji Project\words_list.txt'
check_file = r'C:\Users\adees\Desktop\Mausaji Project\check_file.txt'
output_file = r'C:\Users\adees\Desktop\Mausaji Project\filtered_words5.txt'

# Get the common words that exactly match in both files
common_words = get_common_words(word_list_file, check_file)

# Write the common words to the output file
write_words_to_file(common_words, output_file)

print(f"Filtered words have been written to {output_file}")
