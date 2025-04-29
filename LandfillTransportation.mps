NAME Landfill Transportation
ROWS
 N  OBJ
 L  center[NewYork]
 L  center[NewJersey]
 E  landfill[C1]
 E  landfill[C2]
 E  landfill[C3]
 E  landfill[C4]
 E  landfill[C5]
 E  landfill[C6]
 E  landfill[C7]
 E  depot[Bronx]
 E  depot[Brooklyn]
 E  depot[Queens]
 E  depot[StatenIsland]
 L  depot_capacity[Bronx]
 L  depot_capacity[Brooklyn]
 L  depot_capacity[Queens]
 L  depot_capacity[StatenIsland]
COLUMNS
    flow[NewYork,Bronx]  OBJ       0.7
    flow[NewYork,Bronx]  center[NewYork]  1
    flow[NewYork,Bronx]  depot[Bronx]  -1
    flow[NewYork,Bronx]  depot_capacity[Bronx]  1
    flow[NewYork,Brooklyn]  OBJ       0.7
    flow[NewYork,Brooklyn]  center[NewYork]  1
    flow[NewYork,Brooklyn]  depot[Brooklyn]  -1
    flow[NewYork,Brooklyn]  depot_capacity[Brooklyn]  1
    flow[NewYork,Queens]  OBJ       1.2
    flow[NewYork,Queens]  center[NewYork]  1
    flow[NewYork,Queens]  depot[Queens]  -1
    flow[NewYork,Queens]  depot_capacity[Queens]  1
    flow[NewYork,StatenIsland]  OBJ       0.4
    flow[NewYork,StatenIsland]  center[NewYork]  1
    flow[NewYork,StatenIsland]  depot[StatenIsland]  -1
    flow[NewYork,StatenIsland]  depot_capacity[StatenIsland]  1
    flow[NewYork,C1]  OBJ       1.2
    flow[NewYork,C1]  center[NewYork]  1
    flow[NewYork,C1]  landfill[C1]  1
    flow[NewYork,C3]  OBJ       1.7
    flow[NewYork,C3]  center[NewYork]  1
    flow[NewYork,C3]  landfill[C3]  1
    flow[NewYork,C4]  OBJ       2.2
    flow[NewYork,C4]  center[NewYork]  1
    flow[NewYork,C4]  landfill[C4]  1
    flow[NewYork,C6]  OBJ       1.2
    flow[NewYork,C6]  center[NewYork]  1
    flow[NewYork,C6]  landfill[C6]  1
    flow[NewYork,C7]  OBJ       2
    flow[NewYork,C7]  center[NewYork]  1
    flow[NewYork,C7]  landfill[C7]  1
    flow[NewJersey,Brooklyn]  OBJ       0.5
    flow[NewJersey,Brooklyn]  center[NewJersey]  1
    flow[NewJersey,Brooklyn]  depot[Brooklyn]  -1
    flow[NewJersey,Brooklyn]  depot_capacity[Brooklyn]  1
    flow[NewJersey,Queens]  OBJ       0.7
    flow[NewJersey,Queens]  center[NewJersey]  1
    flow[NewJersey,Queens]  depot[Queens]  -1
    flow[NewJersey,Queens]  depot_capacity[Queens]  1
    flow[NewJersey,StatenIsland]  OBJ       0.4
    flow[NewJersey,StatenIsland]  center[NewJersey]  1
    flow[NewJersey,StatenIsland]  depot[StatenIsland]  -1
    flow[NewJersey,StatenIsland]  depot_capacity[StatenIsland]  1
    flow[NewJersey,C1]  OBJ       2.2
    flow[NewJersey,C1]  center[NewJersey]  1
    flow[NewJersey,C1]  landfill[C1]  1
    flow[NewJersey,C7]  OBJ       1.8
    flow[NewJersey,C7]  center[NewJersey]  1
    flow[NewJersey,C7]  landfill[C7]  1
    flow[Bronx,C2]  OBJ       1.7
    flow[Bronx,C2]  landfill[C2]  1
    flow[Bronx,C2]  depot[Bronx]  1
    flow[Bronx,C3]  OBJ       0.7
    flow[Bronx,C3]  landfill[C3]  1
    flow[Bronx,C3]  depot[Bronx]  1
    flow[Bronx,C4]  OBJ       1.7
    flow[Bronx,C4]  landfill[C4]  1
    flow[Bronx,C4]  depot[Bronx]  1
    flow[Bronx,C6]  OBJ       1.2
    flow[Bronx,C6]  landfill[C6]  1
    flow[Bronx,C6]  depot[Bronx]  1
    flow[Bronx,C7]  OBJ       1.9
    flow[Bronx,C7]  landfill[C7]  1
    flow[Bronx,C7]  depot[Bronx]  1
    flow[Brooklyn,C1]  OBJ       1.2
    flow[Brooklyn,C1]  landfill[C1]  1
    flow[Brooklyn,C1]  depot[Brooklyn]  1
    flow[Brooklyn,C2]  OBJ       0.7
    flow[Brooklyn,C2]  landfill[C2]  1
    flow[Brooklyn,C2]  depot[Brooklyn]  1
    flow[Brooklyn,C3]  OBJ       0.7
    flow[Brooklyn,C3]  landfill[C3]  1
    flow[Brooklyn,C3]  depot[Brooklyn]  1
    flow[Brooklyn,C4]  OBJ       1.2
    flow[Brooklyn,C4]  landfill[C4]  1
    flow[Brooklyn,C4]  depot[Brooklyn]  1
    flow[Brooklyn,C5]  OBJ       0.7
    flow[Brooklyn,C5]  landfill[C5]  1
    flow[Brooklyn,C5]  depot[Brooklyn]  1
    flow[Brooklyn,C7]  OBJ       1.5
    flow[Brooklyn,C7]  landfill[C7]  1
    flow[Brooklyn,C7]  depot[Brooklyn]  1
    flow[Queens,C2]  OBJ       1.7
    flow[Queens,C2]  landfill[C2]  1
    flow[Queens,C2]  depot[Queens]  1
    flow[Queens,C3]  OBJ       2.2
    flow[Queens,C3]  landfill[C3]  1
    flow[Queens,C3]  depot[Queens]  1
    flow[Queens,C5]  OBJ       0.7
    flow[Queens,C5]  landfill[C5]  1
    flow[Queens,C5]  depot[Queens]  1
    flow[Queens,C6]  OBJ       1.7
    flow[Queens,C6]  landfill[C6]  1
    flow[Queens,C6]  depot[Queens]  1
    flow[Queens,C7]  OBJ       1.6
    flow[Queens,C7]  landfill[C7]  1
    flow[Queens,C7]  depot[Queens]  1
    flow[StatenIsland,C3]  OBJ       0.4
    flow[StatenIsland,C3]  landfill[C3]  1
    flow[StatenIsland,C3]  depot[StatenIsland]  1
    flow[StatenIsland,C4]  OBJ       1.7
    flow[StatenIsland,C4]  landfill[C4]  1
    flow[StatenIsland,C4]  depot[StatenIsland]  1
    flow[StatenIsland,C5]  OBJ       0.7
    flow[StatenIsland,C5]  landfill[C5]  1
    flow[StatenIsland,C5]  depot[StatenIsland]  1
    flow[StatenIsland,C6]  OBJ       1.7
    flow[StatenIsland,C6]  landfill[C6]  1
    flow[StatenIsland,C6]  depot[StatenIsland]  1
    flow[StatenIsland,C7]  OBJ       2.1
    flow[StatenIsland,C7]  landfill[C7]  1
    flow[StatenIsland,C7]  depot[StatenIsland]  1
RHS
    RHS1      center[NewYork]  300000
    RHS1      center[NewJersey]  400000
    RHS1      landfill[C1]  100000
    RHS1      landfill[C2]  20000
    RHS1      landfill[C3]  80000
    RHS1      landfill[C4]  70000
    RHS1      landfill[C5]  120000
    RHS1      landfill[C6]  40000
    RHS1      landfill[C7]  50000
    RHS1      depot_capacity[Bronx]  140000
    RHS1      depot_capacity[Brooklyn]  100000
    RHS1      depot_capacity[Queens]  200000
    RHS1      depot_capacity[StatenIsland]  80000
BOUNDS
ENDATA
