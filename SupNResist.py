import pandas as pd
import plotly.graph_objects as go
from datetime import datetime


def support(df, current, before, after): 
    # the FIRST candle stick need to have a before
    # the LAST candle stick need to have an after
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


df = pd.read_csv("EURUSD_Candlestick_1_D_ASK_05.05.2003-19.10.2019.csv")

SupportArr = []
ResistArr = []
n1=2
n2=2
for row in range(3, 205): #len(df)-n2
    if support(df, row, n1, n2):
        SupportArr.append((row,df.low[row]))
    if resistance(df, row, n1, n2):
        ResistArr.append((row,df.high[row]))

# tempss= [SupportArr[1]]
# temprr = [ResistArr[1]]

tempss = [x[1] for x in SupportArr]
temprr = [x[1] for x in SupportArr]

tempss.sort()
temprr.sort()
for i in range(1,len(tempss)):
    if(i>=len(tempss)):
        break
    if (abs(tempss[i] -tempss[i-1])<=0.005):
        tempss.pop(i)

for i in range(1,len(temprr)):
    if(i>=len(temprr)):
        break
    if abs(temprr[i]-temprr[i-1])<=0.005:
        temprr.pop(i)

SupportArr = tempss
ResistArr = temprr

start = 0
end = 200
dfpl = df[start:end]

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['open'],
                high=dfpl['high'],
                low=dfpl['low'],
                close=dfpl['close'])])

Cur = 0

while (1):
    if(Cur>len(SupportArr)-1 ):
        break
    fig.add_shape(type='line', x0=start, y0=SupportArr[Cur][1],
                  x1=end,
                  y1=SupportArr[Cur][1],
                  line=dict(color="green",width=3)
                  )
    Cur+=1

Cur=0
while (1):
    if(Cur>len(ResistArr)-1 ):
        break
    fig.add_shape(type='line', x0=start, y0=ResistArr[Cur][1],
                  x1=end,
                  y1=ResistArr[Cur][1],
                  line=dict(color="red",width=1)
                  )
    Cur+=1    
fig.show()

