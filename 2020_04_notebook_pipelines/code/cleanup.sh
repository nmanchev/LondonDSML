#!/bin/bash

mkdir -p /home/ubuntu/.cache/black/19.10b0

rm -f manual/model.joblib
rm -f manual/test.csv
rm -f manual/train.csv
rm -f manual/data.csv

rm -f master-notebook/model.joblib
rm -f master-notebook/test.csv
rm -f master-notebook/train.csv
rm -f master-notebook/data.csv

rm -f papermill-notebook/model.joblib
rm -f papermill-notebook/test.csv
rm -f papermill-notebook/train.csv
rm -f papermill-notebook/data.csv
rm -f papermill-notebook/out/*

rm -rf airflow/out/*
rm -rf airflow/out/.* 2> /dev/null
rm -f airflow/model.joblib
rm -f airflow/test.csv
rm -f airflow/train.csv
rm -f airflow/data.csv
rm -f airflow/af_home/dags/nb_dag.py
