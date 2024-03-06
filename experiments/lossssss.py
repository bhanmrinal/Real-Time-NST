import matplotlib.pyplot as plt

def msgnet_accuracy(iterations, style_complexity, image_complexity, hardware_speed):
  """
  Simulates MSG-Net's accuracy based on given factors.

  Args:
    iterations: Number of frames processed (X-axis).
    style_complexity: Integer indicating style difficulty (1-5).
    image_complexity: Integer indicating scene complexity (1-5).
    hardware_speed: Factor representing processing power (1-3).

  Returns:
    A list of accuracy values for each iteration.
  """

  # Base accuracy and convergence rate
  base_accuracy = 85
  convergence_rate = 0.1

  # Adjust for complexities and hardware
  complexity_factor = 1 + (style_complexity + image_complexity) / 10
  hardware_factor = hardware_speed / 2

  accuracy = []
  for i in range(iterations):
    # Initial rise
    if i < 10:
      accuracy.append(base_accuracy + i * convergence_rate)
    # Plateau with fluctuations
    else:
      accuracy.append(base_accuracy + complexity_factor * hardware_factor * (1 + 0.05 * i ** 0.5))

  return accuracy

# Set parameters for your desired scenario
iterations = 50
style_complexity = 3
image_complexity = 2
hardware_speed = 2

# Generate and plot accuracy values
accuracy_values = msgnet_accuracy(iterations, style_complexity, image_complexity, hardware_speed)

plt.plot(range(iterations), accuracy_values)
plt.xlabel("Iterations (frames processed)")
plt.ylabel("Style transfer accuracy (%)")
plt.title("MSG-Net: Iteration vs. Accuracy")

plt.show()
