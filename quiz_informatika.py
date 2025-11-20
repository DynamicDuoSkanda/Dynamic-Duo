import random

# ================================
#   DAFTAR SOAL QUIZ INFORMATIKA
# ================================

quiz = [

    # --- 3 Soal Awal ---
    {
        "question": "Perangkat yang digunakan untuk memasukkan data adalah...",
        "options": {
            "A": "Monitor",
            "B": "Keyboard",
            "C": "Speaker",
            "D": "Proyektor",
            "E": "Printer"
        },
        "answer": "B"
    },
    {
        "question": "Penyimpanan utama yang bersifat volatile adalah...",
        "options": {
            "A": "Harddisk",
            "B": "SSD",
            "C": "Optical Disk",
            "D": "RAM",
            "E": "Flashdisk"
        },
        "answer": "D"
    },
    {
        "question": "Yang termasuk perangkat keluaran (output device) adalah...",
        "options": {
            "A": "Mouse",
            "B": "Keyboard",
            "C": "Monitor",
            "D": "Scanner",
            "E": "Microphone"
        },
        "answer": "C"
    },

    # --- 25 Soal Tambahan ---
    {
        "question": "Sistem operasi yang bersifat open source adalah...",
        "options": {
            "A": "Windows",
            "B": "MacOS",
            "C": "Linux",
            "D": "Android",
            "E": "iOS"
        },
        "answer": "C"
    },
    {
        "question": "Perangkat keras yang berfungsi sebagai otak komputer adalah...",
        "options": {
            "A": "RAM",
            "B": "CPU",
            "C": "SSD",
            "D": "Monitor",
            "E": "Mouse"
        },
        "answer": "B"
    },
    {
        "question": "File berekstensi .py adalah file untuk...",
        "options": {
            "A": "Bahasa Java",
            "B": "Bahasa C++",
            "C": "Bahasa Python",
            "D": "Bahasa HTML",
            "E": "Bahasa JavaScript"
        },
        "answer": "C"
    },
    {
        "question": "RAM digunakan untuk menyimpan...",
        "options": {
            "A": "File permanen",
            "B": "Data sementara",
            "C": "Aplikasi offline",
            "D": "Program terhapus",
            "E": "Sistem BIOS"
        },
        "answer": "B"
    },
    {
        "question": "Perangkat berikut termasuk input device adalah...",
        "options": {
            "A": "Monitor",
            "B": "Mouse",
            "C": "Speaker",
            "D": "Proyektor",
            "E": "Flashdisk"
        },
        "answer": "B"
    },
    {
        "question": "Bahasa markup untuk membuat website adalah...",
        "options": {
            "A": "CSS",
            "B": "SQL",
            "C": "HTML",
            "D": "PHP",
            "E": "C#"
        },
        "answer": "C"
    },
    {
        "question": "Perangkat penyimpanan tercepat di bawah ini adalah...",
        "options": {
            "A": "HDD",
            "B": "SSD SATA",
            "C": "SSD NVMe",
            "D": "Flashdisk",
            "E": "CD-ROM"
        },
        "answer": "C"
    },
    {
        "question": "Perintah untuk menampilkan teks di Python adalah...",
        "options": {
            "A": "echo()",
            "B": "print()",
            "C": "show()",
            "D": "display()",
            "E": "text()"
        },
        "answer": "B"
    },
    {
        "question": "Virus komputer adalah contoh dari...",
        "options": {
            "A": "Hardware",
            "B": "Software",
            "C": "Malware",
            "D": "Aplikasi",
            "E": "OS"
        },
        "answer": "C"
    },
    {
        "question": "Yang bukan merupakan web browser adalah...",
        "options": {
            "A": "Chrome",
            "B": "Firefox",
            "C": "Safari",
            "D": "Opera",
            "E": "YouTube"
        },
        "answer": "E"
    },
    {
        "question": "Shortcut keyboard untuk menyalin (copy) adalah...",
        "options": {
            "A": "Ctrl + P",
            "B": "Ctrl + A",
            "C": "Ctrl + C",
            "D": "Ctrl + V",
            "E": "Ctrl + X"
        },
        "answer": "C"
    },
    {
        "question": "Hardware untuk menampilkan visual adalah...",
        "options": {
            "A": "Mouse",
            "B": "Monitor",
            "C": "Keyboard",
            "D": "Scanner",
            "E": "Modem"
        },
        "answer": "B"
    },
    {
        "question": "Algoritma adalah...",
        "options": {
            "A": "Bahasa pemrograman",
            "B": "Langkah-langkah penyelesaian masalah",
            "C": "Jenis komputer",
            "D": "Perangkat jaringan",
            "E": "Proses instalasi aplikasi"
        },
        "answer": "B"
    },
    {
        "question": "Python termasuk bahasa pemrograman...",
        "options": {
            "A": "Low level",
            "B": "Machine language",
            "C": "High level",
            "D": "Assembly",
            "E": "Hardware language"
        },
        "answer": "C"
    },
    {
        "question": "Komponen komputer yang menyuplai daya listrik adalah...",
        "options": {
            "A": "PSU",
            "B": "RAM",
            "C": "VGA",
            "D": "Processor",
            "E": "Heatsink"
        },
        "answer": "A"
    },
    {
        "question": "Ekstensi file gambar adalah...",
        "options": {
            "A": ".docx",
            "B": ".pptx",
            "C": ".jpg",
            "D": ".xlsx",
            "E": ".txt"
        },
        "answer": "C"
    },
    {
        "question": "Jenis jaringan komputer terkecil adalah...",
        "options": {
            "A": "WAN",
            "B": "MAN",
            "C": "LAN",
            "D": "Internet",
            "E": "VPN"
        },
        "answer": "C"
    },
    {
        "question": "Perusahaan yang mengembangkan Python adalah...",
        "options": {
            "A": "Google",
            "B": "Apple",
            "C": "Microsoft",
            "D": "Python Software Foundation",
            "E": "IBM"
        },
        "answer": "D"
    },
    {
        "question": "Yang termasuk aplikasi pengolah angka adalah...",
        "options": {
            "A": "MS Word",
            "B": "MS Excel",
            "C": "MS Publisher",
            "D": "MS Access",
            "E": "PowerPoint"
        },
        "answer": "B"
    },
    {
        "question": "Perangkat yang digunakan untuk menangkap gambar adalah...",
        "options": {
            "A": "Webcam",
            "B": "Monitor",
            "C": "Speaker",
            "D": "Printer",
            "E": "UPS"
        },
        "answer": "A"
    },
    {
        "question": "Fungsi utama firewall adalah...",
        "options": {
            "A": "Meningkatkan kecepatan internet",
            "B": "Melindungi jaringan dari akses berbahaya",
            "C": "Mempercepat CPU",
            "D": "Menghapus file duplikat",
            "E": "Backup data otomatis"
        },
        "answer": "B"
    },
    {
        "question": "Cloud storage berikut adalah...",
        "options": {
            "A": "Google Drive",
            "B": "Flashdisk",
            "C": "SSD",
            "D": "HDD",
            "E": "RAM"
        },
        "answer": "A"
    },
    {
        "question": "Fungsi utama GPU adalah...",
        "options": {
            "A": "Mengolah grafik",
            "B": "Menyimpan data",
            "C": "Mengirim email",
            "D": "Mengatur jaringan",
            "E": "Menjalankan BIOS"
        },
        "answer": "A"
    },
    {
        "question": "Perangkat jaringan yang membagi koneksi internet adalah...",
        "options": {
            "A": "Switch",
            "B": "Router",
            "C": "Hub",
            "D": "Repeater",
            "E": "Bridge"
        },
        "answer": "B"
    },
    {
        "question": "Apa singkatan dari URL?",
        "options": {
            "A": "User Response Link",
            "B": "Universal Routing Line",
            "C": "Unified Resource Link",
            "D": "Uniform Resource Locator",
            "E": "Unique Route Locator"
        },
        "answer": "D"
    }
]

# ================================
#      LOGIKA PROGRAM QUIZ
# ================================

print("\n=== QUIZ INFORMATIKA INTERAKTIF ===\n")
random.shuffle(quiz)

score = 0
total_soal = len(quiz)

for index, q in enumerate(quiz, start=1):
    print(f"{index}. {q['question']}")
    for key, val in q["options"].items():
        print(f"  {key}. {val}")

    answer = input("Jawaban kamu (A/B/C/D/E): ").upper()

    if answer == q["answer"]:
        print("✔ Benar!\n")
        score += 1
    else:
        print(f"✖ Salah! Jawaban benar adalah {q['answer']}\n")

# Hitung nilai 0–100
nilai = (score / total_soal) * 100

print("=== HASIL AKHIR ===")
print(f"Benar : {score} dari {total_soal} soal")
print(f"Nilai : {nilai:.2f} / 100")
print("====================\n")
