#Kikuyu_research/AGRO2025_Conference/linear_predictions_1981_2022.py
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Load and format the CSV data
df = pd.read_csv("linear_predictions_1981_2022.csv")
df["year"] = df["year"].astype(int)
df["y_true"] = df["y_true"].map("{:.4f}".format)
df["y_pred"] = df["y_pred"].map("{:.4f}".format)
df["residual"] = df["residual"].map("{:.4f}".format)

# 1. Generate Table Image
fig, ax = plt.subplots(figsize=(10, len(df) * 0.40))
ax.axis('off')

table = ax.table(
    cellText=df.values,
    colLabels=["Year", "y_true", "y_pred", "residual"],
    cellLoc='center',
    loc='center'
)

table.scale(1, 1.5)
table.auto_set_font_size(False)
table.set_fontsize(10)

for cell in table.get_celld().values():
    cell.set_edgecolor("white")
    cell.set_linewidth(0)

# Bold header text
ncols = len(df.columns)
for c in range(ncols):
    table[(0, c)].set_text_props(weight='bold')

fig.canvas.draw()

cells = table.get_celld()
x_left  = min(cell.get_x() for cell in cells.values())
x_right = max(cell.get_x() + cell.get_width() for cell in cells.values())
y_bot   = min(cell.get_y() for cell in cells.values())
y_top   = max(cell.get_y() + cell.get_height() for cell in cells.values())

header_h = cells[(0, 0)].get_height()
y_header_sep = y_top - header_h

eps_x = 0.002
eps_y = 0.002
x1, x2 = x_left + eps_x, x_right - eps_x
y_top_in    = y_top - eps_y
y_header_in = y_header_sep - eps_y
y_bot_in    = y_bot + eps_y

for y in (y_top_in, y_header_in, y_bot_in):
    ax.add_line(Line2D([x1, x2], [y, y],
                       transform=ax.transAxes, color="black", linewidth=1.2))

plt.savefig("maize_yield_comparison_table.png", bbox_inches='tight', dpi=300)
plt.close()

# 2. Generate Line Plot 
df_plot = pd.read_csv("linear_predictions_1981_2022.csv")

fig, ax = plt.subplots(figsize=(12, 6))

# Plot actual yield
ax.plot(df_plot['year'], df_plot['y_true'], color='green', linewidth=2.5, label='Actual Yield')
ax.scatter(df_plot['year'], df_plot['y_true'], color='yellow', edgecolor='black', s=80, label='Actual (y_true)', zorder=3)

# Plot predicted yield
ax.plot(df_plot['year'], df_plot['y_pred'], color='green', linewidth=2.5, linestyle='--', label='Predicted Yield')
ax.scatter(df_plot['year'], df_plot['y_pred'], color='orange', edgecolor='black', s=80, label='Predicted (y_pred)', zorder=3)

ax.set_xticks(range(df_plot['year'].min(), df_plot['year'].max() + 1, 5))
ax.set_title("Maize Yield Predictions vs Actuals (1981–2022)", fontsize=16)
ax.set_xlabel("Year")
ax.set_ylabel("Yield (t/ha)")
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.savefig("maize_yield_comparison.png", dpi=300, bbox_inches='tight')
plt.close()
