import pandas as pd
import plotly.graph_objects as go
################################    START OF USEFUL NOTES     ################################
#Local time,open,high,low,close,volume
#df = dataframe
#dfpl = dataframePloting
################################    END OF USEFUL NOTES     ################################

################################       GLOBAL VARIABLES       ################################
df = pd.read_csv('EURUSD_Candlestick_1_D_ASK_05.05.2003-19.10.2019.csv')
dataSize = len(df)
start = 0
end = dataSize
dfpl = df[start:dataSize]
################################       GLOBAL VARIABLES       ################################

fig = go.Figure(data=[go.Candlestick(x=dfpl.index,
                open=dfpl['open'],
                high=dfpl['high'],
                low=dfpl['low'],
                close=dfpl['close'])])
fig.show()
