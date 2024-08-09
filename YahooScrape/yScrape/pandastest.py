import pandas as pd


def abc ():
    global a
    a =3

def xyz():
    global a
    x = a+2
    return x
abc()

test = pd.read_csv("D:\\Downloads\\nasdaq_screener_1723022708864.csv")
for i in test['Symbol']:
    print(i)