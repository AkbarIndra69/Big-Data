from collections import defaultdict

# Fungsi untuk membaca file dan mengembalikan data dalam bentuk list
def read_file(file_path):
    with open(file_path, 'r') as file:
        text_data = [line.strip().split(',') for line in file.readlines()]
    return text_data

# Fungsi map untuk mengambil judul lagu dari data
def map_function(text):
    judul_lagu = text[1].strip()
    return [(judul_lagu, 1)]

# Fungsi reduce untuk menghitung kemunculan judul lagu
def reduce_function(mapped_data):
    program_count = defaultdict(int)
    for judul_lagu, count in mapped_data:
        program_count[judul_lagu] += count
    return dict(program_count)

# Mendapatkan frekuensi kemunculan lagu tertentu
def search_song_occurrences(song_title, program_count):
    if song_title in program_count:
        return f"Lagu '{song_title}' muncul {program_count[song_title]} kali."
    else:
        return f"Lagu '{song_title}' tidak ditemukan dalam dataset."

# File path untuk data lagu
file_path = 'guitarDB.txt'

# Baca data dari file
text_data = read_file(file_path)

# Proses map dan reduce
mapped_data = []
for row in text_data[1:]:
    mapped_data.extend(map_function(row))

program_count = reduce_function(mapped_data)

# Judul lagu yang ingin dicari
song_title = input("Masukkan judul lagu yang ingin dicari: ")

# Cari frekuensi kemunculan lagu
result = search_song_occurrences(song_title, program_count)

# Cetak hasilnya
print(result)
