---
name: windows-repair-from-linux-skill
description: "Windows OS triage and servicing from Linux: atomic SAM/SYSTEM hive backup, offline password reset via chntpw, UEFI BCD bootloader repair, ddrescue bad-sector imaging, and BitLocker unlocks."
---

# Windows Bench Repair From Linux Skill

Operating instructions for diagnosing, salvaging, and repairing damaged Windows client installations directly from a Linux workstation or technician live USB environment.

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

## 2. Offline Password Reset with Atomic Registry Hive Backup

Modifying Windows registry hives directly with `chntpw` carries corruption risks if system shutdown was improper. Always create atomic timestamped backups before editing:

```bash
cd /mnt/client_windows/Windows/System32/config

# 1. Mandatory Atomic Backup Rule
sudo cp SAM SAM.bak_$(date +%Y%m%d_%H%M%S)
sudo cp SYSTEM SYSTEM.bak_$(date +%Y%m%d_%H%M%S)

# 2. List local users in SAM hive
sudo chntpw -l SAM

# 3. Reset password for target account
sudo chntpw -u "TargetUser" SAM
# Menu options:
# 1 -> Clear (blank) user password
# 2 -> Unlock and enable account
# q -> Write hive changes and quit (confirm with 'y')

# 4. Clean unmount to sync dirty buffers
cd /
sudo umount /mnt/client_windows
```

---

## 3. UEFI BCD Bootloader Reconstruction from Linux

When a client drive encounters `0xc000000e` or missing EFI boot configuration after cloning or partition resizing:

```bash
# 1. Identify EFI System Partition (ESP) - usually FAT32, ~100MB to 500MB
sudo fdisk -l /dev/nvme0n1
# Suppose /dev/nvme0n1p1 is EFI (FAT32) and /dev/nvme0n1p3 is Windows OS (NTFS)

# 2. Mount ESP and Windows OS
sudo mkdir -p /mnt/esp /mnt/win
sudo mount /dev/nvme0n1p1 /mnt/esp
sudo mount -t ntfs-3g /dev/nvme0n1p3 /mnt/win

# 3. Verify Bootloader Files Exist
# Windows boot manager should live at: /mnt/esp/EFI/Microsoft/Boot/bootmgfw.efi
ls -la /mnt/esp/EFI/Microsoft/Boot/

# If missing, copy clean EFI binaries directly from Windows system:
sudo mkdir -p /mnt/esp/EFI/Microsoft/Boot
sudo cp -r /mnt/win/Windows/Boot/EFI/* /mnt/esp/EFI/Microsoft/Boot/

# 4. Register UEFI NVRAM Boot Entry via Linux
sudo efibootmgr -c -d /dev/nvme0n1 -p 1 -L "Windows Boot Manager" -l "\\EFI\\Microsoft\\Boot\\bootmgfw.efi"

# Verify active boot order
sudo efibootmgr -v
```

---

## 4. Bad Sector Disk Salvage (`ddrescue`)

Never use standard file managers or `cp` on failing drives; hardware read timeouts will freeze the SATA/NVMe bus:

```bash
# Image failing drive with persistent log map for resume support
sudo ddrescue -d -r 2 /dev/sdb /home/michael/client_disk.img /home/michael/rescue.map

# Mount rescued raw image safely to recover client documents
sudo losetup -Pf /home/michael/client_disk.img
sudo mount -t ntfs-3g -o ro /dev/loop0p3 /mnt/rescued_data
```

---

## 5. Unlocking BitLocker Partitions via Linux (`dislocker`)

When servicing BitLocker-encrypted drives where the client possesses the 48-digit recovery key:

```bash
sudo mkdir -p /mnt/bitlocker_raw /mnt/bitlocker_data

# Decrypt partition to a virtual block device
sudo dislocker /dev/nvme0n1p3 -p484848-XXXXXX-XXXXXX-... -- /mnt/bitlocker_raw

# Mount decrypted virtual volume read-only
sudo mount -t ntfs-3g -o ro /mnt/bitlocker_raw/dislocker-file /mnt/bitlocker_data
```
