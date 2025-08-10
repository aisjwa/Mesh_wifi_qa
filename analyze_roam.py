import pandas as pd, matplotlib.pyplot as plt, os
os.makedirs('reports', exist_ok=True)
# Synthetic roam window
df = pd.DataFrame({'t': list(range(40)), 'ap': ['GW']*20 + ['SAT1']*20, 'loss': [0]*19 + [0.03] + [0]*20})
plt.figure()
plt.plot(df['t'], [ -55 - (i%10) for i in range(40) ])
plt.axvline(20, linestyle='--'); plt.title('Roam timeline (synthetic)')
plt.xlabel('time'); plt.ylabel('RSSI (dBm)'); plt.savefig('reports/roam_timeline.png', dpi=160)
print('Saved reports/roam_timeline.png')
