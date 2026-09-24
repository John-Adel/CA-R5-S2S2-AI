from LinearRegression import LinearRegressionGD
import numpy as np
import matplotlib.pyplot as plt

x = [50, 60, 70, 80, 90]
y = [150, 180, 210, 240, 270]

# 1. What does x and y represents?
# This is the data of houses, presumably of a Real State company.
# x is the data on the x-axis which represent's the area feature, and y is the house's price in thousands
# You can take each number from x and y and plot it against a scatter plot graph





# 2. Converting data to numpy array?
x = np.array(x)
y = np.array(y)





# 3. Creating and Training the model
# Note: the alpha provided in the pdf is large, I used a smaller one
no_of_iterations = 100
lrgd = LinearRegressionGD(0.0001, no_of_iterations)
w, b, sse = lrgd.fit(x, y)
# Question: What do theta_0 and theta_1 represent in the regression equation?
print(f"θ₀ = {b}\nθ₁ = {w}\nθ₀ represents the bias also called the y intercept, while θ₁ represents the weight")





# 4. Prediction
data_point = np.array([70])
y_hat = lrgd.predict(data_point, w, b)
print(f"Predicted y:{y_hat}")
y_predicted = (lrgd.predict(x, w, b))

# Question: Is the prediction reasonable based on the dataset? Why?
# It is reasonable, 70 was already inside x, and y gave 210 which is the same answer here. 
# The fraction comes from the closest we got to w and b, which must have been 3 and 0 from least squares





# 5. visualize sse over iterations and ploting the regression lines with data points
iterations = list(range(1, no_of_iterations + 1))
lrgd.plot_training(sse, iterations, x, y, y_predicted)

# Explain: Why SSE decreases over time? What convergence means in Gradient Descent?
# As the weight and bias get closer to their correct number, the line fits more perfectly
# This reduces the error, so the sse decreases
# Convergence means that the function isn't making the weight and bias any better
# The number that was given for the learning rate in the pdf is really big (0.001)
# That overshot the global minimum which resulted in a huge w and b, more than python can actually hold in float64
# I used a smaller alpha with 0.0001, this got to the global minimum in just 2 iterations as we can see from the graph
# If I used smaller alpha, it would take more steps to get to the minimum




# 6. Experimentation
large_step = 0.001
small_step = 0.00001
large_Len_reg = LinearRegressionGD(large_step, 100)
small_len_reg = LinearRegressionGD(small_step, 100)
w_large, b_large, sse_large = large_Len_reg.fit(x, y)
w_small, b_small, sse_small = small_len_reg.fit(x, y)


plt.figure(figsize=(5, 5))

plt.subplot(1, 2, 1)
plt.plot(
    iterations,
    sse_large,
    marker="*",
    linestyle="-",
    color="red",
    markerfacecolor="blue",
    markeredgecolor="black",
    label = "Sum of Squared Residuls"
)
plt.xticks(iterations[::9])
plt.yscale('log')
plt.xlabel("Iterations")
plt.ylabel("Sum of Squared Residuals")
plt.title("Minimizing the Sum of Squared Residuals")
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(
    iterations,
    sse_small,
    marker="*",
    linestyle="-",
    color="red",
    markerfacecolor="blue",
    markeredgecolor="black",
    label = "Sum of Squared Residuls"
)
plt.xticks(iterations[::9])
plt.xlabel("Iterations")
plt.ylabel("Sum of Squared Residuals")
plt.title("Minimizing the Sum of Squared Residuals")
plt.legend()

plt.tight_layout()
plt.show()
# Compare between Convergence speed and the Final SSE value
print(f"Final SSE For the large alpha: {sse_large[-1]}\nFinal SSE for the small alpha: {sse_small[-1]}")
# we can see with the large alpha, the sse overshot from the first iteration, it continued to get larger,
# it missed the global minimum from the fist iteration
# while the sse with the small alpha, it got to zero gradually, but it needed more iterations though
# for the convergence speed, it is huge for the large alpha, as the sse overshot the global minimum from the first iteration
# while in the small alpha, the convergence was much more slower, it got smaller and smaller gradually 

# Question: What happens if the learning rate is too large?
# The function misses the global minimum






# Bonus Tasks
# Method to calculate mse
mse = lrgd.calculate_mse(sse[-1], y)
print(f"Mean Square Error: {mse}")

# x normalization and comparison
len_reg_norm = LinearRegressionGD(0.0001, 100)
x_norm = len_reg_norm.normalize(x)
w_norm, b_norm, sse_norm = len_reg_norm.fit(x_norm, y)
y_predicted_norm = len_reg_norm.predict(x_norm, w_norm, b_norm)

len_reg_norm2 = LinearRegressionGD(0.0001, 10000)
x_norm2 = len_reg_norm2.normalize(x)
w_norm2, b_norm2, sse_norm2 = len_reg_norm2.fit(x_norm2, y)
y_predicted_norm2 = len_reg_norm2.predict(x_norm2, w_norm2, b_norm2)

len_reg_norm3 = LinearRegressionGD(0.1, 10000)
x_norm3 = len_reg_norm3.normalize(x)
w_norm3, b_norm3, sse_norm3 = len_reg_norm3.fit(x_norm3, y)
y_predicted_norm3 = len_reg_norm3.predict(x_norm3, w_norm3, b_norm3)
plt.figure(figsize=(5, 5))

plt.subplot(2, 2, 1)
plt.scatter(x, y, label="Data")
plt.plot(x, y_predicted, color="red", label="Best-fit Line")
plt.xlabel("Area of the House")
plt.ylabel("Price in Thousands")
plt.title("alpha = 0.0001 and iterations = 100, x not normalized")
plt.legend()

plt.subplot(2, 2, 2)
plt.scatter(x_norm, y, label="Data")
plt.plot(x_norm, y_predicted_norm, color="red", label="Best-fit Line")
plt.xlabel("Area of the House")
plt.ylabel("Price in Thousands")
plt.title("alpha = 0.0001, iterations = 100, x normalized")
plt.legend()

plt.subplot(2, 2, 3)
plt.scatter(x_norm2, y, label="Data")
plt.plot(x_norm2, y_predicted_norm2, color="red", label="Best-fit Line")
plt.xlabel("Area of the House")
plt.ylabel("Price in Thousands")
plt.title("alpha = 0.0001, iterations = 10000, x normalized")
plt.legend()

plt.subplot(2, 2, 4)
plt.scatter(x_norm3, y, label="Data")
plt.plot(x_norm3, y_predicted_norm3, color="red", label="Best-fit Line")
plt.xlabel("Area of the House")
plt.ylabel("Price in Thousands")
plt.title("alpha = 0.1, iterations = 10000, x normalized")
plt.legend()

plt.tight_layout()
plt.show()
# Explanation
# we can see that when x is normalized, the step is really small, you have to increse the number or iterations
# or increase the alpha itself safely






# Multi dimentionality

x_multi = np.array([
    [50, 5, 6],
    [60, 6, 7],
    [70, 8, 12],
    [80, 7, 5],
    [90, 10, 14]
])
y = np.array([150, 180, 210, 240, 270])
test = np.array([[75, 6, 10]])
multi_reg = LinearRegressionGD(0.5, 10000)
x_multi_norm = multi_reg.normalize(x_multi)
test_norm = (test - x_multi.min(axis = 0)) / (x_multi.max(axis = 0) - x_multi.min(axis = 0))
w_multi, b_multi, sse_multi = multi_reg.fit(x_multi_norm, y)
print(f"w for Multidimentional x: {w_multi}\nb for Multidimentional x: {b_multi}")
y_multi_predicted = multi_reg.predict(test_norm, w_multi, b_multi)
print(f"Predicted y hat for Multidimentional x: {y_multi_predicted}")

# unforutnatily it works in code but it doesn't find the optimal solution
