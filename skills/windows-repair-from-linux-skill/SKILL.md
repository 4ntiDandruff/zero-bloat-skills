---
name: windows-repair-from-linux-skill
description: "Windows OS triage and servicing from Linux: offline SAM password reset via chntpw, registry hive editing, BCD bootloader recovery, ddrescue bad-sector imaging, and BitLocker partition unlocks."
---

# Windows Bench Repair From Linux Skill

Operating instructions for diagnosing, salvaging, and repairing damaged Windows client installations directly from a Linux workstation or technician live environment.

---

## 1. NTFS Partitions & Windows Fast Startup

Windows 10 and 11 utilize Fast Startup (hybrid hibernation), leaving NTFS volumes in a dirty, locked state:

```bash
# Identify storage partition
lsblk -f

# Clear hibernation locks safely without data loss
sudo ntfsfix -d /dev/nvme0n1p3

# Mount volume cleanly
sudo mkdir -p /mnt/client_windows
sudo mount -t ntfs-3g -o remove_hiberfile /dev/nvme0n1p3 /mnt/client_windows
```

---

## 2. Offline Windows Local Password Reset (`chntpw`)

Reset locked local administrator or user passwords offline without modifying system files:

```bash
cd /mnt/client_windows/Windows/System32/config

# List local users stored in the SAM registry hive
sudo chntpw -l SAM

# Reset password for target user
sudo chntpw -u "TargetUser" SAM
# Menu options:
# 1 -> Clear (blank) user password
# 2 -> Unlock and enable account
# q -> Write hive changes and quit (confirm with 'y')
```

---

## 3. Bad Sector Disk Salvage (`ddrescue`)

Never use standard file managers or `cp` on failing drives; disk read errors will freeze the I/O bus:

```bash
# Image failing drive with persistent block logging
sudo ddrescue -d -r 2 /dev/sdb /home/michael/client_disk.img /home/michael/rescue.map

# Mount rescued raw image safely to recover client documents
sudo losetup -Pf /home/michael/client_disk.img
```

---

## 4. Unlocking BitLocker Partitions via Linux (`dislocker`)

When servicing BitLocker-encrypted drives where the client possesses the 48-digit recovery key:

```bash
sudo mkdir -p /mnt/bitlocker_raw /mnt/bitlocker_data

# Decrypt partition to a virtual block device
sudo dislocker /dev/nvme0n1p3 -p484848-XXXXXX-XXXXXX-... -- /mnt/bitlocker_raw

# Mount decrypted virtual volume read-only
sudo mount -t ntfs-3g -o ro /mnt/bitlocker_raw/dislocker-file /mnt/bitlocker_data
```
