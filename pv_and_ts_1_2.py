#This code generates the p-v and t-s digrams for an ideal otto cycle

import numpy as np
import matplotlib.pyplot as plt


P1 = 101325.0            # Initial pressure (Pa)
T1 = 300.0               # Initial temperature (K)
r = 8.0                  # Compression ratio
T3 = 1500.0              # Max temperature after heat addition (K)
R = 287.0                # Gas constant for air (J/kg·K)
gamma = 1.4              # Ratio of specific heats

# Derived specific heats
cp = gamma * R / (gamma - 1)
cv = cp - R

#State 1
v1 = R * T1 / P1

#State 2 (isentropic compression)
v2 = v1 / r
T2 = T1 * r**(gamma - 1)
P2 = R * T2 / v2

#State 3 (constant volume heat addition)
v3 = v2
P3 = R * T3 / v3

#State 4 (isentropic expansion)
v4 = v1
T4 = T3 / r**(gamma - 1)
P4 = R * T4 / v4

#Entropy (relative values)
s1 = 0
s2 = s1
s3 = s2 + cv * np.log(T3/T2)
s4 = s3

# P–v DATA
# isentropic compression 1→2
v_12 = np.linspace(v1, v2, 200)
P_12 = P1 * (v1**gamma) / (v_12**gamma)

# constant volume 2→3
v_23 = np.array([v2, v2])
P_23 = np.array([P2, P3])

# isentropic expansion 3→4
v_34 = np.linspace(v2, v1, 200)
P_34 = P3 * (v3**gamma) / (v_34**gamma)

# constant volume 4→1
v_41 = np.array([v1, v1])
P_41 = np.array([P4, P1])

#T–s DATA
# constant volume 2→3
T_23 = np.linspace(T2, T3, 200)
s_23 = s2 + cv * np.log(T_23/T2)

# constant volume 4→1
T_41 = np.linspace(T4, T1, 200)
s_41 = s4 + cv * np.log(T_41/T4)

# P–v Plot
plt.figure(figsize=(7,5))
plt.plot(v_12, P_12/1000)
plt.plot(v_23, P_23/1000)
plt.plot(v_34, P_34/1000)
plt.plot(v_41, P_41/1000)

# State points
v_states = [v1, v2, v3, v4, v1]
P_states = [P1, P2, P3, P4, P1]
plt.scatter(v_states, np.array(P_states)/1000)
for i, (v, p) in enumerate(zip(v_states[:-1], P_states[:-1])):
    plt.text(v, p/1000, f" {i+1}")

plt.xlabel("Specific Volume (m³/kg)")
plt.ylabel("Pressure (kPa)")
plt.title("P–v Diagram of Ideal Otto Cycle")
plt.grid(True)

#T–s Plot
plt.figure(figsize=(7,5))

# 2→3
plt.plot(s_23, T_23)
# 3→4
plt.plot([s3, s3], [T3, T4])
# 4→1
plt.plot(s_41, T_41)
# 1→2
plt.plot([s1, s1], [T1, T2])

# State points
s_states = [s1, s2, s3, s4, s1]
T_states = [T1, T2, T3, T4, T1]
plt.scatter(s_states, T_states)
for i, (s, T) in enumerate(zip(s_states[:-1], T_states[:-1])):
    plt.text(s, T, f" {i+1}")

plt.xlabel("Entropy (J/kg·K) (relative)")
plt.ylabel("Temperature (K)")
plt.title("T–s Diagram of Ideal Otto Cycle")
plt.grid(True)

plt.show()
