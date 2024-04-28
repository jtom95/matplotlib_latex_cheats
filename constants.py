from enum import Enum
from typing import Tuple, List
import numpy as np


ANGLES2ORIENTATION = {"X": [np.pi / 2, 0], "Y": [np.pi / 2, np.pi / 2], "Z": [0, 0]}

class Orientations(Enum):
    X = "x"
    Y = "y"
    Z = "z"
    UNK = "unknown"

    @classmethod
    def from_angles(cls, theta: float, phi: float, deg: bool=False) -> "Orientations":
        if deg:
            theta = np.deg2rad(theta)
            phi = np.deg2rad(phi)
        if np.isclose(theta, np.pi / 2):
            if np.isclose(phi, 0):
                return cls.X
            if np.isclose(phi, np.pi / 2):
                return cls.Y
        if np.isclose(theta, 0):
            return cls.Z
        return cls.UNK

    @staticmethod
    def to_angles(orientation: "Orientations") -> Tuple[float, float]:
        if orientation == Orientations.X:
            return np.pi / 2, 0
        if orientation == Orientations.Y:
            return np.pi / 2, np.pi / 2
        if orientation == Orientations.Z:
            return 0, 0
        return np.nan, np.nan


class ProbeTypes(Enum):
    Exy = "Exy"
    Ez = "Ez"
    Hxy = "Hxy"
    Hz = "Hz"
    UNK = "unknown"


class FieldComponents(Enum):
    X = "x"
    Y = "y"
    Z = "z"
    UNK = "unknown"


class FieldTypes(Enum):
    E = "E"
    H = "H"
    UNK = "unknown"


class MeasuremeableFields(Enum):
    Ex = "Ex"
    Ey = "Ey"
    Ez = "Ez"
    Hx = "Hx"
    Hy = "Hy"
    Hz = "Hz"
    UNK = "unknown"
    
    @classmethod
    def from_field_type_and_orientation(cls, fieldtype: FieldTypes, orientation: Orientations) -> "MeasuremeableFields":
        if isinstance(orientation, Orientations):
            orientation = orientation.value
        return field_and_component_to_quid(fieldtype, orientation)


class FrequencyUnits(Enum):
    Hz = 1
    kHz = 1e3
    MHz = 1e6
    GHz = 1e9


class DistanceUnits(Enum):
    m = 1
    cm = 1e-2
    mm = 1e-3
    um = 1e-6
    nm = 1e-9


class VoltageUnits(Enum):
    V = 1
    mV = 1e-3
    uV = 1e-6
    nV = 1e-9
    pV = 1e-12
    fV = 1e-15

class CurrentUnits(Enum):
    A = 1
    mA = 1e-3
    uA = 1e-6
    nA = 1e-9
    pA = 1e-12
    fA = 1e-15

class ScalingUnits(Enum):
    linear = "linear"
    dB = "dB"


def field_and_component_to_quid(fieldtype: FieldTypes, component: FieldComponents) -> MeasuremeableFields:
    if isinstance(fieldtype, str):
        fieldtype = FieldTypes(fieldtype)
    if isinstance(component, str):
        component = FieldComponents(component)
    
    if fieldtype == FieldTypes.E:
        if component == FieldComponents.X:
            return MeasuremeableFields.Ex
        if component == FieldComponents.Y:
            return MeasuremeableFields.Ey
        if component == FieldComponents.Z:
            return MeasuremeableFields.Ez
    if fieldtype == FieldTypes.H:
        if component == FieldComponents.X:
            return MeasuremeableFields.Hx
        if component == FieldComponents.Y:
            return MeasuremeableFields.Hy
        if component == FieldComponents.Z:
            return MeasuremeableFields.Hz
    raise ValueError(f"fieldtype {fieldtype} and component {component} are not valid")
