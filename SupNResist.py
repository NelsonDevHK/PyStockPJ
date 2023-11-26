import pandas as pd

df = pd.read_csv("EURUSD_Candlestick_1_D_ASK_05.05.2003-19.10.2019.csv")

df = df[df['volume'] != 0 ]

df.reset_index(drop=True,inplace=True)
df.isna().sum()
print(df.tail())

def support(df, current, before, after): 
    current = current + 1
    for i in range(current - before, current):
        if(df.low[i] > df.low[i - 1]):
            return 0
    for i in range(current , current + after):
        if(df.low[i] < df.low[i - 1]):
            return 0
    return 1

def resistance(df, current, before, after): 
    current = current + 1
    for i in range(current - before, current):
        if(df.high[i] < df.high[i - 1]):
            return 0
    for i in range(current , current + after):
        if(df.low[i] > df.low[i - 1]):
            return 0
    return 1