---
name: hardware-boardview-skill
description: "SOP diagnosa motherboard meja servis: deteksi short circuit, injeksi tegangan aman 1A, penelusuran power rails (19V VIN, 3.3V/5V ALW, S3/S0 state), dan analisa skema PDF/boardview dengan bantuan AI vision."
---

# Hardware Boardview & Circuit Diagnostics Skill

SOP standar meja servis Megapass Intra Solusindo untuk diagnosa motherboard laptop dan PC desktop mati total, korsleting (short-to-ground), dan anomali sinyal daya.

---

## 1. Prinsip Utama: Sirkuit Sebelum Komponen

Sebelum mencurigai chipset atau IC controller utama (Super I/O, PCH, CPU):
- Jangan menyalakan board langsung dengan adaptor bawaan saat terjadi kondisi mati total.
- Selalu ukur resistansi ke ground (impedansi) pada seluruh induktor (koil) utama menggunakan multimeter digital (mode Ohm/Diode).
- Jika terdeteksi impedansi < 5 Ohm pada jalur non-core (3.3V atau 5V ALW), itu adalah **hard short**. Dilarang memberikan tegangan penuh 19V.

---

## 2. Prosedur Injeksi Tegangan Aman (Current Injection)

Metode pelacakan komponen panas (thermal tracking) tanpa merusak jalur tembaga PCB:

1. **Persiapan Lab Bench Power Supply**:
   - Atur voltase PSU ke nilai rendah: **1.0V hingga 1.2V**.
   - Atur pembatas arus (current limiter): **1.0A maksimal** pada tahap awal.
   - Jangan pernah menginjeksi 19V ke jalur sekunder (3.3V / 5V / 1.05V / VCC_CORE).
2. **Koneksi Titik Injeksi**:
   - Probe hitam (GND) dijepitkan ke ground kokoh motherboard (lubang baut / shield port USB).
   - Probe merah dihubungkan ke kapasitor keramik (MLCC) atau kaki induktor jalur yang mengalami short.
3. **Deteksi Panas**:
   - Sentuh motherboard dengan punggung jari atau gunakan thermal camera / cairan isopropyl alcohol (IPA 99%).
   - Komponen rusak (kapasitor bocor atau MOSFET jebol) akan mendidihkan alkohol dalam hitungan detik.
   - Ganti komponen yang teridentifikasi, lalu ukur ulang resistansi ke ground sebelum menyalakan mesin.

---

## 3. Urutan Penelusuran Power Rails (State S5 ke S0)

```
[ Adaptor 19V / Baterai ]
          ↓
[ DC-IN MOSFETs (Reverse Polarity & Current Sense Protection) ]
          ↓
[ VIN / B+ Main Power Rail (19V - 20V) ]
          ↓
[ 3.3V & 5V Always-On Converter (Standby IC) ]
    ├── 3.3V_ALW (Menghidupi Super I/O & SPI BIOS Flash)
    └── 5.0V_ALW
          ↓
[ Sinyal Power Button (PWRBTN#) ditekan ]
          ↓
[ Super I/O (EC) mengirim PM_PWRBTN# ke PCH/SoC ]
          ↓
[ PCH merespons: SLP_S5#, SLP_S4#, SLP_S3# HIGH ]
          ↓
[ Regulator RAM (1.2V DDR4 / 1.1V DDR5) & System Agent ON ]
          ↓
[ VCC_CORE PWM Controller Aktif → CPU Menerima Tegangan Inti ]
          ↓
[ VR_READY / ALL_SYS_PWRGD dikirim balik ke EC & CPU ]
          ↓
[ PLTRST# (Platform Reset) De-asserted → Display Tampil ]
```

---

## 4. Analisa Skema & Boardview dengan Copilot AI

Saat membaca skema PDF dan file boardview (.cad, .brd, .fz):
- Identifikasi nomor net power rail utama (contoh: `+3VALW`, `+5VALW`, `+VCC_CORE`, `EC_ON`).
- Cari IC pengendali tegangan terkait, periksa kondisi pin:
  - `VIN` (Tegangan masuk)
  - `EN` (Enable signal, biasanya 3.3V)
  - `VREG3` / `VREG5` (LDO internal output)
  - `PGOOD` (Power Good feedback)
- Jika `EN` ada namun output koil 0V dan resistansi normal, IC regulator rusak atau jalur bootstrap (kapasitor boot) open circuit.
