#starter code 
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13'] 
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970] 
mission_success = [True, False, True, True, True, True, False] 
successful_missions = 0 

#Count the total number of missions 
print("Total number of missions: " + str(len(mission_names))) 

#Count the number of successful missions 
for x in mission_success: 
    if x: 
        successful_missions += 1 
    else:  
        continue 
print("Number of successful missions: " + str(successful_missions)) 

#calculate success rate 
success_rate = successful_missions / len(mission_names) * 100 
sucess_rate = round(success_rate, 2)  
print("Success rate: " + str(sucess_rate) + "%") 

#Identify and list all missions launched before the year 2000 
print("Missions launched before the year 2000: ") 
for x in range(len(mission_success)): 
    if mission_years[x] < 2000: 
        print("- " + mission_names[x]) 