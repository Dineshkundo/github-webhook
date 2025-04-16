#!/bin/bash

echo "[INFO] Pulling latest DAGs..."
cd /home/adqdevops2/airflow/dags || exit
git pull origin main

if [ -f requirements.txt ]; then
  echo "[INFO] Installing requirements..."
  pip install -r requirements.txt
fi

echo "[INFO] Triggering Airflow DAG..."
airflow dags trigger test
