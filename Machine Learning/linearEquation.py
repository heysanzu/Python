# 1. Define the core model equation: y_hat = (w * x) + b
def forward_pass(x, weight, bias):
    y_hat = (weight * x) + bias
    return y_hat

# 2. Our Data (1 single sample)
x = 3.0          # Feature: Active Tasks
y_actual = 65.0  # Target: Actual measured CPU Temperature

# 3. Initializing Parameters (Random initial guesses)
weight = 5.0     
bias = 10.0      

# 4. Execute the calculation
y_predicted = forward_pass(x, weight, bias)

# 5. Evaluate the initial mistake
error = y_actual - y_predicted

print(f"Actual Target (y):    {y_actual}°C")
print(f"Model Prediction (𝛾̂): {y_predicted}°C")
print(f"Current Error:        {error}°C")
