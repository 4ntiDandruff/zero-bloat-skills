---
name: eeprom-flashing-skill
description: "SOP pembacaan, validasi, dan flashing SPI BIOS/EEPROM (24/25 series) via CH341A programmer & flashrom, pembersihan Intel ME Region, dan binding native Rust Tauri v2."
---

# EEPROM Firmware Flashing Skill

SOP tingkat sirkuit untuk membaca, memverifikasi, memanipulasi, dan menulis ulang chip SPI Flash EEPROM pada motherboard komputer dan laptop.

---

## 1. Persiapan Fisik & Voltage Pin 3.3V vs 5V (CH341A Mod)

- **Peringatan Kritis**: Modul programmer CH341A hitam standar pabrik sering memiliki kesalahan sirkuit bawaan: jalur data VCC/I/O mengalirkan tegangan 5.0V meskipun saklar diatur ke 3.3V.
- Sebagian besar chip SPI Flash motherboard modern (Winbond, Macronix, GigaDevice 25QXX) bekerja pada **3.3V** atau **1.8V** (seri low-voltage seperti 25Q64FW).
- Mengalirkan 5.0V ke chip 3.3V/1.8V dapat merusak struktur gerbang silikon chip secara permanen.
- Selalu pastikan jalur pinout regulator 1117-3.3V terhubung ke pin 28 chip CH341A sebelum menyambungkan klip SOIC8 ke motherboard.

---

## 2. Prosedur Pembacaan & Verifikasi Dump (Aturan MD5 Tiga Kali)

Dilarang menghapus atau menulis file baru sebelum dump firmware asli terbukti valid:

```bash
# 1. Baca chip percobaan pertama
flashrom -p ch341a_spi -r dump_01.bin

# 2. Baca chip percobaan kedua
flashrom -p ch341a_spi -r dump_02.bin

# 3. Uji kesamaan hash MD5
md5sum dump_01.bin dump_02.bin
```

Jika hash kedua file tidak identik 100%:
- Bersihkan kaki-kaki IC dari korosi atau flux menggunakan sikat dan IPA 99%.
- Pastikan jepitan klip SOIC8 menempel sempurna pada seluruh pin.
- Ulangi pembacaan hingga didapatkan hash yang identik 3 kali berturut-turut.

---

## 3. Pembersihan Intel Management Engine (Clean ME Region)

Masalah umum setelah penggantian motherboard atau chip BIOS:
- Laptop mati otomatis tepat 30 menit sekali.
- Kipas berputar kecepatan penuh (100%) terus menerus sejak pertama kali menyala.
- Boot delay (tampil gambar membutuhkan waktu 1-2 menit setelah tombol ditekan).

### Prosedur Clean ME:
1. Ekstrak bagian ME Region dari file dump menggunakan `me_cleaner` atau Intel FIT (Flash Image Tool).
2. Masukkan repository CSE/ME Region bersih (*unconfigured*) yang cocok dengan SKU chipset.
3. Rekonstruksi file BIOS dan tulis kembali ke chip via `flashrom`:
   ```bash
   flashrom -p ch341a_spi -w bios_clean_me.bin
   ```

---

## 4. Pola Rust Native Binding (Tauri v2)

Untuk aplikasi desktop tanpa dependensi berat:
- Gunakan libftdi atau binding libusb di Rust untuk berkomunikasi langsung dengan chip CH341A.
- Pantau progress bar byte per byte via background thread tanpa memblokir thread UI.
