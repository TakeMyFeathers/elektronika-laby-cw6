import matplotlib.pyplot as plt
import math
import csv

PREAMBLE = (
    r"\usepackage[T1]{fontenc}\usepackage[polish]{babel}\usepackage[utf8]{inputenc}"
)
plt.rcParams.update(
    {"text.usetex": True, "font.family": "sans-serif", "text.latex.preamble": PREAMBLE}
)

CIRCUIT_NAME = ["A", "B", "C"]

V_IN = (1.46, 16, 9.5)
F_LH = ((5.94, 90.78), (4.48, 1846), (0.855, 990.5))
K_0 = (33.2, 25.3, 46.2)

X = []
Y = ([],[],[])

with open("data.csv", "r") as csvfile:
    plots = csv.reader(csvfile, delimiter=",")

    for row in plots:
        X.append(float(row[0]))
        
        for i in range(0, len(CIRCUIT_NAME)):
            Y[i].append(20*math.log10(float(row[i+1]) / V_IN[i]))

            
figure, ax = plt.subplots()

for i in range(0,3):
    ax.set_xscale("log")

    ax.plot(X, Y[i])
    ax.scatter(X, Y[i])
    	
    ax.axhline(20 * math.log10(K_0[i]), color="grey", linestyle="--", alpha=0.5)
    ax.text(x=0.1, y=20 * math.log10(K_0[i]) + (ax.get_ylim()[1]-ax.get_ylim()[0])/100, s=r"$K_0$", color="black")
    	
    ax.axvline(F_LH[i][0], color="grey", linestyle="--", alpha=0.5)
    ax.text(
    	    x=F_LH[i][0],
        y=ax.get_ylim()[0] + (ax.get_ylim()[1]-ax.get_ylim()[0])/10,
    	    s=r"$f_{L3dB}$",
    	    color="black",
        rotation="vertical",
        ha="right"
    )
    	
    ax.axvline(F_LH[i][1], color="grey", linestyle="--", alpha=0.5)
    ax.text(
        x=F_LH[i][1],
    	    y=ax.get_ylim()[0] + (ax.get_ylim()[1]-ax.get_ylim()[0])/10,
    	    s=r"$f_{H3dB}$",
    	    color="black",
        rotation="vertical",
        ha="right"
    )
    
    ax.set_xlabel(r"Częstotliwość")
    ax.set_ylabel("Wzmocnienie")
    ax.set_title(f"Charakterystyka częstotliwościowa - układ {CIRCUIT_NAME[i]}")
    	
    figure.savefig(f"circuit_{CIRCUIT_NAME[i]}.png")
    ax.clear()
    

ax.set_xscale("log")

ax.plot(X, Y[0])
ax.plot(X, Y[1])
ax.plot(X, Y[2])

ax.set_xlabel(r"Częstotliwość")
ax.set_ylabel("Wzmocnienie")
ax.set_title("Charakterystyka częstotliwościowa - porównanie układów")

ax.legend(["A", "B", "C"])
figure.savefig("comparison.png")
