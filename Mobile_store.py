import pandas as pd
load_df=pd.read_csv('MOBILE_STORE_PROJECT.csv')
load_df
print(load_df)
load_df['Revenue']=load_df['Selling_Price']*load_df['Sold']
load_df['Cost']=load_df['Purchase_Price']*load_df['Sold']
load_df['Profit']=load_df['Revenue']-load_df['Cost']
load_df['Profit_Margin']=load_df['Profit']/load_df['Revenue']*100
load_df["Unsold_Stock"] = load_df["Stock"] - load_df["Sold"]
load_df["Inventory_Value"] = load_df["Unsold_Stock"] * load_df["Purchase_Price"]
print(load_df.groupby("Brand")["Sold"].sum())
print(load_df.loc[load_df["Profit"].idxmax()])
print(load_df.groupby("Brand")["Revenue"].sum())
print(load_df.sort_values("Profit", ascending=False))
print(load_df[load_df["Profit"] > 100000])
print(load_df)
load_df.to_csv("Mobile_Store_Report.csv", index=False)