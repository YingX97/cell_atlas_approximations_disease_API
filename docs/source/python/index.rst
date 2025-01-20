.. note::
   This package is under active development. A testing version is available on Test PyPI.
   
Quickstart
----------
Install with:

.. code-block:: bash

   pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ atlasapprox-disease==0.1.0.dev1

To use:

.. code-block:: python

   import atlasapprox_disease as aad
   api = aad.API()
   result = api.differential_gene_expression(disease="COVID", cell_type="T cell", top_n=10)
