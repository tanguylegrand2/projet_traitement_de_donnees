# Data Cleaning and Preparation Application

This project is aimed at developing an application for cleaning and preparing data for future statistical work. The application includes functionalities to handle missing values, remove duplicates, standardize data, and more.

## Project Overview

The objective of this project is to create a set of tools that automate the process of data preprocessing, which is essential for preparing data before conducting any statistical analysis or machine learning work.

## Features

- **Handle Missing Data**: Techniques to fill or remove missing data.
- **Remove Duplicates**: Automatically identify and remove duplicate entries.
- **Data Standardization**: Normalize or standardize data to ensure consistency.
- **Data Transformation**: Support for encoding categorical data and other transformation tasks.

## Technologies Used

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Scikit-learn
- **Tools**: Jupyter Notebooks for interactive development

## Installation

Clone the repository:

```bash
git clone https://github.com/tanguylegrand2/projet_traitement_de_donnees.git
cd projet_traitement_de_donnees
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the Application

The main functionalities are contained within the Python scripts in this project. You can run the scripts or use Jupyter Notebooks to interactively process your datasets.

Example command to start the script:

```bash
python clean_data.py
```

## Usage

Once the application is set up, you can clean and prepare datasets by importing them and applying the relevant methods. Example code snippet:

```python
import pandas as pd
from data_cleaning import clean_data

df = pd.read_csv('your_dataset.csv')
df_clean = clean_data(df)
```

## Future Improvements

- **Integration with databases**: Fetch data directly from databases like MySQL or PostgreSQL.
- **User Interface**: Develop a web-based interface to make the application user-friendly for non-programmers.
- **Advanced Cleaning Techniques**: Implement more advanced methods for dealing with imbalanced datasets or outliers.


