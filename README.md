# Kopi-Kita Kasir ☕

Aplikasi kasir sederhana untuk kedai kopi, dibuat dengan Python (Flask).

## Fitur
- Hitung subtotal berdasarkan menu (Kopi Susu, Americano, Latte)
- Promo Rp5.000 jika subtotal > Rp50.000
- Diskon 10% setiap hari Rabu
- Diskon tambahan 5% untuk member
- Tanggal & jam otomatis zona WIB
- Tampilan struk rapi dalam tabel

## Cara Menjalankan (Lokal)
1. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan server:
   ```bash
   python app.py
   ```
3. Buka di browser: `http://127.0.0.1:5000`

## Deploy ke Render
- Pastikan repo berisi:
  - app.py
  - requirements.txt
  - Procfile
  - templates/index.html
- Di Render:
  - Build Command: `pip install -r requirements.txt`
  - Start Command: `gunicorn app:app`

Setelah deploy, aplikasi bisa diakses lewat link publik (contoh: `https://kopi-kita.onrender.com`).

Kasir default: **Belen**.
