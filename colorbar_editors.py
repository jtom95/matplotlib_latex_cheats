from typing import List
import matplotlib.pyplot as plt

# add \small to all the labels of the colorbar
def get_colorbars_axes_from_fig(fig: plt.Figure) -> List[plt.Axes]:
    colorbars = []
    for ax in fig.axes:
        if ax.get_label() == "<colorbar>":
            colorbars.append(ax)
    return colorbars



