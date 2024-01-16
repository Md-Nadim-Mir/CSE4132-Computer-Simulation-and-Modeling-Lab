import numpy as np
import matplotlib.pyplot as plt

def distance(x1, y1, x2, y2):
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def simulate_pure_pursuit(v_fighter, v_bomber):
    t = 0
    dt = 1  # Time step
    xf, yf = np.random.randint(1, 1000), np.random.randint(1, 1000)
    xb, yb = np.random.randint(1, 1000), np.random.randint(1, 1000)

    while distance(xf, yf, xb, yb) > 100 and distance(xf, yf, xb, yb) < 900:
       
       
        # Update fighter position
        xf += v_fighter * np.cos(np.arctan2((yb - yf), (xb - xf))) * dt
        yf += v_fighter * np.sin(np.arctan2((yb - yf), (xb - xf))) * dt

        # Update bomber position
        xb += v_bomber * np.cos(np.arctan2((yf - yb), (xf - xb))) * dt
        yb += v_bomber * np.sin(np.arctan2((yf - yb), (xf - xb))) * dt

        print(f"time={t} xf={xf:.2f} yf={yf:.2f} xb={xb:.2f} yb={yb:.2f} distance={distance(xf, yf, xb, yb):.2f}")
        t += dt

    if distance(xf, yf, xb, yb) < 100:
        print(f"BOMBER SHOT DOWN at {t} seconds")
    elif distance(xf, yf, xb, yb) > 900:
        print(f"BOMBER ESCAPES FROM THE SIGHT OF FIGHTER at {t} seconds")

    # Plot the paths
    plt.title("Simulation of a Pure Pursuit")
    plt.plot([xf], [yf], marker='o', label='Fighter')
    plt.plot([xb], [yb], marker='o', label='Bomber')
    plt.legend()
    plt.grid()
    plt.show()

# Example usage
simulate_pure_pursuit(v_fighter=20, v_bomber=20)
