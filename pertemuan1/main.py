import os

# Function untuk validasi folder / file
def validasi(path):
    if os.path.exists(path):
        return True
    else:
        return False

# Membuat 5 folder
for i in range(1, 6):
    nama_folder = f"Kategori_{i}"

    # Validasi folder
    if not validasi(nama_folder):
        os.makedirs(nama_folder)

    print(f"Folder '{nama_folder}' validasi:", validasi(nama_folder))

    # Membuat 5 file teks di setiap folder
    for j in range(1, 6):
        nama_file = os.path.join(nama_folder, f"file_{j}.txt")

        # Validasi file
        if not validasi(nama_file):
            with open(nama_file, "w") as file:
                file.write(f"Ini adalah isi dari file_{j}.txt di {nama_folder}")

        print(f"File '{nama_file}' validasi:", validasi(nama_file))