#!/usr/bin/env python3
from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import math
import os

model = load_model_from_path("./block_demo.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
a = []
i = 0
while True:
	viewer.render()
	sim.step()
	if(i == 2000):
		print(a)
		sim.reset();
		i = 0
	i += 1
