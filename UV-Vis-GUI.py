from matplotlib.widgets import Cursor
import pandas as pd
import matplotlib.pyplot as plt

LOWER_LIMIT, UPPER_LIMIT = 200, 1000

# import dataframe
df_absorbance = pd.read_excel("data/200-1000_Absorbance.xlsx")
df_reflectance = pd.read_excel("data/200-1000_Reflectance.xlsx")

# get clean dataframe
df_absorbance = df_absorbance.dropna().loc[
    (df_absorbance["Wavelength/ nm"] >= LOWER_LIMIT) & (df_absorbance["Wavelength/ nm"] <= UPPER_LIMIT)
]
df_reflectance = (
    df_reflectance.drop(columns=df_reflectance.columns[4:])
    .dropna()
    .loc[(df_reflectance["Wavelength/ nm"] >= LOWER_LIMIT) & (df_reflectance["Wavelength/ nm"] <= UPPER_LIMIT)]
)

# print(df_reflectance)
# print(df_absorbance)

plt.figure(figsize=(13, 6))
ax_absorbance = plt.subplot(1, 2, 1)
ax_absorbance.plot(df_absorbance["Wavelength/ nm"], df_absorbance.iloc[:, 1:4], label=df_absorbance.columns[1:])
ax_absorbance.set_xlabel("Wavelength (nm)")
ax_absorbance.set_ylabel("Absorbance (%)")
ax_absorbance.set_title("Absorbance vs Wavelength")
ax_absorbance.legend()
cursor_absorbance = Cursor(ax_absorbance, color="k", linewidth=1)
ax_absorbance.grid()

ax_reflectance = plt.subplot(1, 2, 2)
ax_reflectance.plot(df_reflectance["Wavelength/ nm"], df_reflectance.iloc[:, 1:4], label=df_reflectance.columns[1:])
ax_reflectance.set_xlabel("Wavelength (nm)")
ax_reflectance.set_ylabel("Reflectance (%)")
ax_reflectance.set_title("Reflectance vs Wavelength")
ax_reflectance.legend()
cursor_reflectance = Cursor(ax_reflectance, color="k", linewidth=1)
ax_reflectance.grid()
plt.tight_layout()
plt.show()
