# OLD NOTES:
# Subbing in point COM for each joint in forward (or inverse) kinematics, to then calculate total COM
# Calculate COM for different walking phases
# Use CoM values as a trajectory 'x' -> generate ZMP via cart table model. (LIPM uses ZMP -> CoM). 
# Do smooth generation in Matlab, work backwards to get joint angles

# NEW NOTES 25/6/22 re Paul April 10th
# Use calculate_zmp as basis, sample scripts used in sections 3.3.5 (calcMC, calcCoM) and 4.3.1 (calcZMP):
# Calculate_zmp has calcCOM and calcZMP. calcCOM contains calcMC to use.
from vpython import *
from time import *
import random
import numpy as np
import math

#specify initial conditions
M = 100; #TotalMass from body downwards

#know from body + feet: position, rotation, veloctiy and angular velocity
from SetupJoints_InverseKinematics import SetupBiped
