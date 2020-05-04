import papermill as pm


pm.execute_notebook("ingest_data.ipynb",
                    "out/ingest_data_out.ipynb")

pm.execute_notebook("data_prep.ipynb",
                    "out/data_prep_out.ipynb")

pm.execute_notebook("model_training.ipynb",
                    "out/model_training_out.ipynb",
                    parameters=dict(tree_max_depth=None, tree_min_samples_split=2, tree_min_samples_leaf=1)
)

pm.execute_notebook("validation.ipynb",
                    "out/validation_out.ipynb")

