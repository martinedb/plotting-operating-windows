## Load Profile + Operating Window Plot #2: Large Pump

import numpy as np
import matplotlib.pyplot as plt

# ----- Flow and Head for Small Pump at Various Speeds -----
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
ax1.plot(flow_LP_full_speed, head_LP_full_speed, label='Large Pump - 100%', color='blue', linewidth=2.5)
ax1.plot(flow_LP_90_speed, head_LP_90_speed, label='Large Pump - 90%', color='blue', linestyle='--', linewidth=2)
ax1.plot(flow_LP_80_speed, head_LP_80_speed, label='Large Pump - 80%', color='blue', linestyle='-.', linewidth=2)
ax1.plot(flow_LP_70_speed, head_LP_70_speed, label='Large Pump - 70%', color='blue', linestyle=':', linewidth=2)

# System curves
ax1.plot([0, 200], [44, 44], color='black', label='Max System Curve', linewidth=2)
ax1.plot([0, 200], [37, 37], linestyle='--', color='black', label='Min System Curve', linewidth=2)

# POR, BEP, and POR Window
ax1.plot(neg_POR_LP_flow, neg_POR_LP_head, '--', color='blue', label='Large Pump POR- 77%', linewidth=1.5)
ax1.plot(pos_POR_LP_flow, pos_POR_LP_head, '-.', color='blue', label='Large Pump POR+ 77%', linewidth=1.5)
ax1.plot(BEP_LP_flow, BEP_LP_head, ':', color='blue', label='Large Pump BEP', linewidth=1.5)
ax1.plot(POR_window_LP_flow, POR_window_LP_head, color='blue', linewidth=4, label='Large Pump POR Window')

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
ax1.set_title("Scenario #2: Large Pump – Operating Window + Load Profile", fontsize=14, weight='bold')
fig.tight_layout()
plt.show()

