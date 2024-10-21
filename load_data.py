#!/usr/bin/python3

import pandas
import csv

CSV_PATH="prices.csv"

def process_pandas():
  df = pandas.read_csv(CSV_PATH)
  return df['PRODUCT_PRICE'].mean()

def process_csv():
  sum = 0
  rows = 0
  parsed = csv.reader(open(CSV_PATH))

  for row in parsed:
    rows += 1
    if rows == 1: continue
    
    sum += float(row[14])
  avg = sum / (rows - 1)
  return avg

def process_py():
  sum = 0
  rows = 0
  
  file = open(CSV_PATH, "r")
  for row in file:
    rows += 1
    if rows == 1: continue

    columns = row.split(',')
    sum += float(columns[14])
  file.close()
  
  avg = sum / (rows - 1)
  return avg
    

if __name__ == "__main__":
    print("Average price using pure python: ", end='')    
    print(process_py())
    print("Average price using csv module: ", end='')    
    print(process_csv())
    print("Average price using pandas module: ", end='')    
    print(process_pandas())

# dictionary that contains the average for each value in the dict
def process_csv_dict():
  item_prices = {
    # "Wine": 0,
    # "Spirits": 0,
    # "Refreshment Beverages": 0,
    # "General Merchandise": 0,
  }
  item_counts = {
    # "Wine": 0,
    # "Spirits": 0,
    # "Refreshment Beverages": 0,
    # "General Merchandise": 0,
  }

  df = pandas.read_csv(CSV_PATH)

  for (index, item_kind) in df['ITEM_CATEGORY_NAME'].items():

      if item_kind not in item_prices: 
        item_prices[item_kind] = 0
        item_counts[item_kind] = 0
      
      item_prices[item_kind] += df['PRODUCT_PRICE'][index]
      item_counts[item_kind] += 1
  
  for (kind, price) in item_prices.items():
    item_prices[kind] = price / item_counts[kind]

  print(item_prices)
  return item_prices

# 
def process_pandas_groupby():
  df = pandas.read_csv(CSV_PATH)

  res = df.groupby('ITEM_CATEGORY_NAME').mean(True).filter([
    'ITEM_CATEGORY_NAME',
    'PRODUCT_PRICE',
  ])
  print(res)
  return res