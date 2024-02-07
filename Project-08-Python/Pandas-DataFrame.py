## import pandas
import pandas as pd

## read csv file from pandas

df = pd.read_csv("store.csv")

## clean data 
## rename colums
col_name = list(df.columns)

## list comprehension
clean_col = [name.lower().replace(" ","_").replace("-","_") for name in col_name]

df.columns = clean_col

## data tranfomation
df[df["country"]== "United States"][["customer_name","country"]]

## query
df.query("city == 'Los Angeles' and category == 'Furniture'")

## aggregate data
df.groupby(["segmment","region"])[["sales","profit"]].agg(["sum","mean","std"]).reset_index()

## write csv
df.to_csv("new_store.csv")
