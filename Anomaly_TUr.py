import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use(['dark_background'])

year, Mean_Anomaly, ssp_585= np.loadtxt('UR_ano.txt', unpack=True,skiprows=3)
fig = plt.figure()
ax = fig.add_subplot(111)

# Plot ages with male or female symbols as markers
ax.plot(year, ssp_585, marker='o', markersize=4, c='#FBF5DF', lw=1.5,
        mfc='#FBF5DF', mec='#FBF5DF')
ax.plot(year, Mean_Anomaly, c='#C60C30', lw=3,
        mfc='#C60C30', mec='#C60C30')

#===============Legend guide
ax.legend(["MPI-ESM1-2-HR_ssp585", "Mean Anomaly"],
          fontsize=5,facecolor ='#2c2b27', loc="lower right")
#===============

ax.set_xlabel('Year',weight='bold')
ax.set_ylabel('Surface Temperature Anomalies (°C)',size=8,weight='bold')
plt.figtext(0.45, 0.95, '©2024 Morteza Sharif',size=8,weight='bold')#,rotation=-45
plt.figtext(0.45, 0.92,'ULB Anomaly IPCC 1979-2100',size=8,weight='bold')
plt.figtext(0.45, 0.89,'CMIP6 Data https://climate-scenarios.canada.ca',size=8,weight='bold')


#===============Line 
plt.hlines(y=-0.5,xmin=1979,xmax=2100,color='#6CA0DC',linestyle='--',alpha=0.99,lw=2)
plt.hlines(y=0,xmin=1979,xmax=2100,color='#FBF5DF',linestyle='--',alpha=0.55,lw=2)
plt.hlines(y=0.5,xmin=1979,xmax=2100,color='#FDA172',linestyle='--',alpha=0.75,lw=2)
plt.hlines(y=1,xmin=1979,xmax=2100,color='#ED7014',linestyle='--',alpha=0.99,lw=2)
plt.hlines(y=1.5,xmin=1979,xmax=2100,color='#c70000',linestyle='--',alpha=0.85,lw=2)
#===============

#===============Text in Fig
plt.annotate('1.5 °C', xy =(1978.5, 1.580),fontsize = 8, weight='bold',color = '#c70000')
plt.annotate('1 °C', xy =(1978.5, 1.075),fontsize = 8, weight='bold',color = '#ED7014')
plt.annotate('0.5 °C', xy =(1978.5, 0.615),fontsize = 8, weight='bold',color = '#FDA172')
plt.annotate('-0.5 °C', xy =(1978.5, -0.395),fontsize = 8, weight='bold',color = '#6CA0DC')
#===============


#ax.grid()
fig.canvas.draw()

plt.show()
