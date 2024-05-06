from typing import List, Literal
import matplotlib.pyplot as plt
from .constants import DistanceUnits


def set_all_axes_ticks_to_small_in_latex(
    fig: plt.Figure,
    fontsize=12,
    instruction="\small",
    distance_units: Literal["m", "cm", "mm", "um", "nm"] = "m",
):
    axes = fig.get_axes()
    if isinstance(distance_units, str):
        distance_units = DistanceUnits[distance_units]

    multiplier = 1 / distance_units.value
    for ax in axes:
        ax.yaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, _: r"{}{{{:.1f}}}".format(instruction, x * multiplier))
        )
        ax.xaxis.set_major_formatter(
            plt.FuncFormatter(lambda x, _: r"{}{{{:.1f}}}".format(instruction, x * multiplier))
        )
        ax.yaxis.set_tick_params(labelsize=fontsize)
        ax.xaxis.set_tick_params(labelsize=fontsize)
    return fig


def set_axes_ticks_to_small_in_latex(
    axes: List[plt.Axes],
    fontsize=12,
    instruction="\small",
    distance_units: Literal["m", "cm", "mm", "um", "nm"] = "m",
    which_axis: Literal["x", "y", "both"] = "both",
    number_of_decimals: int = 1,
):
    if isinstance(axes, plt.Axes):
        axes = [axes]
    if isinstance(distance_units, str):
        distance_units = DistanceUnits[distance_units]

    multiplier = 1 / distance_units.value
    for ax in axes:
        if which_axis in ["y", "both"]:
            ax.yaxis.set_major_formatter(
                plt.FuncFormatter(lambda x, _: r"{}{{{:.{}f}}}".format(instruction, x * multiplier, number_of_decimals))
            )
            ax.yaxis.set_tick_params(labelsize=fontsize)
        if which_axis in ["x", "both"]:
            ax.xaxis.set_major_formatter(
                plt.FuncFormatter(lambda x, _: r"{}{{{:.{}f}}}".format(instruction, x * multiplier, number_of_decimals))
            )
            ax.xaxis.set_tick_params(labelsize=fontsize)

    return axes[0].get_figure()
