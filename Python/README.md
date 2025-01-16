Python interface to disease-related cell atlas approximations
=============================================

`atlasapprox_disease` is a Python interface designed to provide easy access to disease-related cell atlas data. Built using the [cellxgene census](https://github.com/chanzuckerberg/cellxgene-census) as the initial data source and powered by the [scquill approximation algorithm](https://github.com/fabilab/scquill/), this package enables researchers to explore thousands of datasets efficiently. 

The package enables researchers to address complex biological questions across multiple organs, cell types, and disease conditions such as:

- *What is the expression of a specific gene in a specific disease across all datasets?*
- *In COVID-19, what is the differential cell abundance of each cell type between normal and disease states?*
- *What are the top 20 most differentially expressed genes in kidney disease?*

---

## Features

- **Differential Analysis**:
  - Differential gene expression.
  - Differential cell type abundance.
- **Top Measurements**:
  - Identify the highest measurements for genes or cell types across datasets.
- **Additional Capabilities**:
	-Retrieve metadata for datasets, organs, and cell types.
	-Calculate average gene expression values.
	-Determine the fraction of cells expressing specific genes.
	-Generate dot plots to visualize gene expression patterns.

---

## Installation

Install the development version of the package from Test PyPI:
```bash
TODO
