---
name: ventoy-servicing-skill
description: "Workbench USB bootable servicing SOP: Ventoy Global CLI configuration, Windows 11 TPM/SecureBoot/RAM/Account bypass, Intel Gen 11-14 RST VMD storage driver injection, and .ventoyignore management."
---

# VENTOY-SERVICING-SKILL
### SOP Flashdisk Bootable Meja Servis & Triage Multiboot Linux/Windows

Modul ini adalah standar operasional meja kerja (*workbench SOP*) untuk mengelola flashdisk multiboot Ventoy teknisi: rendering menu CLI anti-lag/melar pada monitor servis, otomatisasi bypass instalasi Windows 11, injeksi driver storage Intel RST VMD Gen 11-14 (Obat VMD) agar SSD NVMe terbaca, penyembunyian folder kerja via `.ventoyignore`, dan sekring kernel buffer flushing (`sync`) di Linux.

---

## 1. Topologi Partisi Ventoy & Aturan Saklar Fisik

```text
[ Flashdisk USB Fisik Teknisi (/dev/sdX) ]
      │
      ├─► Partisi 1 (exFAT/NTFS - Data & ISO)
      │     ├─► /ventoy/ventoy.json (Konfigurasi CLI & Bypass)
      │     ├─► /ISO/ (File ISO Windows, Linux, Rescue WinPE)
      │     ├─► /Drivers/ (.ventoyignore + Obat_VMD_Intel_Gen11_14/)
      │     └─► /Tools/ (.ventoyignore + Diagnostic Utilities)
      │
      └─► Partisi 2 (FAT/VTOYEFI - EFI Bootloader Murni)
            └─► [SEKRING: DILARANG DIUBAH / DIFORMAT]
```

- **Partisi 1**: Area kerja teknisi. Bebas diisi ISO dan folder utilitas.
- **Partisi 2**: Bootloader EFI Ventoy. Tidak boleh diutak-atik agar bootloader tidak korup.

---

## 2. Konfigurasi Baku `ventoy/ventoy.json` (CLI & Zero-Bloat Bypass)

Letakkan berkas konfigurasi di `/ventoy/ventoy.json` pada root Partisi 1:

```json
{
  "control": [
    { "VTOY_DEFAULT_MENU_MODE": "list" },
    { "VTOY_WIN11_BYPASS_CHECK": "1" },
    { "VTOY_WIN11_BYPASS_NRO": "1" }
  ],
  "theme": {
    "display_mode": "CLI"
  }
}
```

### Penjelasan Parameter Saklar:
1. `"theme.display_mode": "CLI"`
   * **Masalah**: Tema grafis resolusi tinggi sering lag, pecah, atau melar (*stretched aspect ratio*) pada monitor tabung servis jadul, laptop mini, atau layar LCD rasio 4:3.
   * **Solusi**: Mode CLI merender antarmuka teks murni standar VGA BIOS yang ringan, anti-lag, dan selalu tajam di layar manapun.
2. `"VTOY_DEFAULT_MENU_MODE": "list"`
   * Menyajikan daftar ISO dalam bentuk list berurutan abjad, bukan tree bertingkat yang membingungkan.
3. `"VTOY_WIN11_BYPASS_CHECK": "1"`
   * Otomatis mem-bypass pemeriksaan TPM 2.0, SecureBoot, CPU whitelist, dan batas minimal RAM 4GB saat instalasi Windows 11.
4. `"VTOY_WIN11_BYPASS_NRO": "1"`
   * Otomatis mem-bypass kewajiban koneksi internet (OOBE Network Requirement), memungkinkan teknisi membuat akun pengguna lokal (*offline user*) tanpa harus login akun Microsoft.

---

## 3. Injeksi Driver Intel RST VMD Gen 11-14 (`Drivers/Obat_VMD_*`)

### Mengapa SSD NVMe Sering Tidak Terbaca?
Pada laptop Intel Core Generasi 11 (Tiger Lake), 12 (Alder Lake), 13 (Raptor Lake), hingga 14 (Meteor Lake), kontroler penyimpanan Intel VMD (*Volume Management Device*) aktif secara default di level prosesor. Installer Windows standar tidak memiliki driver VMD bawaan, sehingga menampilkan pesan error:
> *"We couldn't find any drives. To get a storage driver, click Load driver."*

### SOP Penanganan Meja Servis:
1. Siapkan folder driver di Partisi 1 flashdisk:
   `Drivers/Obat_VMD_Intel_Gen11_14/`
2. Ekstrak berkas driver Intel Rapid Storage Technology (RST) ke folder tersebut:
   * `iaStorVD.sys`
   * `iaVD.inf` & `iaVD.cat`
   * `RstMwVmd.inf`
3. Saat installer Windows berhenti di layar partisi kosong:
   * Klik tombol **Load driver** ➔ **Browse**.
   * Navigasi ke drive USB ➔ `Drivers` ➔ `Obat_VMD_Intel_Gen11_14`.
   * Klik **OK** / **Next**.
   * Partisi SSD NVMe langsung terbaca seketika **tanpa perlu mengubah mode SATA/VMD di BIOS** (menghindari risiko merusak recovery OEM atau garansi pabrik).

---

## 4. Penyembunyian Folder Non-Boot via `.ventoyignore`

Ventoy secara otomatis memindai seluruh direktori di Partisi 1 untuk mencari file bootable. Jika teknisi menyimpan folder software, backup data pelanggan, atau koleksi driver, menu boot akan menjadi kotor dan proses booting melambat.

### Aturan Baku:
Letakkan berkas kosong bernama `.ventoyignore` di setiap folder non-boot:
```bash
# Tandai folder agar diabaikan oleh parser Ventoy
touch /media/user/Ventoy/Drivers/.ventoyignore
touch /media/user/Ventoy/Tools/.ventoyignore
touch /media/user/Ventoy/Backup/.ventoyignore
```

Ventoy akan langsung melewati folder-folder tersebut saat membangun menu boot.

---

## 5. Utilitas Otomatis (`scripts/ventoy_helper.py`)

Gunakan skrip pembantu bawaan modul untuk inisialisasi dan verifikasi cepat flashdisk:

### A. Inisialisasi Flashdisk Baru (1 Perintah)
```bash
# Buat struktur folder ISO, Drivers VMD, .ventoyignore, dan ventoy.json otomatis
python3 skills/ventoy-servicing-skill/scripts/ventoy_helper.py init /media/user/Ventoy
```

### B. Audit & Verifikasi Flashdisk yang Sudah Ada
```bash
# Periksa apakah ventoy.json valid, mode CLI aktif, dan .ventoyignore terpasang
python3 skills/ventoy-servicing-skill/scripts/ventoy_helper.py verify /media/user/Ventoy
```

---

## 6. Protokol Fail-Safe Sirkuit: Kernel Buffer Flushing (`sync`)

Sistem operasi Linux menggunakan *asynchronous write caching* untuk perangkat penyimpanan USB. Saat perintah penyalinan file ISO 5GB selesai di terminal, sebagian data masih berada di RAM kernel buffer dan belum selesai ditulis ke chip flashdisk.

### Prosedur Mutlak Sebelum Cabut Flashdisk:
```bash
# 1. Bilas seluruh cache kernel ke chip memori USB
sync

# 2. Lepaskan partisi secara bersih
sudo umount /dev/sdX1
```

> **PERINGATAN KERUSAKAN**: Mencabut flashdisk tanpa `sync` menyebabkan file ISO korup (*ghost image*), installer Windows error 0x8007025D saat dekompresi file, atau partisi exFAT rusak.
