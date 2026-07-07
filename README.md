<div align="center">

# Interpreter Kustom Sederhana (Python GUI)

[![Python](https://img.shields.io/badge/Language-Python_3-blue.svg)]()
[![GUI](https://img.shields.io/badge/GUI-Tkinter-orange.svg)]()
[![Concept](https://img.shields.io/badge/Concept-Compiler_Design-success.svg)]()

</div>

---

## 📖 Latar Belakang & Deskripsi
Proyek ini adalah implementasi **Interpreter Bahasa Pemrograman Kustom** sederhana yang dibangun menggunakan Python. Interpreter ini membaca teks (skrip) baris demi baris, memecah (*parsing*) sintaks kustom melalui ekspresi reguler (*Regular Expression*/RegEx), mengevaluasi operasi matematika, dan mengatur alur (*control flow*) secara rekursif.

Proyek ini mendemonstrasikan pemahaman kuat tentang konsep dasar *Software Engineering* dan *Compiler Design*, termasuk *Lexical Analysis* (pemindaian string) dan *Abstract Syntax Tree Evaluation* (lewat evaluasi dinamis). Alat ini dibungkus dengan GUI interaktif menggunakan pustaka **Tkinter** untuk memudahkan pengguna mengetik dan menjalankan program buatan mereka sendiri.

---

## 📚 Kamus Sintaks (Syntax Dictionary)
Interpreter ini berjalan berdasarkan aturan dan struktur bahasa yang dirancang khusus (mirip *pseudocode* bahasa Indonesia).

| Perintah | Deskripsi & Contoh |
| --- | --- |
| **Deklarasi Variabel (`=`)** | Mendukung operasi aritmatika kompleks secara langsung berkat *dynamic evaluation*. <br>Contoh: `a=2+3/2*10-3` |
| **Kondisi (`jika`)** | Membandingkan variabel dengan angka absolut menggunakan operator (`<`, `<=`, `>`, `>=`). <br>Contoh: `jika a<10` |
| **Label Lompatan (`:`)** | Menandai baris tertentu sebagai destinasi lompatan program (*looping*/iterasi). <br>Contoh: `ulang:` |
| **Lompatan Eksekusi (`goto`)**| Memaksa interpreter melompat ke label jika kondisi bernilai `True`. <br>Contoh: `goto ulang` |
| **Mencetak Output (`nyetak`)**| Menampilkan nilai variabel atau teks ke terminal GUI. Mendukung format parameter dengan kutip tunggal/ganda.<br>Contoh: `nyetak('nilai:', a)` atau `nyetak(a)` |

---

## 🚀 Cara Menjalankan Aplikasi
1. Pastikan Anda telah menginstal **Python 3** di sistem Anda.
2. Kloning (unduh) repositori ini ke komputer Anda.
3. Jalankan berkas Python utama melalui terminal atau Command Prompt:
   ```bash
   python "projcompiler v3.1.py"
   ```
4. Jendela GUI akan terbuka. Anda dapat:
   - Mengetik sintaks kustom langsung pada kotak teks bagian atas.
   - Atau mengeklik tombol **File** untuk memuat skrip berekstensi `.txt`.
5. Klik **Run** untuk mengeksekusi skrip. Hasil *output* atau perhitungan akan muncul pada kotak teks bagian bawah.

---

## 💻 Contoh Penggunaan
Berikut adalah demonstrasi program yang telah dieksekusi menggunakan interpreter ini.

### 1. Program Hitung Maju Sederhana
Program ini menunjukkan fungsi dasar deklarasi variabel, pencetakan *output*, evaluasi sebaris, dan *conditional jump*.
```text
a=1
ulang:
a=a+1
nyetak(a)
jika a<10 goto ulang
```
**Hasil Eksekusi:**
<div align="center">
  <img src="assets/hasil program 1.png" width="600" alt="Hasil Program 1">
</div>

### 2. Program Evaluasi Aritmatika Kompleks & Looping
Program yang lebih rumit dengan evaluasi operasi matematika beruntun dan loop dinamis multibaris, mendemonstrasikan stabilitas interpreter dalam mengelola memori variabel yang di-update secara berulang.
```text
a=2+3/2*10-3
b=a+20/2+2
b=b+2
c=b-a
ulang:
c=c+1
nyetak('nilai c:',c)
jika c<1000 
goto ulang
```
**Hasil Eksekusi:**
<div align="center">
  <img src="assets/hasil program 2.png" width="600" alt="Hasil Program 2">
</div>
