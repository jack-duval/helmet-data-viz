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


    # z1 - z2 - x3 = x glob
    # y1 - y2 + y3 = y glob
    # -x1 - x2 + z3 = z glob

    x_glob = []
    y_glob = []
    z_glob = []

    roll = [] # r1 left pos
    pitch = [] # r2 face down pos
    yaw = [] # r3 right rot pos

    hockey_rad = 8
    football_rad = 10

    # r1 = ((x3 + x1 - x2) / 10cm) * 9.81 = r1 radians/s2
    # r2 = ((y1 - y2 - y3) / 10cm) * 9.81 = r2 radians/s2
    # r3 = ((y1 + y2) / 10cm) * 9.81 = r3 radians/s2
    
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

        x_g = packet["z1"] - packet["z2"] - packet["x3"]
        y_g = packet["y1"] - packet["y2"] + packet["y3"]
        z_g = (-1 * packet["x1"]) - packet["x2"] + packet["z3"]

        x_glob.append(x_g)
        y_glob.append(y_g)
        z_glob.append(z_g)

        roll_i = ((packet["x3"] + packet["x1"] - packet["x2"]) / 10) * 9.81
        pitch_i = ((packet["y1"] - packet["y2"] - packet["y3"]) / 10) * 9.81
        yaw_i = ((packet["y1"] + packet["y2"]) / 10) * 9.81

        roll.append(roll_i)
        pitch.append(pitch_i)
        yaw.append(yaw_i)

        packets.append(packet)
    
    accels = [a1, a2, a3]
    # for i in range(len(accels)):
    #     plt.plot(t, accels[i].get("x"))
    #     plt.plot(t, accels[i].get("y"))
    #     plt.plot(t, accels[i].get("z"))

    #     plt.xlabel("time")
    #     plt.ylabel("accel")
    #     plt.title("a"+str(i+1))
    #     plt.show()

    plt.plot(t, a1.get("mag"))
    plt.plot(t, a2.get("mag"))
    plt.plot(t, a3.get("mag"))
    ax = plt.gca()

    ax.set_ylim([0, 100])

    plt.xlabel("time")
    plt.ylabel("magnitudes")
    plt.title("Mags")
    plt.show()

    plt.plot(t, roll)
    plt.plot(t, pitch)
    plt.plot(t, yaw)
    plt.xlabel("time")
    plt.ylabel("rot accel")
    plt.show()

    
    






