int: C;					  % Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types
set of int: times = 0..C+1;            	  % Enough times to visit each customer once and depot twice if needed

array[trucks] of int: cap;	     	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers
array[trucks] of int: centsPerKm;         % Cost of running trucks (in cents per km)
array[customers,customers] of int: D;  	  % Distances between customers (including the depot)
array[trucks] of var 0..100000000000: cost;

var int: tot_cost;	      	   	  % Total cost of the solution
array[trucks,customers,goods] of var 0..MAXCAP: solution;     % solutions array
array[trucks,times] of var 0..C: temp;

constraint
	forall(c in customers)(
		order[1,c]=sum(t in trucks)(solution[t,c,1])
				);

constraint
	forall(c in customers)(
		order[2,c]=sum(t in trucks)(solution[t,c,2])
			);

constraint 
	forall(i in 1..T)
		(cap[i] >= sum(g in goods, c in customers)(solution[i,c,g]));
constraint
	forall(i in 1..T)(
			sum(j in customers)(solution[i,j,1])>0 -> refrig[i]
			);
constraint
	forall(t in trucks)(
		temp[t,0]=0 /\ temp[t,C+1]=0
			);
constraint
	forall(t in trucks)(
		forall(ti,tti in times where ti!=tti)(
			temp[t,ti]=0 \/ temp[t,ti]!=temp[t,tti]
			)
			);
constraint
	forall(t in trucks,c in customers)(
		sum(g in goods)(solution[t,c,g])>0 -> exists(ti in times)(temp[t,ti]=c) 
			);
constraint
	forall(t in trucks,c in customers where c!=0)(
		sum(g in goods)(solution[t,c,g])=0 -> forall(ti in times)(temp[t,ti]!=c)
			);	
constraint
	forall(t in trucks)(
	cost[t]= centsPerKm[t] * sum(ti in 1..C+1)(D[temp[t,ti],temp[t,ti-1]])
		);
constraint
	tot_cost=sum(t in trucks)(cost[t]);

%solve satisfy;
solve minimize tot_cost;

output[show(T) ++ "," ++ show(C)++","++show(tot_cost/100)++"\n"]++
[if (fix(solution[t,fix(temp[t,ti]),1]) + fix(solution[t,fix(temp[t,ti]),2]))!=0 then show(t)++","++show(ti)++","++show(temp[t,ti])++","++show(solution[t,fix(temp[t,ti]),1])++","++ show(solution[t,fix(temp[t,ti]),2])++"\n" else "" endif| t in trucks,ti in times];


