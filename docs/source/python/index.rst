AtlasApprox Disease - Python API
================================

This Python package provides a convenient interface to access the **atlasapprox-disease** REST API, enabling efficient querying of disease-related cell atlas approximations.

Installation
------------
To install the latest version of the package:

.. code-block:: bash

    pip install atlasapprox-disease

To install the package locally:

.. code-block:: bash

    pip install -e .

Getting Started
---------------
To use the API, import the `atlasapprox_disease` package and create an API instance:

.. code-block:: python

    import atlasapprox_disease as aad

    api = aad.API()

API Reference
-------------

API Object
++++++++++
.. autoclass:: atlasapprox_disease.API
   :members:
   :undoc-members:
   :show-inheritance: