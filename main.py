#starter code
mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]
total_missions = 0
successful_missions = 0
pre_y2k_missions_index = []
pre_y2k_missions_names = []
i = -1

#analyze list data
for x in mission_names:
    total_missions += 1
for x in mission_success:
    if x:
        successful_missions += 1
    else: continue
for x in mission_years:
    i += 1
    if x < 2000:
        pre_y2k_missions_index.append(i)
for x in pre_y2k_missions_index:
    pre_y2k_missions_names.append(mission_names[x])

#calculate success rate
success_rate = successful_missions / total_missions
success_rate *= 100

#print data
print("Total number of missions: " + str(total_missions))
print("Number of successful missions: " + str(successful_missions))
print("Success rate: " + str(success_rate) + "%.")
print("Missions launched before 2000:")
print("- " + pre_y2k_missions_names[0])
print("- " + pre_y2k_missions_names[1])
print("- " + pre_y2k_missions_names[2])
print("- " + pre_y2k_missions_names[3])
print("- " + pre_y2k_missions_names[4])
print("- " + pre_y2k_missions_names[5])