#A
# Hàm mật độ biên f_X(x) của X
def marginal_x(x):
    integral_y = 0
    for y in range(0, 3):  # Tích phân theo y từ 0 đến 3
        integral_y += (x + y) / (pi * (1 + x**2 + y**2))
    return integral_y

x = 1
print("f_X(x):", marginal_x(x))

# Hàm mật độ biên f_Y(y) của Y
def marginal_y(y):
    integral_x = 0
    for x in range(0, 3):  # Tích phân theo x từ 0 đến 3
        integral_x += (x + y) / (pi * (1 + x**2 + y**2))
    return integral_x

y = 0.5
print("f_Y(y):", marginal_y(y))

#B
# Hàm mật độ điều kiện f(x|y) của X
def conditional_x(x, y):
    if x >= 0 and y >= 0:
        return (x + y) / (pi * (1 + x**2 + y**2) * marginal_y(y))
    else:
        return 0
        
print("f(x|y):", conditional_x(x, y))

# Hàm mật độ điều kiện f(y|x) của Y
def conditional_y(x, y):
    if x >= 0 and y >= 0:
        return (x + y) / (pi * (1 + x**2 + y**2) * marginal_x(x))
    else:
        return 0
print("f(y|x):", conditional_y(x, y))