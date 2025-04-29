\ Model Landfill Transportation
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  0.7 flow[NewYork,Bronx] + 0.7 flow[NewYork,Brooklyn]
   + 1.2 flow[NewYork,Queens] + 0.4 flow[NewYork,StatenIsland]
   + 1.2 flow[NewYork,C1] + 1.7 flow[NewYork,C3] + 2.2 flow[NewYork,C4]
   + 1.2 flow[NewYork,C6] + 2 flow[NewYork,C7]
   + 0.5 flow[NewJersey,Brooklyn] + 0.7 flow[NewJersey,Queens]
   + 0.4 flow[NewJersey,StatenIsland] + 2.2 flow[NewJersey,C1]
   + 1.8 flow[NewJersey,C7] + 1.7 flow[Bronx,C2] + 0.7 flow[Bronx,C3]
   + 1.7 flow[Bronx,C4] + 1.2 flow[Bronx,C6] + 1.9 flow[Bronx,C7]
   + 1.2 flow[Brooklyn,C1] + 0.7 flow[Brooklyn,C2] + 0.7 flow[Brooklyn,C3]
   + 1.2 flow[Brooklyn,C4] + 0.7 flow[Brooklyn,C5] + 1.5 flow[Brooklyn,C7]
   + 1.7 flow[Queens,C2] + 2.2 flow[Queens,C3] + 0.7 flow[Queens,C5]
   + 1.7 flow[Queens,C6] + 1.6 flow[Queens,C7] + 0.4 flow[StatenIsland,C3]
   + 1.7 flow[StatenIsland,C4] + 0.7 flow[StatenIsland,C5]
   + 1.7 flow[StatenIsland,C6] + 2.1 flow[StatenIsland,C7]
Subject To
 center[NewYork]: flow[NewYork,Bronx] + flow[NewYork,Brooklyn]
   + flow[NewYork,Queens] + flow[NewYork,StatenIsland] + flow[NewYork,C1]
   + flow[NewYork,C3] + flow[NewYork,C4] + flow[NewYork,C6]
   + flow[NewYork,C7] <= 300000
 center[NewJersey]: flow[NewJersey,Brooklyn] + flow[NewJersey,Queens]
   + flow[NewJersey,StatenIsland] + flow[NewJersey,C1] + flow[NewJersey,C7]
   <= 400000
 landfill[C1]: flow[NewYork,C1] + flow[NewJersey,C1] + flow[Brooklyn,C1]
   = 100000
 landfill[C2]: flow[Bronx,C2] + flow[Brooklyn,C2] + flow[Queens,C2]
   = 20000
 landfill[C3]: flow[NewYork,C3] + flow[Bronx,C3] + flow[Brooklyn,C3]
   + flow[Queens,C3] + flow[StatenIsland,C3] = 80000
 landfill[C4]: flow[NewYork,C4] + flow[Bronx,C4] + flow[Brooklyn,C4]
   + flow[StatenIsland,C4] = 70000
 landfill[C5]: flow[Brooklyn,C5] + flow[Queens,C5] + flow[StatenIsland,C5]
   = 120000
 landfill[C6]: flow[NewYork,C6] + flow[Bronx,C6] + flow[Queens,C6]
   + flow[StatenIsland,C6] = 40000
 landfill[C7]: flow[NewYork,C7] + flow[NewJersey,C7] + flow[Bronx,C7]
   + flow[Brooklyn,C7] + flow[Queens,C7] + flow[StatenIsland,C7] = 50000
 depot[Bronx]: - flow[NewYork,Bronx] + flow[Bronx,C2] + flow[Bronx,C3]
   + flow[Bronx,C4] + flow[Bronx,C6] + flow[Bronx,C7] = 0
 depot[Brooklyn]: - flow[NewYork,Brooklyn] - flow[NewJersey,Brooklyn]
   + flow[Brooklyn,C1] + flow[Brooklyn,C2] + flow[Brooklyn,C3]
   + flow[Brooklyn,C4] + flow[Brooklyn,C5] + flow[Brooklyn,C7] = 0
 depot[Queens]: - flow[NewYork,Queens] - flow[NewJersey,Queens]
   + flow[Queens,C2] + flow[Queens,C3] + flow[Queens,C5] + flow[Queens,C6]
   + flow[Queens,C7] = 0
 depot[StatenIsland]: - flow[NewYork,StatenIsland]
   - flow[NewJersey,StatenIsland] + flow[StatenIsland,C3]
   + flow[StatenIsland,C4] + flow[StatenIsland,C5] + flow[StatenIsland,C6]
   + flow[StatenIsland,C7] = 0
 depot_capacity[Bronx]: flow[NewYork,Bronx] <= 140000
 depot_capacity[Brooklyn]: flow[NewYork,Brooklyn]
   + flow[NewJersey,Brooklyn] <= 100000
 depot_capacity[Queens]: flow[NewYork,Queens] + flow[NewJersey,Queens]
   <= 200000
 depot_capacity[StatenIsland]: flow[NewYork,StatenIsland]
   + flow[NewJersey,StatenIsland] <= 80000
Bounds
End
