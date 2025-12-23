- This project is made in [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution)

# Downloading the CPU
1. Download and install [Logisim Evolution](https://github.com/logisim-evolution/logisim-evolution) using the guide provided in the Logisim Evolution repo
2. Download the latest version of the CPU and the INS_ROM (Instruction ROM) and place them together in a folder for easy access
3. Launch Logisim Evolution and use the File tab to open main.circ
4. It will say there's a missing library and ask you to select where the library is located, navigate to the folder where you placed the unzipped files and select 8-Bit-CPU-INS-ROM.circ
5. navigate to the "Computer" chip in the menu on the left by double clicking on it
6. load a properly formatted hex file such as any of the example scripts in /docs/examples/ in the repo into *BOTH* RAMs (This simulates dual-read memory)
7. toggle the clock and watch the cpu run, you can also use the "State" tab to see the current state of each register in the CPU

# Resetting the CPU
1. Toggle the "Clear" pin on
2. Toggle the "Clk" pin on, then off
3. Turn off the "Clear" pin
4. Run the program as normal