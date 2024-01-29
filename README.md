## Automated_Backup_Excel_Files
Creation of automated backup and encryption of weekly Excel files.

## Overview

This Python script performs currency conversion on an Excel file containing sales data. 
It utilizes the powerful data manipulation library, pandas, to handle Excel data and the forex-python library to fetch daily updated exchange rates. 
The converted data is then saved to a new Excel file using openpyxl.

## Features

- Converts currency values from Krone (CZK) to Euro (EUR) based on daily exchange rates
- Uses pandas for efficient data manipulation
- Retrieves exchange rates from forex-python
- Saves the results to a new Excel file with openpyxl

## Requirements

- Python 3.x
- watchdog==<3.0.0>

## Usage

1. Install the required packages: `pip install -r requirements.txt`
2. Run the script: `automated.py`
