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
stepLimit = 5000
blockData = [[None],[None],[None]] * stepLimit
dataTesting = True
i = 0
while True:
	position = sim.data.get_body_xpos("block")[2]
	velocity = sim.data.get_body_xvelp("block")[2]
	time = sim.data.time
	blockData[i] = [[position], [velocity], [time]]
	viewer.add_marker(pos=np.array([3, 0, 3]), label=f'[P, V, T]: {[[round(position,5)], [round(velocity,5)], [round(time, 5)]]}')
	viewer.render()
	sim.step()
	#if(i == stepLimit):
	if(i == stepLimit):
		# If you are working on making sure the data works properly, set dataTesting = True
		# If you are testing to make sure the simulation is running properly and need to run it
		# multiple times, set dataTesting = False for an easy loop
		if(dataTesting):
			with open('testData.txt','w') as f:
				f.write("Column 1: Position	Column 2: Velocity	Column 3: Time\n")
				for line in blockData[0:stepLimit + 1]:
					for pt in line:
						f.write(f"{pt}	")
					f.write(f"\n")
			break
		else:
			sim.reset()
			i = 0
	i += 1
	
	
