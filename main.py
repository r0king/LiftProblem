from lifts import init
print("Press enter or any other character if you dont want to update ")
N = int(input("\n\nEnter no of lifts in the building "))
M = int(input("Enter no of floors in the building "))+1
# create a list of lifts
lifts = []
for _ in range(N):
  lifts.append(init(M))

# each itteration
while True:
  try:
    for i in range(N):
      try:
        #itterate through the lifts
        
          if(input(f'\nUpdate L{i} [y] ? ') == 'y'):
            start = int(input("Starting floor "))
            end = int(input("Destination floor "))
            # if either floor number is higher than the number of loors
            if not (start<M and end<M):
              raise Exception("Error floor numbers")
            # create a new route for the lift to go      
            lifts[i].add_destination(start,end)      
      except ValueError:
        #if no update is present 
        pass        
    
      lifts[i].move()
      
  except KeyboardInterrupt:
    # print total time traveled for each lifts
    for i in range(N):
       print(f'\nLIFT {i}: {lifts[i].end_time} SECONDS')
    exit(0)  