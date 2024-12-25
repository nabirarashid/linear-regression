import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
rainfall = [1.65, 1.46, 2.05, 3.03, 3.35, 3.55, 2.85, 3.55, 3.35, 2.85, 2.05, 1.65]

def get_gradient_at_b(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
    x_val = x[i]
    y_val = y[i]
    diff += (y_val - ((m * x_val) + b))
  b_gradient = -(2/N) * diff  
  return b_gradient

def get_gradient_at_m(x, y, b, m):
  N = len(x)
  diff = 0
  for i in range(N):
      x_val = x[i]
      y_val = y[i]
      diff += x_val * (y_val - ((m * x_val) + b))
  m_gradient = -(2/N) * diff  
  return m_gradient

#Your step_gradient function here
def step_gradient(b_current, m_current, x, y, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    b_final = b_current - (learning_rate * b_gradient)
    m_final = m_current - (learning_rate * m_gradient)
    return [b_final, m_final]
  
#Your gradient_descent function here:
#upgrades the values of b & m each time an iteration occurs
def gradient_descent(x,y,num_iterations, learning_rate):
   b = 0
   m = 0
   for i in range(num_iterations):
    b, m = step_gradient(b,m,x,y,learning_rate)
   return [b, m]



plt.plot(months, rainfall, 'o')

b, m = gradient_descent(months, rainfall, 500, 0.001)
predicted_rainfall = [m*month + b for month in months]

plt.plot(months,predicted_rainfall)
plt.show()
