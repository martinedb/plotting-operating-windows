## Load Profile + Operating Window Plot #5: 2 Large Pumps + Small Pump

import numpy as np
import matplotlib.pyplot as plt

## 2 Large Pumps + Small Pump
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

# ----- Load Profile Data -----
values = np.array([
    13.69212966, 18.0555556, 21.2731482, 23.36805561, 29.02777784,
    64.72222237, 122.6851855, 155.0925929, 309.0277785, 266.2037043,
    228.0092598, 175.9259263, 159.7222226, 427.0833343, 628.4722236,
    590.2777791, 332.1759267, 231.481482, 123.8425929, 483.7962974,
    475.6944455, 645.8333348, 547.4537049, 495.3703715, 442.1296306,
    199.0740745, 386.5740749, 447.9166677, 606.4814828, 510.4166678,
    607.6388903, 464.1203714, 274.3055562, 234.9537042, 233.7962968,
    401.6203713, 885.4166687, 979.1666689, 870.3703723, 680.5555571,
    629.629631, 723.3796313, 1429.398151, 539.3518531, 604.166668,
    574.0740754, 545.1388901, 538.1944457, 797.4537055, 712.9629646,
    818.2870389, 687.5000015, 509.2592604, 930.5555576, 709.4907423,
    789.3518536, 704.8611127, 658.5648163, 568.2870383, 445.6018529,
    668.981483, 954.8611133, 1046.296299, 961.8055577, 864.5833353,
    760.4166684, 456.0185195, 754.6296313, 708.3333349, 563.6574087,
    752.3148165, 902.7777798, 815.9722241, 657.4074089, 487.2685196,
    553.240742, 906.250002, 1090.27778, 1097.222225, 1144.675928,
    927.0833354, 936.3425947, 780.0925943, 819.4444463, 739.583335,
    618.0555569, 497.6851863, 79.35185203, 51.4351853, 75.23148165,
    136.5740744, 469.9074085, 714.120372, 880.787039, 469.9074085,
    304.3981488, 329.8611119, 695.6018534, 622.6851866, 405.0925935,
    513.88889, 582.1759272, 190.9722227, 344.9074082, 443.287038,
    711.8055572, 562.5000013, 449.0740751, 306.7129637, 129.6296299,
    75.23148165, 92.5925928, 97.22222244, 113.4259262, 281.2500006,
    178.2407411, 188.6574078, 310.1851859, 234.9537042, 159.7222226,
    178.2407411, 175.9259263, 237.2685191, 123.8425929, 68.28703719,
    184.0277782, 388.8888898, 436.3425936, 291.6666673, 225.694445,
    141.203704, 160.87963, 215.2777783, 612.2685199, 810.185187,
    608.7962977, 394.6759268, 277.7777784, 358.7962971, 498.8425937,
    541.6666679, 680.5555571, 331.0185193
]) * 0.0864

edges = [0, 14.688, 29.376, 44.064, 58.752, 73.44, 88.128, 102.816, 117.504, 132.192]

# Histogram bin frequencies
freq, bins = np.histogram(values, bins=edges)

# Calculate midpoints and cumulative %
midpoint = (np.array(edges[:-1]) + np.array(edges[1:])) / 2
cum_pct = np.cumsum(freq) / freq.sum() * 100

# Ensure it starts at 0
midpoint = np.insert(midpoint, 0, edges[0])
cum_pct = np.insert(cum_pct, 0, 0)

# ----- Plotting -----
fig, ax1 = plt.subplots(figsize=(14, 8))

# Histogram
ax1.hist(values, bins=edges, edgecolor="black", alpha=0.6, label="Load Profile")
for f, left, right in zip(freq, edges[:-1], edges[1:]):
    ax1.text((left + right) / 2, f + max(freq) * 0.02, str(int(f)),
             ha="center", va="bottom", fontsize=8)

# Pump curves
ax1.plot(flow_twoLPsp_full_speed, head_twoLPsp_full_speed, label='2 Large Pumps + Small Pump - 100%', color='blue', linewidth=2.5)
ax1.plot(flow_twoLPsp_90_speed, head_twoLPsp_90_speed, label='2 Large Pumps + Small Pump - 90%', color='blue', linestyle='--', linewidth=2)
ax1.plot(flow_twoLPsp_80_speed, head_twoLPsp_80_speed, label='2 Large Pumps + Small Pump - 80%', color='blue', linestyle='-.', linewidth=2)
ax1.plot(flow_twoLPsp_70_speed, head_twoLPsp_70_speed, label='2 Large Pumps + Small Pump - 70%', color='blue', linestyle=':', linewidth=2)

# System curves
ax1.plot([0, 200], [44, 44], color='black', label='Max System Curve', linewidth=2)
ax1.plot([0, 200], [37, 37], linestyle='--', color='black', label='Min System Curve', linewidth=2)

# POR, BEP, and POR Window
ax1.plot(neg_POR_twoLPsp_flow, neg_POR_twoLPsp_head, '--', color='blue', label='2 Large Pumps + Small Pump POR- 77%', linewidth=1.5)
ax1.plot(pos_POR_twoLPsp_flow, pos_POR_twoLP_head, '-.', color='blue', label='2 Large Pumps + Small Pump POR+ 77%', linewidth=1.5)
ax1.plot(BEP_twoLPsp_flow, BEP_twoLPsp_head, ':', color='blue', label='2 Large Pumps + Small Pump BEP', linewidth=1.5)
ax1.plot(POR_window_twoLPsp_flow, POR_window_twoLPsp_head, color='blue', linewidth=4, label='2 Large Pumps + Small Pump POR Window')

# Cumulative frequency
ax2 = ax1.twinx()
ax2.plot(midpoint, cum_pct, marker="o", linewidth=2.5, color="tab:red", label="Cumulative (%)")

# ----- THIRD Y-AXIS: Operational Frequency (% per bin) -----
ax3 = ax1.twinx()
ax3.spines["right"].set_position(("axes", 1.1))  # Push it further right
ax3.spines["right"].set_visible(True)

# Convert bin frequencies to % (operational frequency per bin)
op_freq_pct = freq / freq.sum() * 100

# Bin midpoints for plotting
op_midpoint = (np.array(edges[:-1]) + np.array(edges[1:])) / 2

# Plot operational frequency line
ax3.plot(op_midpoint, op_freq_pct, linestyle="--", marker="s", linewidth=2,
         color="darkgreen", label="Operational Frequency (%)")

# Format the third y-axis
ax3.set_ylabel("Operational Frequency (%)", color="black")
ax3.set_ylim(0, 100)
ax3.set_yticks(np.arange(0, 101, 10))
ax3.tick_params(axis='y', labelcolor="black")

# Labels and cosmetics
ax1.set_xlabel("Flow Rate (MLD)")
ax1.set_ylabel("Head (m)")
ax2.set_ylabel("Cumulative Frequency (%)")
ax1.set_xlim(0, 135)
ax1.set_yticks(np.arange(0, 121, 10))  # Head/Frequency on left y-axis
ax2.set_ylim(0, 101)
ax2.set_yticks(np.arange(0, 101, 10))  # Cumulative % on right y-axis
ax3.set_ylim(0, 101)
ax3.set_yticks(np.arange(0, 101, 10))

ax1.set_xticks(np.arange(0, 135, 15))
ax1.grid(axis="x", linestyle=":")


lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
lines3, labels3 = ax3.get_legend_handles_labels()
ax1.legend(lines1 + lines2 + lines3, labels1 + labels2 + labels3,
           loc="center left", bbox_to_anchor=(1.25, 0.5), ncol=1, frameon=True, borderpad=1.5)


# Title and layout
ax1.set_title("Scenario #5: Two Large Pumps + Small Pump", fontsize=14, weight='bold')
fig.tight_layout()
plt.show()

