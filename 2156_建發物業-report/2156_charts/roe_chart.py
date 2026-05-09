import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

fin = pd.DataFrame([
    {'Year':2017,'ROE':65.4,'ROA':1.9,'Net_Margin':7.3,'Debt_Asset':96.8,'Gross_Margin':26.2},
    {'Year':2018,'ROE':90.2,'ROA':3.2,'Net_Margin':7.9,'Debt_Asset':95.9,'Gross_Margin':23.1},
    {'Year':2019,'ROE':57.9,'ROA':4.6,'Net_Margin':8.5,'Debt_Asset':88.6,'Gross_Margin':22.9},
    {'Year':2020,'ROE':36.6,'ROA':8.0,'Net_Margin':10.4,'Debt_Asset':62.2,'Gross_Margin':24.5},
    {'Year':2021,'ROE':22.5,'ROA':8.6,'Net_Margin':10.2,'Debt_Asset':60.5,'Gross_Margin':25.0},
    {'Year':2022,'ROE':21.9,'ROA':8.4,'Net_Margin':10.8,'Debt_Asset':61.5,'Gross_Margin':23.4},
    {'Year':2023,'ROE':31.5,'ROA':13.1,'Net_Margin':13.1,'Debt_Asset':51.8,'Gross_Margin':28.1},
    {'Year':2024,'ROE':18.5,'ROA':8.4,'Net_Margin':9.8,'Debt_Asset':53.3,'Gross_Margin':21.5},
    {'Year':2025,'ROE':19.0,'ROA':8.5,'Net_Margin':9.6,'Debt_Asset':55.0,'Gross_Margin':21.2},
])
fin.set_index('Year', inplace=True)

fig, axes = plt.subplots(2, 2, figsize=(16, 10), dpi=110)
fig.suptitle('建發物業 (2156.HK) — ROE / Return Diagnostic & Quality Metrics', fontsize=13, fontweight='bold')

# ROE / ROA
ax = axes[0,0]
ax.bar(fin.index, fin['ROE'], color='steelblue', alpha=0.8, label='ROE')
ax.bar(fin.index, fin['ROA'], color='coral', alpha=0.8, label='ROA')
ax.axhline(15, color='green', linestyle='--', linewidth=1, label='ROE target 15%')
ax.set_title('ROE & ROA (%)')
ax.legend()
ax.set_ylabel('%')
ax.grid(axis='y', alpha=0.3)
for i, (yr, row) in enumerate(fin.iterrows()):
    ax.text(yr, row['ROE']+1, f"{row['ROE']:.0f}%", ha='center', fontsize=7)
    ax.text(yr, row['ROA']+1, f"{row['ROA']:.0f}%", ha='center', fontsize=7)

# Margins
ax2 = axes[0,1]
ax2.plot(fin.index, fin['Gross_Margin'], 'o-', color='green', label='Gross Margin', linewidth=2)
ax2.plot(fin.index, fin['Net_Margin'], 's-', color='blue', label='Net Margin', linewidth=2)
ax2.set_title('Gross Margin & Net Margin (%)')
ax2.legend()
ax2.grid(alpha=0.3)
for yr, row in fin.iterrows():
    ax2.text(yr, row['Gross_Margin']+0.5, f"{row['Gross_Margin']:.1f}%", ha='center', fontsize=7, color='green')
    ax2.text(yr, row['Net_Margin']-1.0, f"{row['Net_Margin']:.1f}%", ha='center', fontsize=7, color='blue')

# Debt/Asset
ax3 = axes[1,0]
ax3.bar(fin.index, fin['Debt_Asset'], color='darkred', alpha=0.7)
ax3.axhline(60, color='orange', linestyle='--', label='Warning 60%')
ax3.axhline(50, color='green', linestyle='--', label='Target <50%')
ax3.set_title('Debt / Total Assets (%)')
ax3.set_ylabel('%')
ax3.legend()
ax3.grid(axis='y', alpha=0.3)
for yr, row in fin.iterrows():
    ax3.text(yr, row['Debt_Asset']+1, f"{row['Debt_Asset']:.0f}%", ha='center', fontsize=8)

# Revenue & Net Profit growth
rev = [447051000,608618000,801330000,1028574000,1556645000,2290473000,3569324000,3292901000,3880549000]
np_ = [30750000,47835000,68181000,106118000,159374000,247212000,467347000,323477000,358909000]
years = list(fin.index)
ax4 = axes[1,1]
ax4_twin = ax4.twinx()
l1 = ax4.bar([y-0.2 for y in years], [r/1e6 for r in rev], 0.4, label='Revenue', color='steelblue', alpha=0.7)
l2 = ax4_twin.plot(years, [n/r*100 for n,r in zip(np_,rev)], 'o-', color='crimson', linewidth=2, label='Net Margin %')
ax4.set_title('Revenue (HKD M) + Net Margin %')
ax4.set_ylabel('Revenue (HKD M)', color='steelblue')
ax4_twin.set_ylabel('Net Margin %', color='crimson')
ax4.grid(axis='y', alpha=0.3)
lines = [l1, l2[0]]
ax4.legend(lines, ['Revenue (HKD M)', 'Net Margin %'], loc='upper left')

plt.tight_layout()
plt.savefig('/Users/kenneth/.openclaw/workspace/analysis/2156_charts/roe_chart.png', dpi=110, bbox_inches='tight')
plt.close()
print("ROE chart saved")
