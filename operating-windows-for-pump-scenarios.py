import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## Goal: To plot operating windows for the following scenarios and have them separately color-coded on the same graph
# Scenario #1: Small pump 
# Scenario #2: Large Pump
# Scenario #3: Small Pump + Large Pump
# Scenario #4: Two Large Pumps
# Scenario #5: Two Large Pumps + Small Pump

#NOTE: All flow rate data is in MLD and all head data is in m

# Data That I Need To Extract From Each of these Scenario Operating Window Plots
# Max System Curve Data (Same for all scenarios)
# Min System Curve Data (Same for all scenarios)
# Parallel Pumping Data for flow and speed at 100%
# Parallel Pumping Data for flow and speed at 90%
# Parallel Pumping Data for flow and speed at 80%
# Parallel Pumping Data for flow and speed at 70%
# POR- data (flow and head) for 77% 1 Pump 
# POR+ data (flow and head) for 77% 1 Pump 
# BEP data for 1 pump (flow and head)'
#POR Window Generator data (POR-, top curve, POR+, right curve, bottom curve, and left curve)

# use different line patterns to differentiate between the data for the parallel pumping data at different speeds, POR- and POR+ and BEP data. The window generator data should have a greater line thickness than the rest of the lines.

##Max System Curve Data for All Operating Window Plots to be combined into one
# Min System Curve
#Flow (MLD)| Head (m)
# 0        | 37
# 200      | 37

# Max System Curve
#Flow (MLD)| Head (m)
# 0        | 44
# 200      | 44

#Small Pump (sp) Data
flow_sp_full_speed = np.array([0, 1.74528, 3.49056, 5.23584, 6.98112, 8.7264, 10.47168, 12.21696, 13.96224, 15.70752, 17.4528]) # ML/D
head_sp_full_speed = np.array([99.5193087443063, 87.7695216500458, 79.0723320988697, 72.7930988102681, 68.2971805037311, 64.9499358987484, 62.1167237148103, 59.1629026714066, 55.4538314880273, 50.3548688841625, 43.2313735793021])

flow_sp_90_speed = np.array([0, 1.570752, 3.141504, 4.712256, 6.283008, 7.85376, 9.424512, 10.995264, 12.566016, 14.136768, 15.70752])
head_sp_90_speed = np.array([80.6106400828881, 71.0933125365371, 64.0485890000845, 58.9624100363172, 55.3207162080222, 52.6094480779862, 50.3145462089963, 47.9219511638393, 44.9176035053021, 40.7874437961716, 35.0174125992347])

flow_sp_80_speed = np.array([0, 1.396224, 2.792448, 4.188672, 5.584896, 6.98112, 8.377344, 9.773568, 11.169792, 12.566016, 13.96224])
head_sp_80_speed = np.array([63.692357596356, 56.1724938560293, 50.6062925432766, 46.5875832385716, 43.7101955223879, 41.567958975199, 39.7547031774786, 37.8642577097002, 35.4904521523375, 32.227116085864, 27.6680790907534])

flow_sp_70_speed = np.array([0, 1.221696, 2.443392, 3.665088, 4.886784, 6.10848, 7.330176, 8.551872, 9.773568, 10.995264, 12.21696])
head_sp_70_speed = np.array([48.7644612847101, 43.0070656085224, 38.7454427284462, 35.6686184170314, 33.4656184468282, 31.8254685903867, 30.437194620257, 28.9898223089892, 27.1723774291334, 24.6738857532396, 21.183373053858])

neg_POR_sp_flow = np.array([0, 0.3897792, 0.7795584, 1.1693376, 1.5591168, 1.948896, 2.3386752, 2.7284544, 3.1182336, 3.5080128, 3.897792, 4.2875712, 4.6773504, 5.0671296, 5.4569088, 5.846688, 6.2364672, 6.6262464, 7.0160256, 7.4058048, 7.795584, 8.1853632, 8.5751424, 8.9649216, 9.3547008, 9.74448, 10.1342592, 10.5240384, 10.9138176, 11.3035968, 11.693376])
neg_POR_sp_head = np.array([0, 0.0667771934121, 0.2671087736483, 0.6009947407086, 1.0684350945931, 1.6694298353017, 2.4039789628345, 3.2720824771914, 4.2737403783724, 5.4089526663776, 6.6777193412069, 8.0800404028603, 9.6159158513379, 11.2853456866396, 13.0883299087655, 15.0248685177155, 17.0949615134896, 19.2986088960879, 21.6358106655103, 24.1065668217569, 26.7108773648275, 29.4487422947224, 32.3201616114413, 35.3251353149844, 38.4636634053517, 41.735745882543, 45.1413827465586, 48.6805739973982, 52.353319635062, 56.1596196595499, 60.0994740708619])

pos_POR_sp_flow = np.array([0, 0.58, 1.15, 1.73, 2.3, 2.88, 3.46, 4.03, 4.61, 5.18, 5.76, 6.34, 6.91, 7.49, 8.06, 8.64, 9.22, 9.79, 10.37, 10.94, 11.52, 12.09, 12.67, 13.25, 13.82, 14.4, 14.97, 15.55, 16.13, 16.7, 17.28])
pos_POR_sp_head = np.array([0, 0.05, 0.2, 0.44, 0.78, 1.22, 1.76, 2.4, 3.13, 3.96, 4.89, 5.92, 7.05, 8.27, 9.59, 11.01, 12.53, 14.15, 15.86, 17.67, 19.58, 21.59, 23.69, 25.89, 28.19, 30.59, 33.09, 35.68, 38.37, 41.17, 44.05])

BEP_sp_flow = np.array([0, 0.49, 0.97, 1.46, 1.94, 2.43, 2.91, 3.4, 3.89, 4.37, 4.86, 5.34, 5.83, 6.32, 6.8, 7.29, 7.77, 8.26, 8.74, 9.23, 9.72, 10.2, 10.69, 11.17, 11.66, 12.14, 12.63, 13.12, 13.6, 14.09, 14.57])
BEP_sp_head = np.array([0, 0.06, 0.24, 0.54, 0.96, 1.5, 2.15, 2.93, 3.83, 4.85, 5.98, 7.24, 8.62, 10.11, 11.73, 13.46, 15.32, 17.29, 19.39, 21.6, 23.94, 26.39, 28.96, 31.66, 34.47, 37.4, 40.45, 43.63, 46.92, 50.33, 53.86])


POR_window_sp_flow = np.array([11.7, 12.6, 13.6, 14.5, 15.4, 16.3, 17.3, 17.3, 15.4, 13.6, 11.7, 11.7, 11.1, 10.5, 9.9, 9.2, 8.6, 8, 8, 9.2, 10.4, 11.7])
POR_window_sp_head = np.array([60.1, 58.4, 56.4, 54.1, 51.3, 48, 44.1, 44.1, 35.2, 27.3, 20.4, 20.4, 22.2, 23.7, 25, 26.1, 27, 27.8, 27.8, 37.2, 48, 60.1])

# Large Pump (LP) Data

flow_LP_full_speed = np.array([0, 3.516, 7.033, 10.549, 14.066, 17.582, 21.099, 24.615, 28.132, 31.648, 35.165]) 
head_LP_full_speed = np.array([86.004, 79.905, 75.338, 71.874, 69.086, 66.546, 63.827, 60.501, 56.141, 50.318, 42.606])

flow_LP_90_speed = np.array([0, 3.16, 6.33, 9.49, 12.66, 15.82, 18.99, 22.15, 25.32, 28.48, 31.65])
head_LP_90_speed = np.array([69.66, 64.72, 61.02, 58.22, 55.96, 53.9, 51.7, 49.01, 45.47, 40.76, 34.51])

flow_LP_80_speed = np.array([0, 2.81, 5.63, 8.44, 11.25, 14.07, 16.88, 19.69, 22.51, 25.32, 28.13])
head_LP_80_speed = np.array([55.04, 51.14, 48.22, 46, 44.21, 42.59, 40.85, 38.72, 35.93, 32.2, 27.27])

flow_LP_70_speed = np.array([0, 2.462, 4.923, 7.385, 9.846, 12.308, 14.769, 17.231, 19.692, 22.154, 24.615])
head_LP_70_speed = np.array([42.14, 39.15, 36.92, 35.22, 33.85, 32.61, 31.28, 29.65, 27.51, 24.66, 20.88])

neg_POR_LP_flow = np.array([0, 0.68, 1.36, 2.04, 2.72, 3.4, 4.08, 4.76, 5.44, 6.12, 6.8, 7.48, 8.16, 8.84, 9.52, 10.2, 10.88, 11.56, 12.24, 12.92, 13.6, 14.28, 14.96, 15.64, 16.32, 17, 17.68, 18.36, 19.04, 19.72, 20.4])
neg_POR_LP_head = np.array([0, 0.07, 0.29, 0.64, 1.14, 1.79, 2.58, 3.51, 4.58, 5.8, 7.16, 8.66, 10.3, 12.09, 14.03, 16.1, 18.32, 20.68, 23.19, 25.83, 28.62, 31.56, 34.64, 37.86, 41.22, 44.73, 48.38, 52.17, 56.1, 60.18, 64.41 ])

pos_POR_LP_flow = np.array([0, 1.17, 2.34, 3.52, 4.69, 5.86, 7.03, 8.21, 9.38, 10.55, 11.72, 12.89, 14.07, 15.24, 16.41, 17.58, 18.75, 19.93, 21.1, 22.27, 23.44, 24.62, 25.79, 26.96, 28.13, 29.3, 30.48, 31.65, 32.82, 33.99, 35.16 ])
pos_POR_LP_head = np.array([0, 0.05, 0.19, 0.43, 0.76, 1.18, 1.7, 2.32, 3.03, 3.83, 4.73, 5.73, 6.82, 8, 9.28, 10.65, 12.12, 13.68, 15.34, 17.09, 18.94, 20.88, 22.91, 25.04, 27.27, 29.59, 32, 34.51, 37.11, 39.81, 42.61])

BEP_LP_flow = np.array([0, 0.9, 1.9, 2.8, 3.7, 4.6, 5.6, 6.5, 7.4, 8.3, 9.3, 10.2, 11.1, 12, 13, 13.9, 14.8, 15.7, 16.7, 17.6, 18.5, 19.4, 20.4, 21.3, 22.2, 23.2, 24.1, 25, 25.9, 26.9, 27.8])
BEP_LP_head = np.array([0, 0.06, 0.25, 0.57, 1.01, 1.57, 2.27, 3.08, 4.03, 5.1, 6.29, 7.61, 9.06, 10.63, 12.33, 14.16, 16.11, 18.19, 20.39, 22.72, 25.17, 27.75, 30.46, 33.29, 36.25, 39.33, 42.54, 45.87, 49.34, 52.92, 56.64])


POR_window_LP_flow = np.array([20.4, 22.9, 25.3, 27.8, 30.2, 32.7, 35.2, 35.2, 31.4, 27.7, 23.9, 23.9, 22.2, 20.6, 18.9, 17.2, 15.5, 13.9, 13.9, 16, 18.2, 20.4])
POR_window_LP_head = np.array([64.4, 62.3, 59.7, 56.6, 52.8, 48.2, 42.6, 42.6, 34, 26.4, 19.7, 19.7, 22.3, 24.4, 26.2, 27.6, 28.8, 29.8, 29.8, 39.9, 51.4, 64.4])

# Small Pump + Large Pump Data (spLP) 

flow_spLP_full_speed = np.array([0, 5.21, 10.42, 15.63, 20.84, 26.05, 31.26, 36.47, 41.68, 46.89, 52.1]) 
head_spLP_full_speed = np.array([77.5, 75.4, 73.5, 71.5, 69.3, 66.8, 63.9, 60.4, 56.1, 51.1, 45])

flow_spLP_90_speed = np.array([0, 4.7, 9.4, 14.1, 18.8, 23.4, 28.1, 32.8, 37.5, 42.2, 46.9])
head_spLP_90_speed = np.array([62.8, 61.1, 59.5, 57.9, 56.2, 54.1, 51.8, 48.9, 45.5, 41.4, 36.4])

flow_spLP_80_speed = np.array([0, 4.2, 8.3, 12.5, 16.7, 20.8, 25, 29.2, 33.3, 37.5, 41.7])
head_spLP_80_speed = np.array([49.6, 48.3, 47, 45.8, 44.4, 42.8, 40.9, 38.6, 35.9, 32.7, 28.8])

flow_spLP_70_speed = np.array([0, 3.6, 7.3, 10.9, 14.6, 18.2, 21.9, 25.5, 29.2, 32.8, 36.5])
head_spLP_70_speed = np.array([38, 37, 36, 35, 34, 32.8, 31.3, 29.6, 27.5, 25, 22])

neg_POR_spLP_flow = np.array([0, 1, 2.1, 3.1, 4.1, 5.2, 6.2, 7.2, 8.3, 9.3, 10.3, 11.4, 12.4, 13.4, 14.5, 15.5, 16.5, 17.6, 18.6, 19.6, 20.7, 21.7, 22.7, 23.8, 24.8, 25.8, 26.9, 27.9, 28.9, 30, 31])
neg_POR_spLP_head = np.array([0, 0.1, 0.3, 0.6, 1.1, 1.8, 2.6, 3.5, 4.6, 5.8, 7.1, 8.6, 10.3, 12, 14, 16, 18.2, 20.6, 23.1, 25.7, 28.5, 31.4, 34.5, 37.7, 41, 44.5, 48.1, 51.9, 55.8, 59.9, 64.1])

pos_POR_spLP_flow = np.array([0, 1.7, 3.5, 5.2, 6.9, 8.7, 10.4, 12.2, 13.9, 15.6, 17.4, 19.1, 20.8, 22.6, 24.3, 26, 27.8, 29.5, 31.3, 33, 34.7, 36.5, 38.2, 39.9, 41.7, 43.4, 45.2, 46.9, 48.6, 50.4, 52.1])
pos_POR_spLP_head = np.array([0, 0.05, 0.2, 0.45, 0.8, 1.25, 1.8, 2.45, 3.2, 4.05, 5, 6.05, 7.2, 8.45, 9.8, 11.25, 12.8, 14.45, 16.2, 18.05, 20, 22.05, 24.2, 26.45, 28.8, 31.25, 33.8, 36.45, 39.2, 42.05, 45])

BEP_spLP_flow = np.array([0, 1.42, 2.83, 4.25, 5.66, 7.08, 8.49, 9.91, 11.32, 12.74, 14.15, 15.57, 16.98, 18.4, 19.81, 21.23, 22.65, 24.06, 25.48, 26.89, 28.31, 29.72, 31.14, 32.55, 33.97, 35.38, 36.8, 38.21, 39.63, 41.04, 42.46])
BEP_spLP_head = np.array([0, 0.06, 0.25, 0.55, 0.99, 1.54, 2.22, 3.02, 3.94, 4.99, 6.16, 7.45, 8.87, 10.41, 12.07, 13.86, 15.77, 17.8, 19.96, 22.24, 24.64, 27.17, 29.81, 32.59, 35.48, 38.5, 41.64, 44.91, 48.29, 51.81, 55.44])

POR_window_spLP_flow = np.array([31, 34.5, 38, 41.5, 45.1, 48.6, 52.1, 52.1, 46.5, 41, 35.4, 35.4, 33, 30.6, 28.3, 25.9, 23.5, 21.1, 21.1, 24.4, 27.7, 31])
POR_window_spLP_head = np.array([64.06, 61.78, 59.19, 56.26, 52.95, 49.21, 45, 45, 35.91, 27.85, 20.81, 20.81, 22.75, 24.48, 26.01, 27.37, 28.57, 29.62, 29.62, 39.64, 51.12, 64.06])

# 2 Large Pumps (twoLP) data

flow_twoLP_full_speed = np.array([0, 6.98, 13.95, 20.93, 27.91, 34.88, 41.86, 48.84, 55.82, 62.79, 69.77]) 
head_twoLP_full_speed = np.array([81.45, 78.86, 76.29, 73.66, 70.86, 67.79, 64.35, 60.46, 56, 50.88, 45])

flow_twoLP_90_speed = np.array([0, 6.28, 12.56, 18.84, 25.12, 31.4, 37.68, 43.95, 50.23, 56.51, 62.79])
head_twoLP_90_speed = np.array([65.97, 63.87, 61.8, 59.66, 57.39, 54.91, 52.13, 48.97, 45.36, 41.21, 36.45])

flow_twoLP_80_speed = np.array([0, 5.58, 11.16, 16.74, 22.33, 27.91, 33.49, 39.07, 44.65, 50.23, 55.82])
head_twoLP_80_speed = np.array([52.13, 50.47, 48.83, 47.14, 45.35, 43.38, 41.19, 38.69, 35.84, 32.56, 28.8])

flow_twoLP_70_speed = np.array([0, 4.88, 9.77, 14.65, 19.54, 24.42, 29.3, 34.19, 39.07, 43.95, 48.84])
head_twoLP_70_speed = np.array([39.91, 38.64, 37.38, 36.09, 34.72, 33.22, 31.53, 29.62, 27.44, 24.93, 22.05])

neg_POR_twoLP_flow = np.array([0, 1.3, 2.5, 3.8, 5.1, 6.3, 7.6, 8.9, 10.1, 11.4, 12.7, 13.9, 15.2, 16.5, 17.7, 19, 20.3, 21.5, 22.8, 24.1, 25.3, 26.6, 27.9, 29.2, 30.4, 31.7, 33, 34.2, 35.5, 36.8, 38])
neg_POR_twoLP_head = np.array([0, 0.1, 0.3, 0.7, 1.2, 1.8, 2.7, 3.6, 4.7, 6, 7.4, 8.9, 10.6, 12.4, 14.4, 16.6, 18.9, 21.3, 23.9, 26.6, 29.5, 32.5, 35.7, 39, 42.4, 46, 49.8, 53.7, 57.7, 61.9, 66.3])

pos_POR_twoLP_flow = np.array([0, 2.3, 4.7, 7, 9.3, 11.6, 14, 16.3, 18.6, 20.9, 23.3, 25.6, 27.9, 30.2, 32.6, 34.9, 37.2, 39.5, 41.9, 44.2, 46.5, 48.8, 51.2, 53.5, 55.8, 58.1, 60.5, 62.8, 65.1, 67.4, 69.8])
pos_POR_twoLP_head = np.array([0, 0.05, 0.2, 0.45, 0.8, 1.25, 1.8, 2.45, 3.2, 4.05, 5, 6.05, 7.2, 8.45, 9.8, 11.25, 12.8, 14.45, 16.2, 18.05, 20, 22.05, 24.2, 26.45, 28.8, 31.25, 33.8, 36.45, 39.2, 42.05, 45])

BEP_twoLP_flow = np.array([0, 1.78, 3.56, 5.34, 7.12, 8.9, 10.67, 12.45, 14.23, 16.01, 17.79, 19.57, 21.35, 23.13, 24.91, 26.69, 28.47, 30.25, 32.02, 33.8, 35.58, 37.36, 39.14, 40.92, 42.7, 44.48, 46.26, 48.04, 49.82, 51.59, 53.37])
BEP_twoLP_head = np.array([0, 0.06, 0.26, 0.58, 1.02, 1.6, 2.31, 3.14, 4.1, 5.19, 6.4, 7.75, 9.22, 10.82, 12.55, 14.41, 16.39, 18.5, 20.75, 23.12, 25.61, 28.24, 30.99, 33.87, 36.88, 40.02, 43.28, 46.68, 50.2, 53.85, 57.63])

POR_window_twoLP_flow = np.array([38, 43.3, 48.6, 53.9, 59.2, 64.5, 69.8, 69.8, 62.3, 54.9, 47.4, 47.4, 43.8, 40.2, 36.6, 33.1, 29.5, 25.9, 25.9, 29.9, 34, 38])
POR_window_twoLP_head = np.array([66.3, 63.6, 60.6, 57.3, 53.6, 49.5, 45, 45, 35.9, 27.8, 20.8, 20.8, 22.9, 24.8, 26.5, 28, 29.4, 30.7, 30.7, 41, 52.9, 66.3])

# 2 Large Pumps + Small Pump (twoLPsp)

flow_twoLPsp_full_speed = np.array([0, 8.7, 17.4, 26.09, 34.79, 43.49, 52.19, 60.89, 69.59, 78.28, 86.98]) 
head_twoLPsp_full_speed = np.array([85.74, 80.57, 76.42, 73, 70.01, 67.15, 64.13, 60.65, 56.4, 51.1, 44.44])

flow_twoLPsp_90_speed = np.array([0, 7.8, 15.7, 23.5, 31.3, 39.1, 47, 54.8, 62.6, 70.5, 78.3])
head_twoLPsp_90_speed = np.array([69.45, 65.26, 61.9, 59.13, 56.71, 54.39, 51.95, 49.12, 45.69, 41.39, 36])

flow_twoLPsp_80_speed = np.array([0, 6.96, 13.92, 20.88, 27.83, 34.79, 41.75, 48.71, 55.67, 62.63, 69.59])
head_twoLPsp_80_speed = np.array([54.87, 51.56, 48.91, 46.72, 44.81, 42.98, 41.04, 38.81, 36.1, 32.7, 28.44])

flow_twoLPsp_70_speed = np.array([0, 6.09, 12.18, 18.27, 24.36, 30.44, 36.53, 42.62, 48.71, 54.8, 60.89])
head_twoLPsp_70_speed = np.array([42.01, 39.48, 37.45, 35.77, 34.3, 32.9, 31.42, 29.72, 27.64, 25.04, 21.78])

neg_POR_twoLPsp_flow = np.array([0, 1.49, 2.99, 4.48, 5.97, 7.47, 8.96, 10.45, 11.95, 13.44, 14.93, 16.43, 17.92, 19.41, 20.9, 22.4, 23.89, 25.38, 26.88, 28.37, 29.86, 31.36, 32.85, 34.34, 35.84, 37.33, 38.82, 40.32, 41.81, 43.3, 44.8])
neg_POR_twoLPsp_head = np.array([0, 0.07, 0.3, 0.67, 1.19, 1.85, 2.67, 3.63, 4.74, 6, 7.41, 8.97, 10.67, 12.53, 14.53, 16.68, 18.98, 21.42, 24.02, 26.76, 29.65, 32.69, 35.88, 39.21, 42.7, 46.33, 50.11, 54.04, 58.12, 62.34, 66.72])

pos_POR_twoLPsp_flow = np.array([0, 2.9, 5.8, 8.7, 11.6, 14.5, 17.4, 20.3, 23.2, 26.09, 28.99, 31.89, 34.79, 37.69, 40.59, 43.49, 46.39, 49.29, 52.19, 55.09, 57.99, 60.89, 63.79, 66.69, 69.59, 72.49, 75.39, 78.28, 81.18, 84.08, 86.98])
pos_POR_twoLPsp_head = np.array([0, 0.05, 0.2, 0.44, 0.79, 1.23, 1.78, 2.42, 3.16, 4, 4.94, 5.97, 7.11, 8.35, 9.68, 11.11, 12.64, 14.27, 16, 17.83, 19.75, 21.78, 23.9, 26.12, 28.44, 30.86, 33.38, 36, 38.71, 41.53, 44.44])

BEP_twoLPsp_flow = np.array([0, 2.9, 5.8, 8.7, 11.6, 14.5, 17.4, 20.3, 23.2, 26.09, 28.99, 31.89, 34.79, 37.69, 40.59, 43.49, 46.39, 49.29, 52.19, 55.09, 57.99, 60.89, 63.79, 66.69, 69.59, 72.49, 75.39, 78.28, 81.18, 84.08, 86.98])
BEP_twoLPsp_head = np.array([0, 0.05, 0.2, 0.44, 0.79, 1.23, 1.78, 2.42, 3.16, 4, 4.94, 5.97, 7.11, 8.35, 9.68, 11.11, 12.64, 14.27, 16, 17.83, 19.75, 21.78, 23.9, 26.12, 28.44, 30.86, 33.38, 36, 38.71, 41.53, 44.44])

POR_window_twoLPsp_flow = np.array([44.8, 51.8, 58.9, 65.9, 72.9, 80, 87, 87, 77.7, 68.4, 59.1, 59.1, 54.4, 49.6, 44.8, 40, 35.2, 30.5, 30.5, 35.2, 40, 44.8])
POR_window_twoLPsp_head = np.array([66.7, 64.3, 61.5, 58.3, 54.5, 49.9, 44.4, 44.4, 35.5, 27.5, 20.5, 20.5, 23.1, 25.2, 27, 28.4, 29.7, 30.8, 30.8, 41.3, 53.2, 66.7])


## Color-Coding for Each Scenario:
# Scenario #1: Small pump (Blue)
# Scenario #2: Large Pump (Red)
# Scenario #3: Small Pump + Large Pump (Green)
# Scenario #4: Two Large Pumps (Purple)
# Scenario #5: Two Large Pumps (Gray)

# The flow in MLD would be the x-axis and the head (m) would be the y-axis.

# A legend would be included for the operating window plot

import matplotlib.pyplot as plt

# Max and Min system curves
flow_system = np.array([0, 200])
head_max_system = np.array([44, 44])
head_min_system = np.array([37, 37])

# Create the plot
plt.figure(figsize=(18, 12))

# Helper function to plot scenario data
def plot_scenario(flow, head, label, color):
    plt.plot(flow, head, label=label, color=color, linewidth=2)

# Plot System Curves
plt.plot(flow_system, head_max_system,  color='black', label='Max System Curve', linewidth=2)
plt.plot(flow_system, head_min_system, linestyle='--', color='black', label='Min System Curve', linewidth=2)

# Scenario 1: Small Pump
plot_scenario(flow_sp_full_speed, head_sp_full_speed, 'Small Pump - 100%', 'blue')
plot_scenario(flow_sp_90_speed, head_sp_90_speed, 'Small Pump - 90%', 'blue')
plot_scenario(flow_sp_80_speed, head_sp_80_speed, 'Small Pump - 80%', 'blue')
plot_scenario(flow_sp_70_speed, head_sp_70_speed, 'Small Pump - 70%', 'blue')
plt.plot(neg_POR_sp_flow, neg_POR_sp_head, '--', color='blue', label='Small Pump POR-', linewidth=1)
plt.plot(pos_POR_sp_flow, pos_POR_sp_head, '-.', color='blue', label='Small Pump POR+', linewidth=1)
plt.plot(BEP_sp_flow, BEP_sp_head, ':', color='blue', label='Small Pump BEP', linewidth=1)
plt.plot(POR_window_sp_flow, POR_window_sp_head, color='blue', linewidth=4, label='Small Pump POR Window')

# Scenario 2: Large Pump
plot_scenario(flow_LP_full_speed, head_LP_full_speed, 'Large Pump - 100%', 'red')
plot_scenario(flow_LP_90_speed, head_LP_90_speed, 'Large Pump - 90%', 'red')
plot_scenario(flow_LP_80_speed, head_LP_80_speed, 'Large Pump - 80%', 'red')
plot_scenario(flow_LP_70_speed, head_LP_70_speed, 'Large Pump - 70%', 'red')
plt.plot(neg_POR_LP_flow, neg_POR_LP_head, '--', color='red', label='Large Pump POR-', linewidth=1)
plt.plot(pos_POR_LP_flow, pos_POR_LP_head, '-.', color='red', label='Large Pump POR+', linewidth=1)
plt.plot(BEP_LP_flow, BEP_LP_head, ':', color='red', label='Large Pump BEP', linewidth=1)
plt.plot(POR_window_LP_flow, POR_window_LP_head, color='red', linewidth=4, label='Large Pump POR Window')

# Scenario 3: Small + Large Pump
plot_scenario(flow_spLP_full_speed, head_spLP_full_speed, 'Small + Large Pump - 100%', 'green')
plot_scenario(flow_spLP_90_speed, head_spLP_90_speed, 'Small + Large Pump - 90%', 'green')
plot_scenario(flow_spLP_80_speed, head_spLP_80_speed, 'Small + Large Pump - 80%', 'green')
plot_scenario(flow_spLP_70_speed, head_spLP_70_speed, 'Small + Large Pump - 70%', 'green')
plt.plot(neg_POR_spLP_flow, neg_POR_spLP_head, '--', color='green', label='Small+Large POR-', linewidth=1)
plt.plot(pos_POR_spLP_flow, pos_POR_spLP_head, '-.', color='green', label='Small+Large POR+', linewidth=1)
plt.plot(BEP_spLP_flow, BEP_spLP_head, ':', color='green', label='Small + Large BEP', linewidth=1)
plt.plot(POR_window_spLP_flow, POR_window_spLP_head, color='green', linewidth=4, label='Small + Large POR Window')

# Scenario 4: Two Large Pumps
plot_scenario(flow_twoLP_full_speed, head_twoLP_full_speed, 'Two Large Pumps - 100%', 'purple')
plot_scenario(flow_twoLP_90_speed, head_twoLP_90_speed, 'Two Large Pumps - 90%', 'purple')
plot_scenario(flow_twoLP_80_speed, head_twoLP_80_speed, 'Two Large Pumps - 80%', 'purple')
plot_scenario(flow_twoLP_70_speed, head_twoLP_70_speed, 'Two Large Pumps - 70%', 'purple')
plt.plot(neg_POR_twoLP_flow, neg_POR_twoLP_head, '--', color='purple', label='Two Large Pumps POR-', linewidth=1)
plt.plot(pos_POR_twoLP_flow, pos_POR_twoLP_head, '-.', color='purple', label='Two Large Pumps POR+', linewidth=1)
plt.plot(BEP_twoLP_flow, BEP_twoLP_head, ':', color='purple', label='Two Large Pumps BEP', linewidth=1)
plt.plot(POR_window_twoLP_flow, POR_window_twoLP_head, color='purple', linewidth=4, label='Two Large Pumps POR Window')

# Scenario 5: Two Large + Small Pump
plot_scenario(flow_twoLPsp_full_speed, head_twoLPsp_full_speed, 'Two Large + Small Pump - 100%', 'gray')
plot_scenario(flow_twoLPsp_90_speed, head_twoLPsp_90_speed, 'Two Large + Small Pump - 90%', 'gray')
plot_scenario(flow_twoLPsp_80_speed, head_twoLPsp_80_speed, 'Two Large + Small Pump - 80%', 'gray')
plot_scenario(flow_twoLPsp_70_speed, head_twoLPsp_70_speed, 'Two Large + Small Pump - 70%', 'gray')
plt.plot(neg_POR_twoLPsp_flow, neg_POR_twoLPsp_head, '--', color='gray', label='2 Large Pumps + Small Pump POR-', linewidth=1)
plt.plot(pos_POR_twoLPsp_flow, pos_POR_twoLPsp_head, '-.', color='gray', label='2 Large Pumps + Small Pump POR+', linewidth=1)
plt.plot(BEP_twoLPsp_flow, BEP_twoLPsp_head, ':', color='gray', label='2 Large Pumps + Small Pump BEP', linewidth=1)
plt.plot(POR_window_twoLPsp_flow, POR_window_twoLPsp_head, color='gray', linewidth=4, label='2 Large Pumps + Small Pump POR Window')


# Plot formatting
plt.xlabel('Flow Rate (MLD)')
plt.ylabel('Head (m)')
plt.title('Operating Windows for Pump Scenarios')
plt.grid(True)
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize='small')
plt.xlim(0, 100)
plt.tight_layout()
plt.show()

# Update this code to include a second and third y-axis for operational and cumulative frequency and include 
# load profile on this graph and put the legend under the graph instead.
