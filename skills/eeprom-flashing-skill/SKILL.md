---
name: eeprom-flashing-skill
description: "SPI BIOS/EEPROM (24/25 series) firmware programming SOP: 1.8V adapter level-shifting, status register write-protect unlock, three-pass dump verification, Intel Clean ME, and flashrom automation."
---

# EEPROM Firmware Flashing Skill

Circuit-level operating procedures for reading, verifying, modifying, and programming SPI Flash EEPROM chips on computer motherboards, preventing silicon overvoltage burnout and register write-protect failures.

---

## 1. Operating Voltage: 3.3V vs 1.8V Adapter Level-Shifter

Supplying 3.3V or 5.0V to a low-voltage 1.8V SPI chip will destroy internal semiconductor gate oxides instantly:

### Voltage Classification Checklist:
| Voltage Class | Common Chip Markings | Mandatory Hardware Setup |
|---|---|---|
| **Standard 3.3V** | `25Q32BV`, `25Q64BV`, `25Q128FV`, `MX25L6406E` | Direct CH341A socket (Pin 28 3.3V Mod verified) |
| **Low-Voltage 1.8V** | `25Q64FW`, `25Q64JW`, `25Q128FW`, `IS25WP064` | **MANDATORY: 1.8V Level-Shifter Adapter** between CH341A and chip |

### The Stock CH341A 5V Line Flaw:
- Stock black CH341A USB programmers route 5.0V to data lines (MOSI, MISO, CLK, CS) even with the 3.3V jumper set.
- **Mandatory Mod**: Lift Pin 28 of the CH341A IC from the PCB and bridge it directly to the 3.3V output pin of the AMS1117 regulator.

---

## 2. In-Circuit Probing vs Hot-Air Desoldering

In-circuit flashing with SOIC8 test clips often fails or produces corrupted hashes because motherboard rail impedance loads down SPI signals:

1. **Backpowering Hazard**: The 3.3V VCC line from the programmer will backfeed into the motherboard's `+3VALW` rail, attempting to power the entire Super I/O, PCH, and standby LEDs.
2. **SOP Decision Tree**:
   - Disconnect main charger and remove RTC CMOS battery (CR2032).
   - If `flashrom` fails to detect the chip identifier (`0x000000` or `0xffffff`), lift **Pin 8 (VCC)** of the SOIC8 chip using a fine soldering tip to isolate power, OR
   - Desolder the chip using a hot air rework station (350°C, air 4) and place it into a dedicated ZIF socket.

---

## 3. Dump Verification (Three-Pass Hash Rule)

Never erase or write until the factory dump is bit-for-bit verified:

```bash
# 1. Read dump 1
flashrom -p ch341a_spi -r dump_01.bin

# 2. Read dump 2
flashrom -p ch341a_spi -r dump_02.bin

# 3. Compare MD5 checksums
md5sum dump_01.bin dump_02.bin
```

If hashes differ:
- Clean IC pins with 99% Isopropyl Alcohol (IPA) to eliminate oxidation and flux residue.
- Reseat the SOIC8 test clip with firm, parallel contact.
- Repeat until three consecutive dumps produce matching hashes before proceeding.

---

## 4. Unlocking Status Register Write-Protect (SR1/BP0/BP1)

Many OEM firmware images (Lenovo, HP, Dell) enable hardware write-protection bits in the SPI Status Register. When protected, `flashrom -w` fails at block verification:

```bash
# Check status register lock bits
flashrom -p ch341a_spi --wp-status

# Clear write-protection bits permanently before flashing
flashrom -p ch341a_spi --wp-disable

# Write clean firmware binary
flashrom -p ch341a_spi -w bios_clean.bin
```

---

## 5. Intel Management Engine Region Cleanup (Clean ME)

Common symptoms of corrupted or uninitialized ME regions after motherboard replacement or chip swap:
- Motherboard shuts down after exactly **30 minutes**.
- CPU cooling fan runs at continuous 100% full blast from cold boot.
- 60–90 second delay before display initializes.

### Clean ME Procedure:
1. Extract ME region partition from factory dump using `me_cleaner` or Intel Flash Image Tool (FIT).
2. Substitute a clean, unconfigured repository CSE/ME region corresponding to the exact chipset SKU.
3. Rebuild the final binary and flash via `flashrom`:
   ```bash
   flashrom -p ch341a_spi -w bios_clean_me.bin
   ```
