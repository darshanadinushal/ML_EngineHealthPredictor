import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_names = ["EngineHealthPredictor"]  # Add more projects as needed

common_files = [
    "utils/__init__.py",
    "utils/common.py",
    "config/__init__.py",
    "config/configuration.py",
    "pipeline/__init__.py",
    "entity/__init__.py",
    "entity/config_entity.py",
    "constants/__init__.py"
]

components = [
    "components/__init__.py",
    "components/data_ingestion.py",
    "components/data_transformation.py",
    "components/data_validation.py",
    "components/model_evaluation.py",
    "components/model_trainer.py"
]

other_files = [
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for project_name in project_names:
    list_of_files = [f"src/{project_name}/{file}" for file in common_files + components] + other_files

    for filepath in list_of_files:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)


        if filedir !="":
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory; {filedir} for the file: {filename}")

        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
            with open(filepath, "w") as f:
                pass
                logging.info(f"Creating empty file: {filepath}")

        else:
            logging.info(f"{filename} is already exists")