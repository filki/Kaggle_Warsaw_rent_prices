![Contributors](https://img.shields.io/github/contributors/filki/Kaggle_Warsaw_rent_prices?style=for-the-badge&logo=github)
![Release](https://img.shields.io/github/release/filki/Kaggle_Warsaw_rent_prices?style=for-the-badge&logo=github)
![Last_commit](https://img.shields.io/github/last-commit/filki/Kaggle_Warsaw_rent_prices?style=for-the-badge&logo=github)\
![License](https://img.shields.io/github/license/filki/Kaggle_Warsaw_rent_prices?style=for-the-badge&logo=github)

# Kaggle_Warsaw_rent_prices
This repository is an attempt to build machine learning model capable of predicting flat prices in Warsaw, Poland. It's synchronized with kaggle network, which you can find here: https://www.kaggle.com/code/filipkin/warsaw-flats

## Packages used
* General Purpose
    * re
    * math
* Data Manipulation
    * numpy
    * pandas
* Data Visualization
    * matplotlib
    * seaborn
    * missingno
* Machine Learning
    * scikit-learn
* Statistics
    * scipy

## Data
Data source: Web-scraped data from Otodom (Polish real estate website) containing information about rental properties in Warsaw.

The dataset contains 3,482 entries with 30 columns including:
* `location`: Property location in Warsaw
* `net_price`: Rental price
* `deposit`: Security deposit amount
* `area`: Property area in square meters
* `room_num`: Number of rooms
* `build_type`: Type of building (block, apartment, etc.)
* `floor`: Floor number
* `total_floor`: Total number of floors in the building
* `build_mat`: Building material
* `windows`: Window type
* `heating`: Heating type
* `year_built`: Year when the building was constructed
* `status`: Property status
* `agd`: Household appliances information
* `security`: Security features
* `add_info`: Additional information
* `rest_info`: Other information
* Various metadata fields related to the web scraping process

## Data Preprocessing
The notebook performs several data cleaning and preprocessing steps:
* Handling missing values in various columns
* Custom functions to fill missing building types and total floor values using regex patterns
* Extraction of numerical values from text fields (like area and room numbers)
* Feature engineering based on URL content and text descriptions

## Exploratory Data Analysis (TBA)
The notebook includes initial exploratory data analysis to understand the distribution of rental prices, property sizes, and other features.

## Model Building (TBA)
Machine learning models will be built to predict rental prices based on property features.

## Results and Evaluation (TBA)
Performance metrics and evaluation of the prediction models will be added as the project progresses.

## Future Work (TBA)
Potential improvements and extensions to the current analysis will be documented here.



