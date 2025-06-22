## Load Profile + Operating Window Plot #1: Small Pump

import numpy as np
import matplotlib.pyplot as plt

# ----- Flow and Head for Small Pump at Various Speeds -----
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
ax1.plot(flow_sp_full_speed, head_sp_full_speed, label='Small Pump - 100%', color='blue', linewidth=2.5)
ax1.plot(flow_sp_90_speed, head_sp_90_speed, label='Small Pump - 90%', color='blue', linestyle='--', linewidth=2)
ax1.plot(flow_sp_80_speed, head_sp_80_speed, label='Small Pump - 80%', color='blue', linestyle='-.', linewidth=2)
ax1.plot(flow_sp_70_speed, head_sp_70_speed, label='Small Pump - 70%', color='blue', linestyle=':', linewidth=2)

# System curves
ax1.plot([0, 200], [44, 44], color='black', label='Max System Curve', linewidth=2)
ax1.plot([0, 200], [37, 37], linestyle='--', color='black', label='Min System Curve', linewidth=2)

# POR, BEP, and POR Window
ax1.plot(neg_POR_sp_flow, neg_POR_sp_head, '--', color='blue', label='Small Pump POR- 77%', linewidth=1.5)
ax1.plot(pos_POR_sp_flow, pos_POR_sp_head, '-.', color='blue', label='Small Pump POR+ 77%', linewidth=1.5)
ax1.plot(BEP_sp_flow, BEP_sp_head, ':', color='blue', label='Small Pump BEP', linewidth=1.5)
ax1.plot(POR_window_sp_flow, POR_window_sp_head, color='blue', linewidth=4, label='Small Pump POR Window')

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
ax1.set_title("Scenario #1: Small Pump – Operating Window + Load Profile", fontsize=14, weight='bold')
fig.tight_layout()
plt.show()
