from collections import defaultdict

def read_file(file_path):
    with open(file_path, 'r') as file:
        text_data = file.readlines()
    return text_data

def map_function(text):
    words = text.split()
    mapped = [(word, 1) for word in words]
    return mapped

def reduce_function(mapped_data):
    word_count = defaultdict(int)
    for word, count in mapped_data:
        word_count[word] += count
    return dict(word_count)

file_path = r'd:\vscode\Semester 3\BIG DATA\Minggu 3\test.txt'

text_data = read_file(file_path)

mapped_data = []
for text in text_data:
    mapped_data.extend(map_function(text))

word_count = reduce_function(mapped_data)

print("Jumlah kata:", word_count)