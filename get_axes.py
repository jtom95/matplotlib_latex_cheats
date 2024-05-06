from typing import List
import matplotlib.pyplot as plt

# add \small to all the labels of the colorbar
def get_colorbars_axes_from_fig(fig: plt.Figure) -> List[plt.Axes]:
    colorbars = []
    for ax in fig.axes:
        if ax.get_label() == "<colorbar>":
            colorbars.append(ax)
    return colorbars

def get_main_axes_from_fig(fig: plt.Figure) -> List[plt.Axes]:
    main_axes = []
    for ax in fig.axes:
        if ax.get_label() != "<colorbar>":
            main_axes.append(ax)
    return main_axes


