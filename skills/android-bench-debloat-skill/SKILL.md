---
name: android-bench-debloat-skill
description: "SOP pembersihan bloatware Android konsumen meja servis via ADB tanpa root: whitelist sistem vital, katalog blacklist vendor (Samsung, Xiaomi, Oppo, Vivo), dan batch automation."
---

# Android Bench Debloat Skill

Panduan meja servis untuk merevitalisasi ponsel Android konsumen yang lemot, memori penuh, dan terbebani aplikasi sistem pihak ketiga (bloatware) tanpa memerlukan akses root yang membatalkan garansi atau memicu deteksi keamanan perbankan.

---

## 1. Prinsip: Disable vs Uninstall User 0

- Perintah `pm uninstall -k --user 0 <package>` menghapus aplikasi dari ruang kerja pengguna utama, namun file APK asli tetap tersimpan aman di partisi `/system` read-only.
- Jika pengguna membutuhkan kembali aplikasi tersebut atau terjadi kendala fungsionalitas, aplikasi dapat dipulihkan instan tanpa download ulang:
  ```bash
  adb shell cmd package install-existing <package>
  ```

---

## 2. Whitelist Kritis: DILARANG Dihapus

Menghapus paket-paket ini akan mengakibatkan *bootloop* atau sistem crash permanen:
- `com.android.systemui` (System UI / status bar)
- `com.google.android.packageinstaller` / `com.android.packageinstaller`
- `com.android.settings` (Menu Pengaturan)
- `com.android.providers.telephony` (Fungsi SMS & Jaringan SIM)
- `com.android.providers.media` / `com.android.providers.downloads`
- Paket keyboard default sebelum memasang keyboard pengganti (Gboard).

---

## 3. Blacklist Bloatware per Vendor

### Xiaomi / MIUI / HyperOS:
```bash
# Iklan sistem (Analytics & MSA)
adb shell pm uninstall -k --user 0 com.miui.analytics
adb shell pm uninstall -k --user 0 com.miui.msa.global
adb shell pm uninstall -k --user 0 com.xiaomi.mipicks

# Aplikasi bloatware
adb shell pm uninstall -k --user 0 com.mi.globalbrowser
adb shell pm uninstall -k --user 0 com.facebook.katana
adb shell pm uninstall -k --user 0 com.facebook.services
```

### Samsung / One UI:
```bash
# Layanan Bixby & Iklan
adb shell pm uninstall -k --user 0 com.samsung.android.bixby.agent
adb shell pm uninstall -k --user 0 com.samsung.android.bixby.service
adb shell pm uninstall -k --user 0 com.samsung.android.game.gamehome
adb shell pm uninstall -k --user 0 com.samsung.android.app.spage
```

---

## 4. Skrip Eksekusi Otomatis Batch

Simpan daftar paket target ke file `debloat_list.txt`, lalu eksekusi satu baris:
```bash
while read -r package; do
    [[ -z "$package" || "$package" =~ ^# ]] && continue
    echo "[*] Menghapus: $package"
    adb shell pm uninstall -k --user 0 "$package" || true
done < debloat_list.txt
```
