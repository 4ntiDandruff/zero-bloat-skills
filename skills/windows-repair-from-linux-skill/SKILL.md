---
name: windows-repair-from-linux-skill
description: "Toolkit reparasi OS Windows dari lingkungan Linux: reset password lokal chntpw, edit registry offline, perbaikan bootloader BCD, penyelamatan data bad sector ddrescue, dan unlock BitLocker."
---

# Windows Bench Repair From Linux Skill

Panduan operasional teknisi meja servis untuk mendiagnosa, memulihkan data, dan memperbaiki instalasi Windows yang rusak menggunakan mesin Linux (live USB atau workstation servis).

---

## 1. Penanganan Partisi NTFS & Fast Startup Windows

Windows 10/11 menggunakan fitur Fast Startup yang membuat sistem operasi tidak shutdown sempurna, melainkan hibernasi kernel. Hal ini mengunci partisi NTFS dalam status "dirty".

```bash
# Identifikasi partisi target
lsblk -f

# Perbaiki status partisi NTFS tanpa merusak data
sudo ntfsfix -d /dev/nvme0n1p3

# Mount partisi dalam mode aman
sudo mkdir -p /mnt/client_windows
sudo mount -t ntfs-3g -o remove_hiberfile /dev/nvme0n1p3 /mnt/client_windows
```

---

## 2. Reset Password Akun Lokal Windows (Offline)

Gunakan utilitas `chntpw` untuk mereset akun lokal yang terkunci atau lupa password:

```bash
cd /mnt/client_windows/Windows/System32/config

# Tampilkan seluruh daftar user di SAM hive
sudo chntpw -l SAM

# Buka menu interaktif untuk user tertentu
sudo chntpw -u "NamaUser" SAM
# Pilihan menu:
# 1 -> Clear (blank) user password
# 2 -> Unlock and enable user account
# q -> Keluar dan simpan perubahan (ketik 'y')
```

---

## 3. Penyelamatan Data dari Media Bad Sector (`ddrescue`)

Jangan gunakan `cp` atau file manager grafis untuk menyalin data dari harddisk/SSD yang mengalami bad sector. File manager akan freeze saat menabrak bad block.

```bash
# Salin image disk dengan logging peta bad sector
sudo ddrescue -d -r 2 /dev/sdb /home/michael/backup_disk.img /home/michael/rescue.map

# Mount file image hasil rescue untuk mengambil dokumen pelanggan
sudo losetup -Pf /home/michael/backup_disk.img
```

---

## 4. Buka Kunci Partisi BitLocker via Linux (`dislocker`)

Jika partisi klien terenkripsi BitLocker dan klien memiliki recovery key 48 digit:

```bash
sudo mkdir -p /mnt/bitlocker_raw /mnt/bitlocker_data

# Dekripsi partisi ke block device virtual
sudo dislocker /dev/nvme0n1p3 -p484848-XXXXXX-XXXXXX-... -- /mnt/bitlocker_raw

# Mount file virtual hasil dekripsi
sudo mount -t ntfs-3g -o ro /mnt/bitlocker_raw/dislocker-file /mnt/bitlocker_data
```
