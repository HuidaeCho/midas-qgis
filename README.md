# Memory-Efficient I/O-Improved Drainage Analysis System (MIDAS) QGIS Plugin

The [MIDAS QGIS plugin](https://plugins.qgis.org/plugins/midas/) offers memory-efficient, OpenMP-parallelized algorithms for computing hydrologic parameters. [MIDAS](https://github.com/HuidaeCho/midas) executable files need to be installed separately in `PATH`.

## Related projects

* [MIDAS](https://github.com/HuidaeCho/midas): Core C library and executables (required for all Python, R, and QGIS interfaces)
* [r.flowaccumulation](https://grass.osgeo.org/grass-stable/manuals/addons/r.flowaccumulation.html): [GRASS](https://grass.osgeo.org/) addon for [MEFA](https://github.com/HuidaeCho/mefa)
* [r.hydrobasin](https://grass.osgeo.org/grass-stable/manuals/addons/r.hydrobasin.html): [GRASS](https://grass.osgeo.org/) addon for [MESHED](https://github.com/HuidaeCho/meshed)
* [r.lfp](https://grass.osgeo.org/grass-stable/manuals/addons/r.lfp.html): [GRASS](https://grass.osgeo.org/) addon for [MELFP](https://github.com/HuidaeCho/melfp)
* [MIDASFlow](https://github.com/HuidaeCho/midasflow): Python package
* [MIDASFlow-R](https://github.com/HuidaeCho/midasflow-r): R package

## Installation

```sh
cd ~/.local/share/QGIS/QGIS3/profiles/default/python/plugins
git clone https://github.com/HuidaeCho/midas-qgis.git
```

## References

* [MEFA](https://github.com/HuidaeCho/mefa) (Flow Accumulation): Huidae Cho, July 2023. Memory-Efficient Flow Accumulation Using a Look-Around Approach and Its OpenMP Parallelization. Environmental Modelling & Software 167, 105771. [doi:10.1016/j.envsoft.2023.105771](https://doi.org/10.1016/j.envsoft.2023.105771). [Author's Version](https://idea.isnew.info/publications/Memory-efficient%20flow%20accumulation%20using%20a%20look-around%20approach%20and%20its%20OpenMP%20parallelization%20-%20Cho.2023.pdf).
* [MESHED](https://github.com/HuidaeCho/meshed) (Watershed Delineation): Huidae Cho, January 2025. Avoid Backtracking and Burn Your Inputs: CONUS-Scale Watershed Delineation Using OpenMP. Environmental Modelling & Software 183, 106244. [doi:10.1016/j.envsoft.2024.106244](https://doi.org/10.1016/j.envsoft.2024.106244). [Author's Version](https://idea.isnew.info/publications/Avoid%20backtracking%20and%20burn%20your%20inputs:%20CONUS-scale%20watershed%20delineation%20using%20OpenMP%20-%20Cho.2025.pdf).
* [MELFP](https://github.com/HuidaeCho/melfp) (Longest Flow Path): Huidae Cho, September 2025. Loop Then Task: Hybridizing OpenMP Parallelism to Improve Load Balancing and Memory Efficiency in Continental-Scale Longest Flow Path Computation. Environmental Modelling & Software 193, 106630. [doi:10.1016/j.envsoft.2025.106630](https://doi.org/10.1016/j.envsoft.2025.106630). [Author's Version](https://idea.isnew.info/publications/Loop%20then%20task%20-%20Hybridizing%20OpenMP%20parallelism%20to%20improve%20load%20balancing%20and%20memory%20efficiency%20in%20continental-scale%20longest%20flow%20path%20computation%20-%20Cho.2025.pdf).
