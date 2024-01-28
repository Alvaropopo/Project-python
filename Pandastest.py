import pandas as pd

# data={
#     'apple':[15,30,35,45,50],
#     'Kiwi':[5,20,25,15,30],
#     'grape':[25,15,30,21,13],
# }
# # print(data)
# data=pd.DataFrame(data,index=['January','February','March','April','May'])
# print(data)
# print(data.loc['April'])
data=pd.read_csv('premier-league-tables.csv')
print(data)
print(data.head(20))
print(data.tail(20))
print(data.info())
print(data.shape)