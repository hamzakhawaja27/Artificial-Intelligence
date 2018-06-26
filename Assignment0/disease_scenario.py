""" File name:   disease_scenario.py
    Author:      hamza khawaja u6019739
    Date:        
    Description: This file represents a scenario simulating the spread of an
                 infectious disease around Australia. It should be 
                 implemented for Part 1 of Exercise 4 of Assignment 0.
                 
                 See the lab notes for a description of its contents.
"""

class DiseaseScenario:

    def read_scenario_file(self, scenario_file_name):
        self.locations=[]
        self.disease={}
        self.conn={}
        try:
            file=open(scenario_file_name)
            for ff in file:
                f=ff.strip('\n')
                temp_set1=set()
                temp_set2=set()
                line=f.split(" ")
                if line[0]=="threshold":
                    self.threshold=float(line[1])
                elif line[0]=="growth":
                    self.growth=float(line[1])
                elif line[0]=="spread":
                    self.spread=float(line[1])
                elif line[0]=="location":
                    self.locations.append(line[1])
                elif line[0]=="start":
                    self.location=line[1]
                elif line[0]=="disease":
                    self.disease[line[1]]=float(line[2])
                elif line[0]=="conn":
                    if line[1] not in self.conn.keys():
                        temp_set1.add(line[2])
                        self.conn[line[1]]=temp_set1
                    if line[1] in self.conn.keys():
                        temp_set1=self.conn[line[1]]
                        temp_set1.add(line[2])
                        self.conn[line[1]]=temp_set1
                    if line[2] not in self.conn.keys():
                        temp_set2.add(line[1])
                        self.conn[line[2]]=temp_set2
                    if line[2] in self.conn.keys():
                        temp_set2=self.conn[line[2]]
                        temp_set2.add(line[1])
                        self.conn[line[2]]=temp_set2
            for locat in self.locations:
                empty_set=set()
                if locat not in self.conn.keys():
                    self.conn[locat]=empty_set
                if locat not in self.disease.keys():
                    self.disease[locat]=0.0
            return True
        except IOError:
            return False






    def valid_moves(self):
        agent_location=self.location
        near_location=list(self.conn[agent_location])
        near_location.append(agent_location)
        return near_location

    def move(self, loc):
        list_valid_moves=self.valid_moves()
        if loc in list_valid_moves:
            self.location=loc
            self.disease[loc]=0
        else:
            raise ValueError('Agent cannot move to this location: Invalid location')

    def spread_disease(self):
        new_disease={}
        for loc in self.locations:
            if loc != self.location:
                disease_value=self.growth * self.disease[loc] + self.disease[loc]
                conn_set_temp=self.conn[loc]
                for near_loc in conn_set_temp:
                    if self.disease[near_loc]>=self.threshold:
                        near_disease_value=self.disease[near_loc]
                        disease_value=disease_value + near_disease_value * self.spread
                new_disease[loc]=disease_value
                    
            else:
                new_disease[loc]=0

        self.disease=new_disease
               

#var=DiseaseScenario()
#print(var.read_scenario_file("/home/hamza/ANU/Semester-3/ArtificialIntelligence/Assignment-0/COMP3620-6230-2017-Assignment-0/exercise4_maps/scenario1.scn"))
#print(var.move("Alice"))
#print(var.location)
##print(var.threshold)
##print(var.growth)
##print(var.spread)
##print(var.locations)
##print(var.location)
##print(var.disease)
##
##print(var.conn)
##print(type(var.conn["lahore"]))
        
#var.spread_disease()       
        
