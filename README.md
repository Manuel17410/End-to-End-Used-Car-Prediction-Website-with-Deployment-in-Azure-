## End to End Used Car Prediction Price with Deployment in Azure

The Project contains the following code files that will be shortly explained:

* setup.py
* .gitignore
* requirements.txt
* jupyter notebook-usedcarpriceprediction
* custom_logging.py
* exception.py
* utils.py
* data_loader.py
* data_processing.py
* model_builder.py
* prediction_pipeline.py
* home.html

## Resources Used

**Python Version**: 3.12.7

**Code Editor**: Visual Studio Code

**Packages**: numpy, pandas, matplotlib, seaborn, scikit-learn, ipykernel, catboost, xgboost, dill, flask, flask_cors, lime, os

**Dataset**: www.kaggle.com/datasets/ayaz11/used-car-price-prediction

## Code Files

## setup.py

The script is designed to package the project for distribution, whether for upload to PyPI or internal use, install the project's dependencies listed in `requirements.txt`, and provide metadata that helps others understand and use the project. 

## .gitignore

It specifies files and directories Git should ignore to prevent them from being tracked in version control. The provided file excludes unnecessary files like compiled Python files (__pycache__/, *.pyc), build artifacts (build/, dist/), environment files (.env, venv/), logs, test coverage reports, and IDE or tool-specific files (e.g., .idea/, .ipynb_checkpoints).

## requirements.txt

It includes all the necessary libraries for the project. The main goal is to make installation smoother.

## UsedCarPricePrediction.ipynb

The main goal of this file was to:

1 - Clean and structure the data: duplicated values and outliers were eliminated, datatypes were corrected, columns were divided to create others that added more value to the analysis, column values were addapted.
2 - Various graphs were generated to gain insights and better understand the data.

## Customlogging.py

The code sets up a logging system that creates a uniquely named log file (based on the current timestamp) in a `logs` directory, formats log messages with details (timestamp, line number, log level, etc.), and logs messages at the INFO level or higher.

## exception.py

The code defines a custom exception handling system that generates detailed error messages, including the script name, line number, and the error description. It includes a function to format the error details and a custom exception class that enhances the default Python exceptions with more informative error messages.

## utils.py

The `utils.py` file contains utility functions that assist with common tasks throughout the project.It centralizes functionality that is used across different parts of the codebase, helping to keep the main code clean and organized. 

















https://predictionofusedcarsprices-hqd7g4engkggcbb4.canadaeast-01.azurewebsites.net/
