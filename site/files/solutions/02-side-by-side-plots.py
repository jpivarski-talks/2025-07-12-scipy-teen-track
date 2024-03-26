
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

penguins[penguins["species"] == "Adelie"].plot.scatter("bill_length_mm", "bill_depth_mm", color="blue", ax=ax1)
penguins[penguins["species"] == "Gentoo"].plot.scatter("bill_length_mm", "bill_depth_mm", color="orange", ax=ax1)
penguins[penguins["species"] == "Chinstrap"].plot.scatter("bill_length_mm", "bill_depth_mm", color="green", ax=ax1)
ax1.set_xlabel("bill length (mm)")
ax1.set_ylabel("bill depth (mm)")

penguins[penguins["species"] == "Adelie"].plot.scatter("flipper_length_mm", "body_mass_g", color="blue", ax=ax2)
penguins[penguins["species"] == "Gentoo"].plot.scatter("flipper_length_mm", "body_mass_g", color="orange", ax=ax2)
penguins[penguins["species"] == "Chinstrap"].plot.scatter("flipper_length_mm", "body_mass_g", color="green", ax=ax2)
ax2.set_xlabel("flipper length (mm)")
ax2.set_ylabel("body mass (g)")

None