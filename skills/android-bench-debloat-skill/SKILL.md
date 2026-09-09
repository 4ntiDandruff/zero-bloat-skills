---
name: android-bench-debloat-skill
description: "Non-root ADB Android debloater SOP for workbench servicing: critical system whitelist, OEM package blacklist catalog (Samsung, Xiaomi, Oppo, Vivo), and batch removal automation."
---

# Android Bench Debloat Skill

Standard operating procedure for reviving laggy, storage-exhausted Android client devices without voiding hardware warranty or tripping financial Knox/SafetyNet triggers via root access.

---

## 1. Principle: Disable vs User 0 Uninstallation

- Running `pm uninstall -k --user 0 <package>` uninstalls the application from primary user space while keeping the signed factory APK in the read-only `/system` partition.
- If a customer requires an uninstalled service restored, it can be reinstituted immediately without downloading:
  ```bash
  adb shell cmd package install-existing <package>
  ```

---

## 2. Vital System Whitelist: DO NOT UNINSTALL

Removing these packages will induce permanent bootloops or catastrophic System UI crashes:
- `com.android.systemui` (System UI, notifications, status bar)
- `com.google.android.packageinstaller` / `com.android.packageinstaller`
- `com.android.settings` (Core system settings)
- `com.android.providers.telephony` (Telephony & SIM baseband services)
- `com.android.providers.media` / `com.android.providers.downloads`
- The default input method (keyboard) before configuring a verified replacement (Gboard).

---

## 3. OEM Package Blacklist Catalog

### Xiaomi / MIUI / HyperOS:
```bash
# System Telemetry & Ad Engines
adb shell pm uninstall -k --user 0 com.miui.analytics
adb shell pm uninstall -k --user 0 com.miui.msa.global
adb shell pm uninstall -k --user 0 com.xiaomi.mipicks

# Preinstalled Third-Party Bloat
adb shell pm uninstall -k --user 0 com.mi.globalbrowser
adb shell pm uninstall -k --user 0 com.facebook.katana
adb shell pm uninstall -k --user 0 com.facebook.services
```

### Samsung / One UI:
```bash
# Telemetry & Redundant Background Services
adb shell pm uninstall -k --user 0 com.samsung.android.bixby.agent
adb shell pm uninstall -k --user 0 com.samsung.android.bixby.service
adb shell pm uninstall -k --user 0 com.samsung.android.game.gamehome
adb shell pm uninstall -k --user 0 com.samsung.android.app.spage
```

---

## 4. Automated Batch Script Execution

Place target package identifiers into `debloat_list.txt`, then run:
```bash
while read -r package; do
    [[ -z "$package" || "$package" =~ ^# ]] && continue
    echo "[*] Removing package: $package"
    adb shell pm uninstall -k --user 0 "$package" || true
done < debloat_list.txt
```
