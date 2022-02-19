import pyupbit
import numpy as np

# 7일동안 원화시장에 대한 OHLCV를 불러옴(Open, Hight, Low, Close, Volume)로 당일시가, 고가, 저가, 종가, 거래량에 대한 데이터
df = pyupbit.get_ohlcv("KRW-BTC", count=7)
df['range'] = (df['high'] - df['low']) * 0.5
df['target'] = df['open'] + df['range'].shift(1)

# fee = 0.0032 # 빗썸기준
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target']  # - fee
                     , 1)

df['hpr'] = df['ror'].cumprod()
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
print("MDD(%): ", df['dd'].max())
df.to_excel("dd.xlsx")
