import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SportsProject {

    private static final double GRAVITY = 9.81;

    public static class Ball {
        private double velocity;
        private double angle;
        private double windResistance;

        public Ball(double velocity, double angle, double windResistance) {
            this.velocity = velocity;
            this.angle = Math.toRadians(angle);
            this.windResistance = windResistance;
        }

        public List<Double[]> calculateTrajectory() {
            double timeOfFlight = (2 * velocity * Math.sin(angle)) / GRAVITY;
            List<Double[]> trajectory = new ArrayList<>();
            double t = 0;
            double x, y;
            double dt = 0.01;

            while (t <= timeOfFlight) {
                x = (velocity * t * Math.cos(angle)) * Math.exp(-windResistance * t);
                y = (velocity * t * Math.sin(angle)) - (0.5 * GRAVITY * t * t);

                if (y >= 0) {
                    trajectory.add(new Double[] { x, y });
                } else {
                    break;
                }
                t += dt;
            }
            return trajectory;
        }

        public void simulateKick() {
            List<Double[]> trajectory = calculateTrajectory();
            System.out.println("Max Height: " + trajectory.stream().mapToDouble(a -> a[1]).max().getAsDouble() + " meters");
            System.out.println("Range: " + trajectory.stream().mapToDouble(a -> a[0]).max().getAsDouble() + " meters");
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter initial velocity of the football (m/s): ");
        double velocity = scanner.nextDouble();

        System.out.print("Enter angle of the kick (degrees): ");
        double angle = scanner.nextDouble();

        System.out.print("Enter wind resistance factor (0-1, default 0.02): ");
        double windResistance = scanner.hasNextDouble() ? scanner.nextDouble() : 0.02;

        Ball football = new Ball(velocity, angle, windResistance);
        football.simulateKick();
    }
}
