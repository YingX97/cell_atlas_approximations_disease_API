.. atlasapprox-disease documentation master file, created by
   sphinx-quickstart on Fri Jan 17 14:05:38 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

API for disease cell atlas approximations
===============================================

Cell Atlas Approximation (Disease) is a lightweight API designed for analyzing approximated single-cell transcriptomics data, using CellxGene Census as its initial data source."

Example of API usage:

- Perform differential gene expression analysis between disease and normal conditions for a specific cell type.
- Compare differential cell type abundance across diseases, organs, or developmental stages.
- Ask the average expression of a set of genes across different cell types, tissues, and diseases.

Version
-------
The most recent version of the API is **v1**.

Interfaces
----------
There are multiple ways to access atlas approximations programmatically:

.. toctree::
   :maxdepth: 1

   Python <python/index>
   R <R/index>
   JavaScript <js/index>
   UNIX shell (bash, zsh, etc.) <sh/index>
   REST (language-agnostic) <rest/index>

.. note::
   The **REST API** is the primary interface and is fully functional.  
   The **Python, R, and JavaScript interfaces are currently under development** and will be released soon.

Authors
-------
This project is developed and maintained by:
**Fabio Zanini**, **Ying Xu**

Affiliated with **[Fabilab](https://fabilab.org)**.

Citation
--------
**Xu et al.** (2024) Lightweight and scalable approximations democratise access to single cell atlases. `biorxiv <https://www.biorxiv.org/content/10.1101/2024.01.03.573994v1>`_.