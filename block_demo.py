#!/usr/bin/env python3
from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import math
import os

model = load_model_from_path("./block_demo.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
i = 0
while True:
	viewer.render()
	sim.step()
	if(i == 500):
		sim.reset();
		i = 0
	i += 1
#t = 0
#while True:
#    sim.data.ctrl[0] = math.cos(t / 10.) * 0.01
#    sim.data.ctrl[1] = math.sin(t / 10.) * 0.01
#    t += 1
#    sim.step()
#    viewer.render()
#    if t > 100 and os.getenv('TESTING') is not None:
#        break
