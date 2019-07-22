import random

import matplotlib.pyplot as plot
import numpy as np
import pandas as pd


def plot1(time, amplitude):
    # Plot a sine wave using time and amplitude obtained for the sine wave

    plot.plot(time, amplitude)

    # Give a title for the sine wave plot

    plot.title('Sine wave')

    # Give x axis label for the sine wave plot

    plot.xlabel('Time')

    # Give y axis label for the sine wave plot

    plot.ylabel('Amplitude = sin(time)')

    plot.grid(True, which='both')

    plot.axhline(y=0, color='k')

    plot.show()

    # Display the sine wave

    plot.show()


def create_sin(input_file='data/input/sine.csv'):
    df = pd.DataFrame()
    df["Date"] = pd.date_range("2018-01-01", end="2018-04-01", freq="15min")
    df.set_index(["Date"], inplace=True)
    df = df.iloc[:-1, :]
    df["price"] = 200 + ((((np.sin(np.arange(len(df)) / 30)) + 1) / 2) * 8000)
    df = df["price"].resample("60min").ohlc()
    df["ask_volume"] = [random.randint(1000, 10000) for k in df.index]
    df["bid_volume"] = [random.randint(1000, 10000) for k in df.index]
    df["Symbol"] = "SINUDS"
    df.rename(columns={"open": "Open", "high": "High", "low": "Low", "close": "Close", "ask_volume": "VolumeFrom",
                       "bid_volume": "VolumeTo"}, inplace=True)
    df = df[["Symbol", "Open", "High", "Low", "Close", "VolumeFrom", "VolumeTo"]]
    print(df.shape)
    df.to_csv(input_file)
