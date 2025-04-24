import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([54, 55, 65, 76, 80])

x_mean=np.mean(x)
y_mean=np.mean(y)

covariance=np.sum( (x-x_mean)*(y-y_mean) )
variance=np.sum( (x-x_mean)**2 )

slope=covariance/variance
m=slope

# y=mx+b
# y-mx=b
# b=y-mx

b = y_mean - m*x_mean 

# print(f"Slope (m): {m}")
# print(f"Intercept (b): {b}")

y_line = m*x + b

plt.scatter(x, y)
plt.plot(x, y_line)
plt.xlabel('Hours Studied')
plt.ylabel('Test Score')
plt.title('LINEAR REGRESSION')
plt.show()
