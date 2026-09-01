# Heat-Map

Interpolation and 3D visualization of a coarse sensor grid, including mapping it onto a cylinder and closing the seam.

Written during a lab practicum at **OSTA Lab, Hanyang University** (2023), on measuring battery cell temperature distribution with an optical fiber sensor — optical frequency domain reflectometry (OFDR) for distributed temperature sensing.

All four scripts run on a 5×10 array of random values (`np.random.random((5, 10))`) rather than measurement data, so they show the method rather than any result.

## The scripts

Each one interpolates the coarse grid with `scipy.interpolate.griddata` and plots the result. The recurring comparison is **linear against cubic** interpolation.

| Script | What it does |
| --- | --- |
| `Interpolation_of_a_5x10_random_array.py` | Interpolates onto a 50×100 grid and shows three stacked `imshow` panels: original, linear, cubic |
| `Interpolation_and_3Dvisualization_of_a_5x10_random_array.py` | Same comparison on a 100×200 grid, drawn as a 3D scatter plot |
| `Visualization_of_a_5x10_random_array_on_a_cylinder.py` | Wraps the grid onto a cylinder — the 5 rows map around the circumference, the 10 columns become height — and plots linear and cubic side by side |
| `Visualization_of_a_5x10_random_array_on_a_cylinder_with_seam_interpolation.py` | The same cylinder, but interpolated across the seam |

## The seam

A fiber wrapped around a cylinder produces a grid whose first and last rows are physically adjacent: on the cell they are neighbours, even though they sit at opposite ends of the array. Interpolating the array as-is leaves a discontinuity along that line.

The seam version appends the first row to the end of the array before interpolating, so the surface closes continuously all the way around.

## Running

```bash
pip install numpy pandas scipy matplotlib
python Interpolation_and_3Dvisualization_of_a_5x10_random_array.py
```
