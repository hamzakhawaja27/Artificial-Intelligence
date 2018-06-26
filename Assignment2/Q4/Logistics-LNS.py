import argparse
import subprocess
import time


# Complete the file with your LNS solution
   
def Minizinc_Print(x,y,z):
   command = [x,y,z]
   result = subprocess.run(command, stdout=subprocess.PIPE)
   output = result.stdout
   output = output.decode()
   lines=output.splitlines()
   num=lines[0].split(",")
   new_cost=float(num[2])
   return new_cost,output
   

def original_sol(text):
   print("Original Solution")
   first_line=text[0].split(",")
   trucks=int(first_line[0])
   cust=int(first_line[1][1:])
   cost=float(first_line[2][1:])
   for t in text:
      print(t)
   print()
   return trucks,cust,cost

def write_try(text,KCons,count,window):

   temp_list=list()
   for i in range(count,count+window ):
      temp_list.append(i)
   for i in range(1,len(text)):
      line_tok=text[i].split(',')
      if temp_list.__contains__(int(line_tok[0])):
         pass
      else:
         out1="solution[" + line_tok[0] + ',' + line_tok[2] + ',' + '1' + ']' + '=' + line_tok[3] + ";"
         out2="solution[" + line_tok[0] + ',' + line_tok[2] + ',' + '2' + ']' + '=' + line_tok[4] + ";"
         t="temp["+ line_tok[0] + ',' + line_tok[1] + ']' + '=' + line_tok[2] + ";"
         KCons.write("constraint\n")
         KCons.write(out1 + "\n")
         KCons.write("constraint\n")
         KCons.write(out2 + "\n")
         KCons.write("constraint\n")
         KCons.write(t + "\n")

   KCons.close()

def printp(final_output):
   lines=output.splitlines()
   count=0
   for l in lines:
      if count==0:
         print(l)
      elif count>=len(lines)-3:
         pass
      else:
         ll=l.split(",")
         if(ll[3]!='0' or ll[4]!='0'):
            print(l)
      count=count+1;
  
if __name__ =='__main__':
   parser = argparse.ArgumentParser()
   parser.add_argument('problem_filename', help='problem file')
   parser.add_argument('start_solution_filename', help='file describing the solution to improve')
   args = parser.parse_args()
   start_solution_filename = args.start_solution_filename
   problem_filename = args.problem_filename
   start_time = time.time()
   start_solution = open(start_solution_filename,'r')
   text=start_solution.read().splitlines()
   trucks,cust,Original_Cost=original_sol(text)
   count=1
   window=1;
   KCons=open("keep_constraints.mzn",'w')
   write_try(text,KCons,count,window)
   temp_cost=Original_Cost
   while (True):
      if (time.time()-start_time)<60.0:
         new_cost,output=Minizinc_Print("minizinc", "Logistics-opt.mzn", problem_filename)
         final_output=output
         temp_cost=new_cost
         print()
         print("time=",time.time()-start_time)
         print("Current Best Solution")
         printp(final_output)
         KCons=open("keep_constraints.mzn",'w')
         final_output=final_output.splitlines()
         final_output=final_output[0:len(final_output)-3]
         write_try(final_output,KCons,count,window)
         count=count+window;
         if (count+window) >trucks+1:
            count=1
            window=window+1
            if window> trucks+1:
               break


      else:
         break


      












   
#   parser = argparse.ArgumentParser()
#   parser.add_argument('problem_filename', help='problem file')
#   parser.add_argument('start_solution_filename', help='file describing the solution to improve')
#   args = parser.parse_args()
#   start_solution_filename = args.start_solution_filename
#   problem_filename = args.problem_filename


   
