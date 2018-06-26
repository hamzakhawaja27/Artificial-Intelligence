int: C;					  % Number of customers
int: T;                     		  % Number of trucks
int: G;                     		  % Number of goods types 
int: MAXCAP;                		  % Upper bound on truck capacity

set of int: trucks = 1..T;    	     	  % Set of trucks
set of int: customers = 0..C;        	  % Set of customers. Includes depot as customer 0
set of int: goods = 1..G;            	  % Set of goods types
int: chilled = 1;  int: ambient = 2; 	  % Good types

array[trucks] of int: cap;	     	  % Capacity of trucks
array[trucks] of bool: refrig;	     	  % Whether or not trucks are refrigerated
array[goods,customers] of int: order;	  % Number of units of goods types ordered by customers
array[trucks,goods,customers] of var 0..MAXCAP: solution;     % solutions array
	
constraint
	forall(c in customers)(
		order[1,c]=sum(t in trucks)(solution[t,1,c])
				);

constraint
	forall(c in customers)(
		order[2,c]=sum(t in trucks)(solution[t,2,c])
			);

constraint 
	forall(i in 1..T)
		(cap[i] >= sum(g in goods, c in customers)(solution[i,g,c])
			);
constraint
	forall(i in 1..T)(
		forall(j in 0..C)(
			(solution[i,1,j]>0) -> refrig[i]
			)
			);

solve satisfy;

output[show(T) ++ "," ++ show(C)++"\n"]++
[if (fix(solution[i,1,j]) + fix(solution[i,2,j]))!=0 then show(i)++","++show(j)++","++show(solution[i,1,j])++","++ show(solution[i,2,j])++"\n" else "" endif | i in 1..T,j in 0..C]


