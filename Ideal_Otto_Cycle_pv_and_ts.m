%%This file shows the pv and ts diagrams for an ideal otto cycle
clear; clc; close all;

%INPUT PARAMETERS
compression_ratio = 8;       
gamma = 1.4;                 
R = 287;                     
cp = gamma * R / (gamma - 1);
cv = cp - R;
T1 = 300;  
T3 = 1500;
P1 = 101325;                

%STATE 1
v1 = R * T1 / P1;            
v2 = v1 / compression_ratio;

%1-2 (isentropic compression)
T2 = T1 * (compression_ratio)^(gamma - 1);
P2 = P1 * (compression_ratio)^gamma;

v_12 = linspace(v1, v2, 200);
P_12 = P1 * (v1 ./ v_12).^gamma;
T_12 = T1 * (v1 ./ v_12).^(gamma - 1);

% Constant-volume heat addition (2→3)
P3 = P2 * (T3 / T2);
v3 = v2;

%PROCESS 3-4 (isentropic expansion)
T4 = T3 / (compression_ratio)^(gamma - 1);
P4 = P3 / (compression_ratio)^gamma;
v4 = v1;

v_34 = linspace(v3, v4, 200);
P_34 = P3 * (v3 ./ v_34).^gamma;
T_34 = T3 * (v3 ./ v_34).^(gamma - 1);

%TEMPERATURE–ENTROPY CALCULATIONS
s1 = 0;
s2 = s1;
s3 = s2 + cv * log(T3 / T2);
s4 = s3;

s_12 = s1 * ones(size(T_12));
s_23 = linspace(s2, s3, 200);
s_34 = s3 * ones(size(T_34));
s_41 = linspace(s4, s1, 200);

T_23 = linspace(T2, T3, 200);
T_41 = linspace(T4, T1, 200);

%P–V DIAGRAM
figure;
plot(v_12, P_12, 'LineWidth', 2); hold on;
plot([v2 v3], [P2 P3], 'LineWidth', 2);
plot(v_34, P_34, 'LineWidth', 2);
plot([v4 v1], [P4 P1], 'LineWidth', 2);

text(v1, P1, ' 1', 'FontSize', 12, 'FontWeight', 'bold');
text(v2, P2, ' 2', 'FontSize', 12, 'FontWeight', 'bold');
text(v3, P3, ' 3', 'FontSize', 12, 'FontWeight', 'bold');
text(v4, P4, ' 4', 'FontSize', 12, 'FontWeight', 'bold');

xlabel('Volume (m^3/kg)');
ylabel('Pressure (Pa)');
title('P–V Diagram of Ideal Otto Cycle');
grid on;

%T–S DIAGRAM
figure;
plot(s_12, T_12, 'LineWidth', 2); hold on;
plot(s_23, T_23, 'LineWidth', 2);
plot(s_34, T_34, 'LineWidth', 2);
plot(s_41, T_41, 'LineWidth', 2);

text(s1, T1, ' 1', 'FontSize', 12, 'FontWeight', 'bold');
text(s2, T2, ' 2', 'FontSize', 12, 'FontWeight', 'bold');
text(s3, T3, ' 3', 'FontSize', 12, 'FontWeight', 'bold');
text(s4, T4, ' 4', 'FontSize', 12, 'FontWeight', 'bold');

xlabel('Entropy (J/kg·K)');
ylabel('Temperature (K)');
title('T–S Diagram of Ideal Otto Cycle');
grid on;


