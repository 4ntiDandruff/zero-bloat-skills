---
name: hardware-boardview-skill
description: "Motherboard repair workbench SOP: short circuit detection, safe 1A current injection, power rails sequencing (19V VIN, 3.3V/5V ALW, S3/S0 states), and AI-assisted boardview/schematic analysis."
---

# Hardware Boardview & Circuit Diagnostics Skill

Standard operating procedure from the Megapass Intra Solusindo hardware repair bench for diagnosing dead computer motherboards, short-to-ground conditions, and power rail anomalies.

---

## 1. Core Principle: Circuit Integrity First

Before suspecting primary ICs or controllers (Super I/O, PCH, SoC, CPU):
- Never power on a dead board directly using an OEM charger without preliminary tests.
- Always measure resistance to ground (impedance) across all primary inductors (coils) with a digital multimeter in resistance or diode mode.
- If impedance reads < 5 Ohms on secondary/always-on rails (3.3V or 5V ALW), a **hard short** is present. Connecting a 19V supply under this condition will destroy silicon layers.

---

## 2. Safe Current Injection Procedure

Safe thermal tracking method without burning internal PCB copper planes:

1. **Bench Power Supply Calibration**:
   - Set supply voltage low: **1.0V to 1.2V**.
   - Set current limiter: **1.0A maximum** during initial probing.
   - Never inject 19V directly into secondary lines (3.3V, 5V, 1.05V, or VCC_CORE).
2. **Connection Points**:
   - Connect black probe (GND) firmly to chassis ground (screw ring or USB shield).
   - Connect red probe to the shorted inductor pad or ceramic capacitor (MLCC).
3. **Thermal Localisation**:
   - Inspect components by touch, thermal imager, or pure isopropyl alcohol (IPA 99%).
   - The defective component (shorted bypass capacitor or punched high-side MOSFET) will boil off alcohol in seconds.
   - Desolder the faulty component and remeasure ground impedance before applying power.

---

## 3. Power Rails Sequencing (S5 to S0 State Flow)

```
[ 19V DC-IN Adapter / Battery Rail ]
                 ↓
[ DC-IN Dual MOSFETs (Reverse Polarity & Current Sense Protection) ]
                 ↓
[ VIN / B+ Main System Rail (19V - 20V) ]
                 ↓
[ 3.3V & 5.0V Always-On PWM Converter (Standby IC) ]
    ├── 3.3V_ALW (Powers Super I/O & SPI BIOS Flash)
    └── 5.0V_ALW
                 ↓
[ Power Button Signal (PWRBTN#) Depressed ]
                 ↓
[ Super I/O (EC) Asserts PM_PWRBTN# to PCH/SoC ]
                 ↓
[ PCH Responds: SLP_S5#, SLP_S4#, SLP_S3# Go HIGH ]
                 ↓
[ Memory Buck Converter (1.2V DDR4 / 1.1V DDR5) & System Agent Enabled ]
                 ↓
[ VCC_CORE Multiphase PWM Controller Activated -> CPU Receives Core Voltage ]
                 ↓
[ VR_READY / ALL_SYS_PWRGD Feedback Delivered to EC & CPU ]
                 ↓
[ PLTRST# (Platform Reset) De-asserted -> Display Initialized ]
```

---

## 4. Schematic & Boardview AI Copilot Analysis

When inspecting PDF schematics alongside boardview files (.cad, .brd, .fz):
- Identify primary net names (e.g., `+3VALW`, `+5VALW`, `+VCC_CORE`, `EC_ON`).
- Locate the corresponding voltage regulator IC and evaluate pin states:
  - `VIN` (Input voltage present)
  - `EN` (Enable logic HIGH, typically 3.3V)
  - `VREG3` / `VREG5` (Internal linear LDO outputs)
  - `PGOOD` (Power Good status output)
- If `EN` is HIGH but coil output remains 0V with normal ground impedance, the IC or its bootstrap capacitor is defective.
