import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# Create some mock data
t = np.arange(0.01, 10.0, 0.01)
data1 = np.exp(t)
data2 = np.sin(2 * np.pi * t)


df = pd.read_csv("C:/Users/radli/code/documentation/plt/doc/buy_xed.csv", na_values="?")

df["time1"] = df["time"].str[:5]

i = 0
while True:
    time_list = list(df["time1"].iloc[i])
    dotdot_count = 0
    for j in range(len(time_list)):
        if time_list[j] == ":":
            dotdot_count += 1
            if dotdot_count == 1 & j == 1:
                time_list[4] = time_list[3]
                time_list[3] = time_list[2]
                time_list[2] = time_list[1]
                time_list[1] = time_list[0]
                time_list[0] = str(0)
                df["time1"].iloc[i] = "".join(time_list)
                break
            if dotdot_count == 2:
                time_list[j] = time_list[j - 1]
                time_list[j - 1] = str(0)
                df["time1"].iloc[i] = "".join(time_list)
                break
    i += 1
    if df["time1"].iloc[i - 1] == df["time1"].iloc[-1]:
        break

i = 0
while True:
    time_list = list(df["time1"].iloc[i])
    dotdot_count = 0
    for j in range(len(time_list)):
        if time_list[j] == ":":
            dotdot_count += 1
            if dotdot_count == 2:
                time_list[j] = time_list[j - 1]
                time_list[j - 1] = str(0)
                df["time1"].iloc[i] = "".join(time_list)
                break
    i += 1
    if df["time1"].iloc[i - 1] == df["time1"].iloc[-1]:
        break


df.plot(x="time1", y="diff")
plt.title("buy XED diff", color="black")
plt.ylabel("diff")
plt.xlabel("time")
plt.tight_layout()
plt.show()
