# Backpropagation in a Neural Network

## Objective
This project aims to implement and analyze the backpropagation algorithm in a simple neural network. The key objectives include:
- Understanding how weights are updated and how error convergence occurs over multiple iterations.
- Visualizing the learning process using graphs.
- Experimenting with different learning rates and activation functions.

## Problem Statement
A feedforward neural network with the following structure is used for backpropagation:
- **Input Layer:** 3 neurons
- **Hidden Layer:** 2 neurons (Sigmoid activation)
- **Output Layer:** 1 neuron (Sigmoid activation)
- **Target Output:** 1
- **Learning Rate:** 0.01, 0.1, and 0.5 (for comparison)

The task is to implement backpropagation, train the network for 1000 iterations, and analyze the changes in weights and errors over time.

## Implementation Steps
1. **Initialize the Neural Network**: Define the structure and initialize weights and biases.
2. **Implement Forward Propagation**: Compute outputs for hidden and output layers.
3. **Compute Error**: Measure the difference between predicted and target output.
4. **Perform Backpropagation**: Update weights using gradient descent.
5. **Run Multiple Iterations**: Repeat forward and backward propagation for 1000 iterations.

## Analysis and Visualization
### 1. Error vs. Iterations Graph (Required)
- **Plot:** Number of iterations (X-axis) vs. Error (Y-axis).
- **Observations:**
  - Does the error decrease gradually?
  - Does it oscillate due to an improper learning rate?

### 2. Weight Updates Over Iterations
- **Plot:** Number of iterations (X-axis) vs. Selected weight value (Y-axis).
- **Observations:**
  - Do weights stabilize over time?
  - Do they oscillate due to a large learning rate?

### 3. Learning Rate Comparison (Recommended)
- **Plot:** Error vs. Iterations for different learning rates (0.01, 0.1, 0.5) on the same graph.
- **Observations:**
  - Which learning rate achieves faster convergence?
  - Does a high learning rate cause oscillations?

### 4. Decision Boundary Visualization
- Visualize the decision boundary before and after training.

## Additional Experiment
- Modify the network to use **ReLU** activation instead of sigmoid and compare its performance.
