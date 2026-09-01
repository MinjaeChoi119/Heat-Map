# Heat-Map

Interpolation and 3D visualization of temperature sensor grids, written during a lab practicum at **OSTA Lab, Hanyang University** (Feb–Jun 2023) on optical frequency domain reflectometry (OFDR) for distributed temperature sensing on Li-ion battery cells.

An OFDR fiber gives temperature readings at discrete points along its length. Wrapped around a cell, that becomes a coarse grid of samples that has to be turned into a continuous surface before anyone can see where the cell is actually getting hot.

These scripts run on a 5×10 randomly generated array rather than the lab's measurements, so the method can be shown without publishing unpublished experimental data.

## Scripts

| Script | What it does |
| --- | --- |
| `Interpolation_of_a_5x10_random_array.py` | Interpolates the coarse 5×10 grid into a smooth 2D temperature field |
| `Interpolation_and_3Dvisualization_of_a_5x10_random_array.py` | Same interpolation, rendered as a 3D surface |
| `Visualization_of_a_5x10_random_array_on_a_cylinder.py` | Maps the grid onto a cylinder — the geometry of a cylindrical cell with fiber wrapped around it |
| `Visualization_of_a_5x10_random_array_on_a_cylinder_with_seam_interpolation.py` | Same, but interpolating across the seam so the surface is continuous all the way around |

## Why the seam matters

A fiber wrapped around a cylinder produces a grid whose first and last columns are physically adjacent — they are neighbours on the cell even though they sit at opposite ends of the array. Interpolating the flat array leaves a visible discontinuity down that line, and it lands exactly where a reader would otherwise look for a hot spot.

The seam-interpolation version treats the horizontal axis as periodic, so the surface closes cleanly and the wrap line stops being an artifact.

## Running

```bash
pip install numpy scipy matplotlib
python Interpolation_and_3Dvisualization_of_a_5x10_random_array.py
```

The lab work itself was done in MATLAB; these are the Python re-implementations of the visualization method.
