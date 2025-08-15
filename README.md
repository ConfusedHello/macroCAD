# MacroCAD
My own macropad made for CAD! Made for Hackclub's Highway/Hackpad event.

<img src="/assets/buildcomplete.jpg" alt="Hackpad" width=75%></img>

For this macropad, there is a function row at the bottom to switch "layers", ie. extra buttons!!


## The PCB
The PCB was designed entirely in KiCad. Here's an image of the schematic.
![Image of the macropad's schematic](/assets/Schematic.png)

And an image of the PCB!
![Image of the macropad's pcb](/assets/PCB.png)
<img src="/assets/pcbsoldered.jpg" alt="Hackpad" width=75%></img>

## The Case
First time using Fusion360! Went pretty well actually. Here's what we went with.

Started off by deciding on some dimensions
![Hand drawn dimensions of case](/assets/Case_Draft.png)

And moved onto creating a sketch
![Sketch of the baseplate](/assets/Case_Dimensions.png)

Then a bit more work later, the final case
![Cross section of the case](/assets/Case_Crosssection.png)

Final case design (render coming soon!)
![Image of the macropad](/assets/Case_Model.png)


## Bill of materials
| Component                                 | Quantity | Aliexpress |
|-------------------------------------------|----------|------------|
| 2L PCB (JLCPCB with cheap shipping)       | 1        | $3.49      |
| SMD Seeed Studio XIAO RP2040              | 1        | $5.64      |
| Gateron Milky Yellows Cherry MX Switches  | 10       | ~$3.86     |
| CherryMX 1.00u Kailh Sockets              | 10       | $2.89      |
| 1N4148W Diodes (SOD-123)                  | 10       | $1.09      |
| Brass M2 Screws (approx 5mm)              | 10       | $0.97      |
| M2 Heat inserts (approx 3mm)              | 10       | $0.97      |


## Acknowledgements
- Matteo Spinelli's [Anatomy of a keyboard](https://matt3o.com/anatomy-of-a-keyboard/) for the plate thickness and hole dimensions
- MX Cherry switches footprint from [daprice/keyswitches.pretty](https://github.com/daprice/keyswitches.pretty)
