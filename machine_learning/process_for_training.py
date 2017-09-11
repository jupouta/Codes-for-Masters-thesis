
import numpy
import matplotlib
import pandas as pd
import sklearn

data = pd.read_table("/Users/jultsi/Google Drive/Gradu/Koodi/processing/adultProcessed.txt",
                     encoding='utf-8', names=["message", "label"])
adultLabel = ["A"] * len(data)
data["label"] = adultLabel

dataYoung = pd.read_table("/Users/jultsi/Google Drive/Gradu/Koodi/processing/youngProcessed.txt",
                          encoding='utf-8', names=["message", "label"])
youngLabel = ["Y"] * len(dataYoung)
dataYoung["label"] = youngLabel


frames = [data, dataYoung]

resultData = pd.concat(frames)
