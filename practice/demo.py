#!/usr/bin/env python3
from mujoco_py import load_model_from_xml, load_model_from_path, MjSim, MjViewer
import mujoco
import math
import os


model = load_model_from_path("./demo.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
while True:
	viewer.render()
	sim.step()
