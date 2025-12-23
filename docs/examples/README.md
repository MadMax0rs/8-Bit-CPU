# Compilation Process

Typically, the compilation process from a windows executable would look like:  
$.asm \xrightarrow{assembling} .obj \xrightarrow{linking} .exe$

Similarly, for this CPU it looks like:  
$.asm \xrightarrow{assembling} .bin \xrightarrow{formatting} .hex$

## What does this mean?
1. asm file &mdash; Your assembly script
2. bin file &mdash; The raw byte-code of your script
3. hex file &mdash; The file format required by logisim-evolution