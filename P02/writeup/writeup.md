# Universal Culling System
## Problem Description
As the higher-ups at StarMount gave you more exhaustive system maps to test your Interstellar Positioning System (IPS) against, you began to realize a slight issue with the design; the Univers is kinda big. Well, not *kinda* big, but larger than our observable scope. Due to this, the IPS seems to be trying to build a data structure containing literally *the entire Universe*, and unsurprisingly, is taking forever to fully process. In order to counteract this issue, you've decided that you want to limit the systems it can pull into memory by the sectors that the ship will possibly travel through in order to make it to its destination.

## Definitions
A sector (at least in this context) will be considered a 5x5x5 lightyear cube of space, starting at the origin and branching out from there. Given a starting system, an ending system, and a list of systems, it's your job to root out all sectors that are not on a direct path between your sector and the destination sector. A direct path should be considered the line directly between the two systems, with a rounded cylinder around the direct path with a radius of 2.5 lightyears (half a sector's breadth) on all sides. The company realizes that this could cut off possible routes that start by going away from the destination, and like Capcom promised with Street Fighter V ~250 years ago, has promised to resolve this issue in a later release.

## Input Specifications
The first line of the input file will contain the name of the current system and the name of the destination system. Every subsequent line (of which there will be one per system) will contain the system name and decimal values of the X, Y, and Z coordinates (in that order, to four decimal places).

So, if you wanted to get from Blackmane to Cambria and also had Ariel and Alliance in your map, input would look like:
```
Blackmane Cambria
Blackmane 136.8153 1898.6918 1617.6132
Ariel 139.9871 1893.4698 1611.1568
Alliance 142.6879 1891.1689 1612.9875
Cambria 148.6897 1892.4189 1605.1564
```

## Output Specifications
You should print the names of all sectors that should be loaded into the IPS' pathfinding system, in alphabetical order, one entry per line. So, the output for the given example input would be:
```
Alliance
Blackmane
Cambria
```

If you run across a system whose endpoint is in the same sector as the starting point (or is the same as the starting point), print out all systems in sectors within range of said starting point. Look in the `examples` directory to see a couple more cases!
