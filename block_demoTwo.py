#!/usr/bin/env python3
# Author: Jacob Meredith (jmer@udel.edu)

from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import math
import time
import os
import numpy as np

# May need to change this pathing based on the location of the .xml file on your device
model = load_model_from_path("./block_demo.xml")

sim = MjSim(model)
viewer = MjViewer(sim)
dataTesting = True
i = 0
posData = []
velData = []
timeData = []
while True:
	position = sim.data.get_body_xpos("block")[2]
	velocity = sim.data.get_body_xvelp("block")[2]
	time = sim.data.time
	
	posData.append(position)
	velData.append(velocity)
	timeData.append(time)
	
	viewer.add_marker(pos=np.array([3, 0, 3]), label=f'[P, V, T]: {[[round(position,5)], [round(velocity,5)], [round(time, 5)]]}')
	viewer.render()
	sim.step()
	
	if(round(velocity,2) == 0 and sim.data.time > 1):
		# If you are working on making sure the data works properly, set dataTesting = True
		# If you are testing to make sure the simulation is running properly and need to run it
		# multiple times, set dataTesting = False for an easy loop
		if(dataTesting):
			
			with open('posData.txt','w') as f:
				f.write("Position:\n")
				for line in posData[0:i + 1]:
					f.write(f"{line}\n")
			
			with open('velData.txt', 'w') as f:
				f.write("Velocity:\n")
				for line in velData[0:i + 1]:
					f.write(f"{line}\n")
					
			with open('timeData.txt','w') as f:
				f.write("Time:\n")
				for line in timeData[0:i + 1]:
					f.write(f"{line}\n")
			
			break
		else:
			sim.reset()
			i = 0
	i += 1
	
	
