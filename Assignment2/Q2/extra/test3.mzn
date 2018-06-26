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
array[trucks,customers,goods] of var 0..MAXCAP: solution;     % solutions array
array[trucks,customers] of var 0..C+1: temp;
	
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
		temp[t,0]=0
			);
constraint
	forall(t in trucks)(
		forall(c,cc in customers where c!=cc)(
		(temp[t,c]>0) -> (temp[t,cc]!=temp[t,c])

		)
		);
constraint
	forall(t in trucks)(
		forall(c,cc in times where c!=cc)(
			sum(g in goods)(solution[t,c,g])>0 -> temp[t,c]>0
			)
			);	
constraint
	forall(t in trucks,c in customers where c!=0)(
			sum(g in goods)(solution[t,c,g])=0 -> temp[t,c]=0
			);

solve satisfy;

%output[show(T) ++ "," ++ show(C)++"\n"]++
%[if (fix(solution[i,j,1]) + fix(solution[i,j,2]))!=0 then show(i)++","++show(j)++","++show(temp[i,j])++","++show(solution[i,j,1])++","++ show%%%%(solution[i,j,2])++"\n" else "" endif | i in 1..T,j in times]++
%["-------------------------"]
%["\n"++show(i)++","++show(ti)++","++show(temp[i,c]) | i in 1..T,ti in times];


output[show(T) ++ "," ++ show(C)++"\n"]++
[show(t)++","++show(temp[t,c])++","++show(c)++","++show(solution[t,c,1])++","++ show(solution[t,c,2])++"\n" | t in trucks,c in customers]++
["-------------------------"]++
["\n"++show(t)++","++show(c)++","++show(temp[t,c]) | t in trucks,c in customers];





% Insert your variables and constraints here


% In question Q2, we are only finding a satisfying solution



% Write a Minizinc output item to print the solution in the desired format for Q2




