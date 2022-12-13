# phys261lab1
This repo contains all the code I used in my analysis of the data collected in the first lab

## Calculations
The estimation of slope at a given point is calculated by finding the average of the secant lines of $t$ and its nearest neighboring points.


$$T = \text{temperature (degrees Celcius)}$$

$$t = \text{time (seconds)}$$

Simply, slope

$$m=\frac{\Delta{T}}{\Delta{t}}$$

$$m = \frac{\frac{T_t-T_{t-0.5}}{t - (t - 0.5)} + \frac{T_{t+0.5} - T_t}{(t + 0.5) - t}}{2}$$

