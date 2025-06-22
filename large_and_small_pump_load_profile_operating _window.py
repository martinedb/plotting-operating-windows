## Load Profile + Operating Window Plot #3: Large Pump + Small Pump

import numpy as np
import matplotlib.pyplot as plt

## Small Pump + Large Pump
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
ax1.plot(flow_spLP_full_speed, head_spLP_full_speed, label='Large Pump + Small Pump - 100%', color='blue', linewidth=2.5)
ax1.plot(flow_spLP_90_speed, head_spLP_90_speed, label='Large Pump + Small Pump - 90%', color='blue', linestyle='--', linewidth=2)
ax1.plot(flow_spLP_80_speed, head_spLP_80_speed, label='Large Pump +  Small Pump - 80%', color='blue', linestyle='-.', linewidth=2)
ax1.plot(flow_spLP_70_speed, head_spLP_70_speed, label='Large Pump + Small Pump - 70%', color='blue', linestyle=':', linewidth=2)

# System curves
ax1.plot([0, 200], [44, 44], color='black', label='Max System Curve', linewidth=2)
ax1.plot([0, 200], [37, 37], linestyle='--', color='black', label='Min System Curve', linewidth=2)

# POR, BEP, and POR Window
ax1.plot(neg_POR_spLP_flow, neg_POR_spLP_head, '--', color='blue', label='Large Pump + Small Pump POR- 77%', linewidth=1.5)
ax1.plot(pos_POR_spLP_flow, pos_POR_spLP_head, '-.', color='blue', label='Large Pump + Small Pump POR+ 77%', linewidth=1.5)
ax1.plot(BEP_spLP_flow, BEP_spLP_head, ':', color='blue', label='Large Pump + Small Pump BEP', linewidth=1.5)
ax1.plot(POR_window_spLP_flow, POR_window_spLP_head, color='blue', linewidth=4, label='Large Pump + Small Pump POR Window')

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
ax1.set_title("Scenario #3: Large Pump + Small Pump – Operating Window + Load Profile", fontsize=14, weight='bold')
fig.tight_layout()
plt.show()

