---
name: eeprom-flashing-skill
description: "SPI BIOS/EEPROM (24/25 series) read, verification, and flashing SOP using CH341A programmers and flashrom, Intel ME Region cleanup, and native Rust Tauri v2 bindings."
---

# EEPROM Firmware Flashing Skill

Circuit-level operating procedures for reading, verifying, modifying, and programming SPI Flash EEPROM chips on computer motherboards.

---

## 1. Voltage Verification: 3.3V vs 5V (CH341A Hardware Mod)

- **Critical Pre-Check**: Stock black CH341A USB programmers frequently feature a PCB routing design flaw: data lines (MOSI, MISO, CLK, CS) carry 5.0V even when configured for 3.3V operation.
- Modern motherboard SPI Flash chips (Winbond, Macronix, GigaDevice 25QXX) operate at **3.3V** or **1.8V** (such as 25Q64FW series).
- Supplying 5.0V directly to 3.3V/1.8V silicon gates will cause irreversible semiconductor degradation.
- Always verify that the 1117-3.3V regulator output connects to CH341A pin 28 before attaching the SOIC8 test clip to the motherboard.

---

## 2. Dump Verification Procedure (Three-Pass Hash Rule)

Never erase or write to a chip before the original factory firmware dump is verified:

```bash
# 1. Read first dump
flashrom -p ch341a_spi -r dump_01.bin

# 2. Read second dump
flashrom -p ch341a_spi -r dump_02.bin

# 3. Compare MD5 checksums
md5sum dump_01.bin dump_02.bin
```

If hashes differ:
- Clean IC pins with a brush and 99% isopropyl alcohol to eliminate flux residue.
- Reseat the SOIC8 test clip ensuring firm, parallel contact on all pins.
- Repeat reading until three consecutive reads produce matching hashes.

---

## 3. Intel Management Engine Region Cleanup (Clean ME)

Common symptoms of an uncleaned or corrupted ME region after motherboard repair:
- System powers down automatically after precisely 30 minutes.
- CPU fan runs at 100% maximum RPM continuously from cold boot.
- Display initialization delay (black screen for 60-90 seconds before POST).

### Clean ME Procedure:
1. Extract the ME Region partition from the firmware dump using `me_cleaner` or Intel Flash Image Tool (FIT).
2. Substitute a clean, unconfigured repository CSE/ME region corresponding to the exact chipset SKU.
3. Rebuild the BIOS binary and write it back via `flashrom`:
   ```bash
   flashrom -p ch341a_spi -w bios_clean_me.bin
   ```

---

## 4. Native Rust Binding Architecture (Tauri v2)

For zero-bloat desktop flasher utilities:
- Use `libftdi` or `libusb` Rust bindings to interface directly with the CH341A USB controller.
- Stream byte progress through background worker threads to maintain smooth, non-blocking UI responsiveness.
