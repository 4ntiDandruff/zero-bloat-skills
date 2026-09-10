---
name: hardware-boardview-skill
description: "Motherboard repair workbench SOP: short circuit detection, high-side MOSFET punch-through verification, safe voltage injection limits per rail, power rails sequencing (19V VIN to S0), and schematic/boardview analysis."
---

# Hardware Boardview & Circuit Diagnostics Skill

Standard operating procedure from the Megapass Intra Solusindo hardware repair bench for diagnosing dead motherboards, short-to-ground conditions, power rail sequencing failures, and silicon punch-through hazards.

---

## 1. Circuit Integrity & Impedance Baseline

Before applying DC adapter power or suspecting primary controllers (Super I/O, PCH, SoC, CPU):
1. **Never plug an OEM charger into a dead board** without taking passive cold measurements first.
2. Measure resistance to ground (impedance) across all primary buck converter coils in 200Ω resistance mode:
   - **Main System Rail (`VIN / B+`)**: Must read >100kΩ. If 0Ω–5Ω, a high-side MOSFET or primary filtering MLCC is dead short.
   - **Always-On (`+3VALW` / `+5VALW`)**: Must read >50Ω (typically 1kΩ–50kΩ). Under 5Ω indicates a catastrophic secondary short.
   - **RAM Rail (`+1.2V_DDR4` / `+1.1V_DDR5`)**: Typically 100Ω–500Ω.
   - **PCH / System Agent (`+1.05V_PCH`)**: Typically 20Ω–80Ω.
   - **CPU Core (`+VCC_CORE`) & GPU Core (`+VCC_GT` / `VGPU`)**: **Normal baseline is ultra-low: 0.2Ω to 2.5Ω**. Do NOT misdiagnose this normal semiconductor resistance as a short circuit!

---

## 2. High-Side MOSFET Punch-Through Verification (CRITICAL HAZARD)

A common fatal mistake is injecting voltage into a coil while its High-Side (upper) MOSFET is internally shorted between Drain and Source:

```
[ 19V VIN / B+ Main Rail ]
            │
       [ Drain (D) ]
      ┌─────┴─────┐
      │ High-Side │  <-- IF SHORTED (D-to-S = 0Ω):
      │  MOSFET   │      Injecting 1V-3V on coil can backfeed or
      └─────┬─────┘      leak 19V directly into the CPU core!
      [ Source (S) ]
            │
            ├─────────────── [ Buck Coil (Inductor) ] ───► [ Sensitive CPU / Core Silicon ]
            │
      [ Drain (D) ]
      ┌─────┴─────┐
      │ Low-Side  │
      │  MOSFET   │
      └─────┬─────┘
      [ Source (S) ]
            │
         [ GND ]
```

### Mandatory Pre-Injection Gate:
- Always measure resistance between **19V VIN pad** (Drain) and the **Phase/Coil pad** (Source of High-Side MOSFET).
- If resistance reads **0Ω (shorted)**, **DO NOT INJECT VOLTAGE**. Replace the punctured High-Side MOSFET first. Injecting current will send voltage straight across the rail into silicon dies.

---

## 3. Safe Current Injection Protocol & Voltage Ceilings

When an actual hard short is isolated (e.g. 0.0Ω on 3VALW or 19V VIN), localize the defective bypass capacitor or diode safely:

### Strict Voltage Limits Per Rail:
| Target Power Rail | Normal Voltage | Maximum Safe Injection Voltage | Maximum Current Cap |
|---|---|---|---|
| **VIN / B+ Main Rail** | 19.0V - 20.0V | **1.0V - 2.0V** (start low!) | 1.0A - 2.0A |
| **+3VALW Standby** | 3.3V | **1.2V maximum** | 1.0A |
| **+5VALW Standby** | 5.0V | **1.5V maximum** | 1.0A |
| **+1.05V PCH / SoC** | 1.05V | **0.8V maximum** | 1.0A |
| **+VCC_CORE / VGPU** | 0.8V - 1.2V | **0.8V maximum** (Never >0.8V!) | 1.0A - 1.5A |

### Injection Execution:
1. Ground black probe firmly to a motherboard screw ring or USB casing ground shield.
2. Solder red injection wire directly to the output pad of the shorted inductor (or positive terminal of MLCC filter). Never hold probes loosely by hand.
3. Apply 99% pure Isopropyl Alcohol (IPA) across the suspected motherboard zone.
4. Switch DC power supply output on at 1.0A cap. The shorted MLCC or punctured semiconductor will instantly boil/evaporate the alcohol in 1-3 seconds.
5. Desolder the defective component, verify cold impedance returns to normal baseline (>50Ω or megaohms), then test rail voltages.

---

## 4. Power Rails Sequencing (S5 to S0 State Flow)

Step-by-step logic gate progression required for motherboard POST:

```
[ 19V DC-IN Adapter / Battery Rail ]
                 ↓
[ DC-IN Dual MOSFETs (Reverse Polarity & Current Sense Resistor PR_B+) ]
                 ↓
[ VIN / B+ Main System Rail (19V - 20V) Stabilized ]
                 ↓
[ 3.3V & 5.0V Always-On PWM Converter (Standby IC) ]
    ├── 3.3V_ALW (Powers Super I/O / EC & SPI BIOS Flash Pin 8)
    └── 5.0V_ALW
                 ↓
[ EC Reads BIOS Firmware & Asserts EC_ON / AC_PRESENT ]
                 ↓
[ Power Button Signal (PWRBTN#) Depressed (3.3V Pulled Down to 0V Temporarily) ]
                 ↓
[ Super I/O Asserts PM_PWRBTN# to PCH/SoC ]
                 ↓
[ PCH Releases Sleep Signals: SLP_S5#, SLP_S4#, SLP_S3# Go HIGH (3.3V) ]
                 ↓
[ RAM Converter (1.2V DDR4 / 1.1V DDR5) & 1.05V PCH Rails Enable ]
                 ↓
[ VCC_CORE Multiphase PWM Controller Activated -> CPU Receives Core Voltage ]
                 ↓
[ VR_READY / ALL_SYS_PWRGD Feedback Delivered to EC & CPU ]
                 ↓
[ PLTRST# (Platform Reset) De-asserted (3.3V) -> Clock Active -> Display Initialized ]
```

---

## 5. Schematic & Boardview AI Copilot Analysis

When cross-referencing PDF schematics alongside boardview viewers (OpenBoardView / `.cad` / `.brd` / `.fz`):
1. **Trace Net Names**:
   - `VIN` / `B+` / `VCC_IN` (Primary high-voltage rail)
   - `+3VALW`, `+5VALW`, `+3VS5`, `+3VS3` (Standby and switched rails)
   - `EC_ON`, `ALL_SYS_PWRGD`, `PGOOD` (Enables and feedback gates)
2. **IC Pin State Evaluation**:
   - `VIN`: Operating input present.
   - `EN`: High logic level (typically 3.3V or voltage-divided from VIN).
   - `VREG3` / `VREG5`: Linear internal LDO references active.
   - `BOOT` (Bootstrap Pin): Must measure ~5V higher than coil voltage during switching. If boot diode or capacitor is leaky, high-side MOSFET cannot fully saturate, resulting in 0V output.
3. If `EN` is active, `VIN` present, and impedance is normal, but coil voltage stays 0V, replace the bootstrap capacitor and PWM controller.
