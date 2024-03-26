
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

color = {"Adelie": "blue", "Gentoo": "orange", "Chinstrap": "green"}

for species in ["Adelie", "Gentoo", "Chinstrap"]:
    penguins[penguins["species"] == species].plot.scatter("bill_length_mm", "bill_depth_mm", color=color[species], ax=ax1)
    penguins[penguins["species"] == species].plot.scatter("flipper_length_mm", "body_mass_g", color=color[species], ax=ax2)

ax1.set_xlabel("bill length (mm)")
ax1.set_ylabel("bill depth (mm)")

ax2.set_xlabel("flipper length (mm)")
ax2.set_ylabel("body mass (g)")

None