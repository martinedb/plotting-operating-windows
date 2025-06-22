## Load Profile + Operating Window Plot #4: Large Pump + Large Pump

import numpy as np
import matplotlib.pyplot as plt

## 2 Large Pumps
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
freq, bins = np.histogram(values, bins=edges)
midpoint = np.insert(midpoint, 0, edges[0])  # Insert 0 MLD
cum_pct = np.insert(cum_pct, 0, 0)           # Insert 0%


# ----- Plotting -----
fig, ax1 = plt.subplots(figsize=(14, 8))

# Histogram
ax1.hist(values, bins=edges, edgecolor="black", alpha=0.6, label="Load Profile")
for f, left, right in zip(freq, edges[:-1], edges[1:]):
    ax1.text((left + right) / 2, f + max(freq) * 0.02, str(int(f)),
             ha="center", va="bottom", fontsize=8)

# Pump curves
ax1.plot(flow_twoLP_full_speed, head_twoLP_full_speed, label='2 Large Pumps - 100%', color='blue', linewidth=2.5)
ax1.plot(flow_twoLP_90_speed, head_twoLP_90_speed, label='2 Large Pumps - 90%', color='blue', linestyle='--', linewidth=2)
ax1.plot(flow_twoLP_80_speed, head_twoLP_80_speed, label='2 Large Pumps - 80%', color='blue', linestyle='-.', linewidth=2)
ax1.plot(flow_twoLP_70_speed, head_twoLP_70_speed, label='2 Large Pumps - 70%', color='blue', linestyle=':', linewidth=2)

# System curves
ax1.plot([0, 200], [44, 44], color='black', label='Max System Curve', linewidth=2)
ax1.plot([0, 200], [37, 37], linestyle='--', color='black', label='Min System Curve', linewidth=2)

# POR, BEP, and POR Window
ax1.plot(neg_POR_twoLP_flow, neg_POR_twoLP_head, '--', color='blue', label='2 Large Pumps POR- 77%', linewidth=1.5)
ax1.plot(pos_POR_twoLP_flow, pos_POR_twoLP_head, '-.', color='blue', label='2 Large Pumps POR+ 77%', linewidth=1.5)
ax1.plot(BEP_twoLP_flow, BEP_twoLP_head, ':', color='blue', label='2 Large Pumps BEP', linewidth=1.5)
ax1.plot(POR_window_twoLP_flow, POR_window_twoLP_head, color='blue', linewidth=4, label='2 Large Pumps POR Window')

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
ax1.set_title("Scenario #4: Two Large Pumps – Operating Window + Load Profile", fontsize=14, weight='bold')
fig.tight_layout()
plt.show()

