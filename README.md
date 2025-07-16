# 🎮 lockPuzzle

A fully custom retro-style game developed in low-level C and assembly, designed to run on an **RISC-V CPU implemented on the DE1-SoC FPGA board** as the CPU. This project interfaces directly with hardware components such as VGA, PS/2 keyboard, audio output, and a hardware timer. This project demonstrates hands-on embedded systems and digital design concepts.

---

## 🛠️ Features

- **Low-level C and Assembly Programming**  
  Written with tight control over memory and timing, targeting the FPGA’s custom CPU for efficient execution.

- **VGA Graphics Output**  
  The game renders visuals frame-by-frame to a VGA monitor, implementing pixel-based graphics and timing control using hardware-mapped I/O.

- **PS/2 Keyboard Input**  
  Real-time input handling via PS/2 interface allows responsive control using physical keys.

- **Audio Output**  
  Custom audio samples are stored and played through a speaker using DAC interfacing, adding immersion to gameplay.

- **Hardware Timer Integration**  
  A 100Hz hardware timer controls game timing, delays, and frame updates with precise granularity.

- **Game Logic and Mechanics**  
  Implements a fully playable retro game with interactive elements and real-time gameplay. Features smooth animation, input-based interactions, and retro-style visuals.

---

## 💡 Technologies Used

- **DE1-SoC FPGA Board** – used to implement a soft-core **RISC-V processor** and custom memory-mapped peripherals  
- **Custom RISC-V CPU** – executes game logic using compiled C and assembly code  
- **C and RISC-V Assembly** – for direct low-level programming and control  
- **VGA Protocol** – for visual rendering  
- **PS/2 Protocol** – for keyboard input  
- **Audio Sampling** – for simple sound effects and background audio
- **Hardware Timer** – for consistent timing and animation pacing  
- **Direct Hardware Access** – using memory-mapped I/O

---

## 🧪 Demo and Testing

You can test and play the game without hardware by running  `main.c` on [**CPulator**](https://cpulator.01xz.net/?sys=rv32-de1soc), an online MIPS CPU simulator that supports memory-mapped I/O.

1. Go to **https://cpulator.01xz.net/?sys=rv32-de1soc**
2. Select **File** -> **Open...** and upload `main.c`
3. Change the language to **C**
4. Click **Compile & Load**
5. Press **Continue** to start the game
---

## 📚 Learning Outcomes

This project was a hands-on journey into:
- Embedded systems and hardware-software co-design
- FPGA-based CPU development and peripheral interfacing
- Hardware interfacing with real-world protocols
- Game development at the bare-metal level

