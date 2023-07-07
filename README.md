# Dollar_Rial_Price_Dataset
In this dataset, which we named **Dollar_Rial_Price_Dataset**, the price changes of the US dollar to the Iranian Rial have been collected using our crawler from **2011** to **2023** in the Persian calendar **1390** to **1402**. 

- This dataset will be suitable for predicting **time series data for predicting the dollar price** and other applications.
- Data collection and crawler implementation by: [Mohammad Taghizadeh](https://github.com/M-Taghizadeh)
- Source of data collection: https://tgju.org/

## Dataset Preview
For (almost) every day the price of the dollar has been scraped and entered, totaling **3310** records
It has been collected in the dataset for **13 years** (1390-1402).

| Record ID  | Date      | Persian_Date | Open    | Low     | High    | Close   |
|------------|-----------|--------------|---------|---------|---------|---------|
| 3,300      | 6/24/2023 | 1402/04/03   | 500,370 | 497,500 | 508,680 | 508,610 |
| 3,301      | 6/25/2023 | 1402/04/04   | 501,560 | 497,410 | 502,200 | 499,400 |
| 3,302      | 6/26/2023 | 1402/04/05   | 498,200 | 495,600 | 499,900 | 497,810 |
| 3,303      | 6/27/2023 | 1402/04/06   | 499,320 | 492,600 | 499,400 | 492,820 |
| 3,304      | 6/28/2023 | 1402/04/07   | 492,600 | 490,600 | 492,900 | 492,230 |
| 3,305      | 7/1/2023  | 1402/04/10   | 492,660 | 492,600 | 498,400 | 498,220 |
| 3,306      | 7/2/2023  | 1402/04/11   | 500,810 | 498,600 | 500,900 | 499,340 |
| 3,307      | 7/3/2023  | 1402/04/12   | 503,210 | 501,400 | 503,400 | 502,000 |
| 3,308      | 7/4/2023  | 1402/04/13   | 502,140 | 498,300 | 502,200 | 500,750 |
| 3,309      | 7/5/2023  | 1402/04/14   | 499,030 | 498,400 | 501,400 | 500,950 |

## Dataset Description 
We collected the following values ​​for each day.
| Field          | Description                                   |
|----------------|-----------------------------------------------|
| Date           | Date (format: date)                           |
| Persian_Date   | Persian date (format: Persian date)            |
| Open           | First price recorded on the day (format: price)|
| Low            | Lowest price recorded on the day (format: price)|
| High           | Highest price recorded during the day (format: price)|
| Close          | Last price recorded on the day (format: price) |


## Dataset Usage
You can access the dataset in 3 ways.

1. [**Github**](https://github.com/M-Taghizadeh/Dollar_Rial_Price_Dataset): Download the original dataset file in CSV format and use it from [here](https://github.com/M-Taghizadeh/Dollar_Rial_Price_Dataset/blob/master/Dollar_Rial_Price_Dataset.csv)


2. [**Kaggle**](https://www.kaggle.com/datasets/mohammadtaghizadeh/dollar-rial-price-dataset)

3. [**Hugging Face**](https://huggingface.co/datasets/mohammadtaghizadeh/Dollar_Rial_Price_Dataset): Load Dataset from Hugging Face repository with the following command.
    ```python
    from datasets import load_dataset

    dataset = load_dataset("mohammadtaghizadeh/Dollar_Rial_Price_Dataset")
    ```


## Crawler and How to Update Dataset
The important point of this dataset is that we also published our price extractor **crawler** in this project, which you can run at any time to update the dataset. To run this crawler, you need to install your system's **webdriver** so that the **Selenium** crawler can extract the new data.