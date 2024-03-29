import seaborn as sns
import pandas as pd
sales = pd.read_excel("C:/Users/VigneshNatchimuthu/Downloads/NewOrders.xlsx")
print(sales)
sns.relplot("Sales","Profit",data=sales)
sns.relplot("Sales","Profit",data=sales,hue="Order Priority")
sns.relplot("Sales","Profit",data=sales,hue="Order Priority",style="Order Priority")
sns.relplot("Sales","Profit",data=sales,size="Discount",sizes=(25,200))
sales.head()
sns.relplot("Order Date","Sales",data=sales,kind='line')
sales['year'] = sales['Order Date'].dt.year
sns.relplot('year','Sales',data=sales,kind='line',ci=None)
sns.relplot('year','Sales',data=sales,kind='line',ci="sd")
sns.relplot('year','Sales',data=sales,kind='line',estimator=None)
sns.relplot('year','Sales',data=sales,kind='line',hue='Ship Mode',style="Product Category",ci=None)
sns.relplot('year','Sales',data=sales,kind='line',hue='Ship Mode', col="Product Category",ci=None)
sns.relplot('year','Sales',data=sales,kind='line',hue='Ship Mode', col="Region",ci=None)
sns.relplot('year','Sales',data=sales,kind='line',hue='Ship Mode', col="Region",ci=None,col_wrap=4)
sns.relplot("Sales","Profit",data=sales,col="Customer Segment" ,col_wrap=2)
sns.relplot("Sales","Profit",data=sales,col="Customer Segment", col_wrap=2,hue="Order Priority")
sns.relplot("Sales","Profit",data=sales,col="Customer Segment", row='Product Category', hue="Ship Mode")
sns.catplot("Ship Mode","Sales",data=sales)
sns.catplot("Ship Mode","Sales",data=sales, jitter=False)
sns.catplot("Ship Mode","Sales",data=sales.query("Profit > 1000"), jitter=False)
sns.catplot("Ship Mode","Sales",data=sales.query("Profit > 1000"), kind="swarm")
sns.catplot("Sales","Ship Mode",data=sales.query("Profit > 1000"), kind="swarm")
sns.catplot(x="Product Category",y="Shipping Cost",data=sales,kind="box")
sns.catplot(x="Product Category",y="Shipping Cost",hue ="Ship Mode" ,hue_order=["Delivery Druck","Regular Air","Express air"],data=sales,kind="box")
sns.catplot(x="Product Category",y="Shipping Cost",data=sales,kind="violin")
sns.catplot(x="Product Category",y="Sales",col="Customer Segment", hue="Ship Mode",data=sales,kind="bar")
sns.catplot(x="Product Category",y="Sales",hue="Ship Mode",col="Customer Segment",data=sales,kind="point")
