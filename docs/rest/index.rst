REST API Guide
==============

Welcome to the atlasapprox-disease REST API documentation. This guide will help you understand how to use the REST API endpoints to interact with the atlasapprox-disease service.

Quick Start
-----------

.. tabs::

   .. tab:: **Python**

      .. code-block:: python
      
        import requests

        url = "https://disease-approximation-p523xiwksa-ts.a.run.app/differential_cell_type_abundance"
        params = {"disease_keyword": "flu"}

				# Make the POST request
				response = requests.post(url, params=params)

				# Pretty-print the JSON response

				data = response.json()
				print(json.dumps(data, indent=4))

.. _endpoints:

Reference API
=============

The complete API is described below. Endpoints refer to the end of the URL only. For instance, to query the differential cell type abundance for influenza, the **endpoint** description is ``/differential_cell_type_abundance`` so the full URL is ``https://disease-approximation-p523xiwksa-ts.a.run.app/differential_cell_type_abundance?disease_keyword=flu``.

.. contents::
   :local:

Differential Cell Type Abundance
++++++++++++++++++++++++++++++++

**Endpoint:** ``/differential_cell_type_abundance``

**Method:** ``POST``

**Description:**

Fetch differential cell type abundance for a given disease keyword or unique IDs.

**Parameters:**

- ``disease_keyword`` (str, optional): The keyword of the disease.
- ``unique_ids`` (list of str, optional): A list of unique IDs.

**Returns:**

An JSON Array: Each element in the array represents the differential abundance of a cell type and contains the following fields:
  - ``disease`` (str): The disease name.
  - ``dataset_title`` (str): Title of the dataset.
  - ``cell_type`` (str): The type of cell.
  - ``comparison`` (str): The type of comparison, usually "disease vs. normal".
  - ``condition`` (str): The condition being measured.
  - ``condition_baseline`` (str): The baseline condition for comparison.
  - ``normal_count`` (int): Count of the cell type in normal samples.
  - ``disease_count`` (int): Count of the cell type in disease samples.
  - ``normal_total_count`` (int): Total count of all cells in normal samples.
  - ``disease_total_count`` (int): Total count of all cells in disease samples.
  - ``normal_fraction`` (float): Fraction of the cell type in normal samples.
  - ``disease_fraction`` (float): Fraction of the cell type in disease samples.
  - ``delta_fraction`` (float): Difference between disease_fraction and normal_fraction.

**Example Request:**

.. code-block:: bash

    curl -X POST "https://disease-approximation-p523xiwksa-ts.a.run.app/differential_cell_type_abundance" -d "disease_keyword=flu"

**Example Response:**

.. code-block:: json

    [
       {
          "disease": "influenza",
          "dataset_title": "Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19",
          "cell_type": "blood cell",
          "comparison": "disease vs. normal",
          "condition": "disease",
          "condition_baseline": "normal",
          "normal_count": 309,
          "disease_count": 216,
          "normal_total_count": 17590,
          "disease_total_count": 10519,
          "normal_fraction": 0.0175667993177942,
          "disease_fraction": 0.020534271318566402,
          "delta_fraction": 0.0029674720007722005
       },
       ...
    ]

Differential Gene Expression
++++++++++++++++++++++++++++

**Endpoint:** ``/differential_gene_expression``

**Method:** ``POST``

**Description:**

Fetch differential gene expression for a given disease keyword, unique IDs, cell type keyword, and top N genes.

**Parameters:**

- ``disease_keyword`` (str, optional): The keyword of the disease.
- ``unique_ids`` (list of str, optional): A list of unique IDs.
- ``cell_type_keyword`` (str, optional): The type of cell.
- ``top_n`` (int, optional): The number of top genes to return. This will return both the top upregulated and top downregulated genes.

**Returns:**

An JSON Array: Each element in the array represents the differential expression of a gene and contains the following fields:
  - ``disease`` (str): The disease name.
  - ``dataset_title`` (str): Title of the dataset.
  - ``cell_type`` (str): The type of cell.
  - ``comparison`` (str): The type of comparison, usually "disease vs. normal".
  - ``condition`` (str): The condition being measured.
  - ``condition_baseline`` (str): The baseline condition for comparison.
  - ``regulation`` (str): Indicates if the gene is upregulated or downregulated.
  - ``feature_name`` (str): The gene identifier.
  - ``unit`` (str): Unit of measurement.
  - ``normal_expr`` (float): Expression level of the gene in normal samples.
  - ``disease_expr`` (float): Expression level of the gene in disease samples.
  - ``log_transformed`` (bool): Indicates if the data is log-transformed.
  - ``log2_fc`` (float): Log fold change of the gene expression.
  - ``normal_fraction`` (float): Fraction of the cell type expressing the gene in normal samples.
  - ``disease_fraction`` (float): Fraction of the cell type expressing the gene in disease samples.
  - ``delta_fraction`` (float): Difference between disease_fraction and normal_fraction.

**Example Request:**

.. code-block:: bash

    curl -X POST "https://disease-approximation-p523xiwksa-ts.a.run.app/differential_gene_expression" -d "disease_keyword=flu&cell_type_keyword=blood&top_n=5"

**Example Response:**

.. code-block:: json

    [
       {
          "disease": "influenza",
          "dataset_title": "Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19",
          "cell_type": "erythrocyte",
          "comparison": "disease vs. normal",
          "condition": "disease",
          "condition_baseline": "normal",
          "regulation": "up",
          "feature_name": "ENSG00000158578",
          "unit": "cptt",
          "normal_expr": 3.978105306625366,
          "disease_expr": 34.78181838989258,
          "log_transformed": false,
          "log2_fc": 2.845557928085327,
          "normal_fraction": 0.20652173459529877,
          "disease_fraction": 0.9579287767410278,
          "delta_fraction": 0.7514070272445679
       },
       ...
    ]

Fetch Metadata
++++++++++++++

**Endpoint:** ``/metadata``

**Method:** ``GET``

**Description:**

Fetch metadata for a given disease keyword.

**Parameters:**

- ``disease_keyword`` (str): The keyword of the disease.

**Returns:**

JSON Array: Each element in the array represents a dataset and contains the following fields:
  - ``unique_id`` (str): Unique identifier for the record.
  - ``disease`` (str): The disease name.
  - ``dataset_title`` (str): Title of the dataset.
  - ``cell_type_number`` (int): Number of cell types in this record.
  - ``collection_name`` (str): Name of the collection the dataset belongs to.
  - ``unit`` (str): Unit of measurement.
  - ``log_transformed`` (bool): Indicates if the data is log-transformed.
  - ``has_normal_baseline`` (bool): Indicates if the dataset has a normal baseline.

**Example Request:**

.. code-block:: bash

    curl -X GET "https://disease-approximation-p523xiwksa-ts.a.run.app/metadata?disease_keyword=flu"

**Example Response:**

.. code-block:: json

    [
        {
            "unique_id": "6c9402a9-13cd-55a4-daf5-ad6002360886",
            "disease": "COVID-19",
            "dataset_id": "055ca631-6ffb-40de-815e-b931e10718c0",
            "dataset_title": "Individual Single-Cell RNA-seq PBMC Data from Wilk et al.",
            "cell_type_number": 26,
            "collection_name": "A Web Portal and Workbench for Biological Dissection of Single Cell COVID-19 Host Responses",
            "unit": "cptt",
            "log_transformed": false,
            "has_normal_baseline": true
        },
        {
            "unique_id": "2d592d70-812d-7652-77d6-59e4bdb2223c",
            "disease": "COVID-19",
            "dataset_id": "de2c780c-1747-40bd-9ccf-9588ec186cee",
            "dataset_title": "Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19",
            "cell_type_number": 14,
            "collection_name": "Immunophenotyping of COVID-19 and influenza highlights the role of type I interferons in development of severe COVID-19",
            "unit": "cptt",
            "log_transformed": false,
            "has_normal_baseline": true
        },
        ...
    ]
