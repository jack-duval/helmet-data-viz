import numpy as np
import matplotlib.pyplot as plt
import math

def packetize(row):
    split = row.split(',')
    
    ret = {}

    ret["time"] = int(split[0])
    ret["x1"] = float(split[1])
    ret["y1"] = float(split[2])
    ret["z1"] = float(split[3])
    ret["x2"] = float(split[4])
    ret["y2"] = float(split[5])
    ret["z2"] = float(split[6])
    ret["x3"] = float(split[7])
    ret["y3"] = float(split[8])
    ret["z3"] = float(split[9])
    ret["hr"] = split[10]

    return ret

if __name__ == "__main__":
    path = './data.txt'
    data = np.loadtxt(path, dtype=str)
    # print(data)

    packets = []

    a1 = {"x": [], "y": [], "z": [], "mag": []}
    a2 = {"x": [], "y": [], "z": [], "mag": []}
    a3 = {"x": [], "y": [], "z": [], "mag": []}
    
    t = []

    for d in data:
        packet = packetize(d)
        a1["x"].append(packet["x1"])
        a1["y"].append(packet["y1"])
        a1["z"].append(packet["z1"]) 
        mag1 = math.sqrt((packet["x1"]**2) + (packet["y1"]**2) + (packet["z1"]**2))
        a1["mag"].append(mag1) 

        a2["x"].append(packet["x2"])
        a2["y"].append(packet["y2"])
        a2["z"].append(packet["z2"]) 
        mag2 = math.sqrt((packet["x1"]**2) + (packet["y1"]**2) + (packet["z1"]**2))
        a2["mag"].append(mag2) 

        a3["x"].append(packet["x2"])
        a3["y"].append(packet["y2"])
        a3["z"].append(packet["z2"]) 
        mag3 = math.sqrt((packet["x1"]**2) + (packet["y1"]**2) + (packet["z1"]**2))
        a3["mag"].append(mag3) 

        t.append(packet["time"])
        packets.append(packet)
    
    accels = [a1, a2, a3]
    for i in range(len(accels)):
        plt.plot(t, accels[i].get("x"))
        plt.plot(t, accels[i].get("y"))
        plt.plot(t, accels[i].get("z"))

        plt.xlabel("time")
        plt.ylabel("accel")
        plt.title("a"+str(i+1))
        plt.show()

    plt.plot(t, a1.get("mag"))
    plt.plot(t, a2.get("mag"))
    plt.plot(t, a3.get("mag"))
    ax = plt.gca()

    ax.set_ylim([0, 100])

    plt.xlabel("time")
    plt.ylabel("magnitudes")
    plt.title("Mags")
    plt.show()
    






