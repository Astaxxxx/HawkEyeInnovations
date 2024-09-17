import math
import matplotlib.pyplot as plt

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)

class Ball:
    def __init__(self, velocity, angle, wind_resistance=0.02):
        self.velocity = velocity  # m/s
        self.angle = math.radians(angle)  # Degrees to radians
        self.wind_resistance = wind_resistance  # Simulating wind drag

    def calculate_trajectory(self):
        time_of_flight = (2 * self.velocity * math.sin(self.angle)) / GRAVITY
        max_height = (self.velocity**2 * math.sin(self.angle)**2) / (2 * GRAVITY)
        range_distance = (self.velocity**2 * math.sin(2 * self.angle)) / GRAVITY

        time_intervals = [i * 0.01 for i in range(int(time_of_flight / 0.01) + 1)]
        x_positions, y_positions = [], []

        for t in time_intervals:
            x = (self.velocity * t * math.cos(self.angle)) * math.exp(-self.wind_resistance * t)
            y = (self.velocity * t * math.sin(self.angle)) - (0.5 * GRAVITY * t**2)
            if y >= 0:
                x_positions.append(x)
                y_positions.append(y)

        return x_positions, y_positions, max_height, range_distance

    def simulate_kick(self):
        x_positions, y_positions, max_height, range_distance = self.calculate_trajectory()
        print(f"Max Height: {max_height:.2f} meters")
        print(f"Range: {range_distance:.2f} meters")
        return x_positions, y_positions

def plot_trajectory(x_positions, y_positions, velocity, angle):
    plt.plot(x_positions, y_positions, label=f"v={velocity} m/s, θ={angle}°")
    plt.title("Football Kick Trajectory Simulation")
    plt.xlabel("Distance (m)")
    plt.ylabel("Height (m)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    velocity = float(input("Enter the initial velocity of the football (m/s): "))
    angle = float(input("Enter the angle of the kick (degrees): "))
    wind_resistance = float(input("Enter wind resistance factor (0-1, default 0.02): ") or 0.02)

    football = Ball(velocity, angle, wind_resistance)
    x_pos, y_pos = football.simulate_kick()
    plot_trajectory(x_pos, y_pos, velocity, angle)
