# Perceptron Lab Exercise

## Objective

In this lab exercise, we aim to understand the logical working of a perceptron and implement it from scratch using Python (NumPy). The perceptron will be used to classify linearly separable data (AND and OR gates). Additionally, we will visualize the decision boundary and understand the limitations of a single-layer perceptron when applied to non-linearly separable data (XOR gate).

## Requirements

- Python 3.x
- NumPy
- Matplotlib (for visualization)

## Steps

### 1. Implementing Perceptron from Scratch

- Implement a single-layer perceptron to classify **AND** or **OR** gate.
- Initialize the weights and bias randomly.
- Use the **sigmoid function** as the activation function.
- Update weights using the **perceptron learning rule** or using **guesses**.
- Train the perceptron on the data and test it to classify the output.

### 2. Visualizing the Decision Boundary

- After training the perceptron, visualize the **decision boundary** that separates the classes (i.e., output of the gate).
- Use **matplotlib** to visualize the decision boundary.

### 3. Extension: Perceptron for XOR Gate

- Implement a perceptron for the **XOR gate**.
- Show that a **single-layer perceptron** fails to learn the XOR function (as it is not linearly separable).
- Introduce a **multi-layer perceptron (MLP)** to overcome this limitation and correctly classify XOR inputs.
