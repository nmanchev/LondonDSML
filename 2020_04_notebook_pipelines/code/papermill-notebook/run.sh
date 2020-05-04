#!/bin/bash

papermill ingest_data.ipynb out/ingest_data_out.ipynb

papermill data_prep.ipynb out/data_prep_out.ipynb

papermill model_training.ipynb out/model_training.ipynb --log-output -p tree_max_depth 5

papermill validation.ipynb out/validation_out.ipynb --log-output