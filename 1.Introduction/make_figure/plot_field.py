import numpy as np
import matplotlib.pyplot as plt

# 関数
def F(x, y):
    return x ** 2 / 20 + y ** 2

# それぞれの微分
def diff(x, y):
    """ (dF/dx, dF/dy)を返す """
    return (x / 10, 2 * y)

# フィールドの定義
fig = plt.figure(figsize=(8, 6), dpi=150, facecolor="white")
ax = fig.add_subplot(111)

# 等高線プロット
x1 = np.linspace(-10, 10, 200)
y1 = np.linspace(-5, 5, 100)
X1, Y1 = np.meshgrid(x1, y1)
Z = F(X1, Y1)
ax.contour(X1, Y1, Z)

# ベクトルプロット
x2 = np.linspace(-10, 10, 20)
y2 = np.linspace(-5, 5, 10)
X2, Y2 = np.meshgrid(x2, y2)

dFdx, dFdy = diff(X2, Y2)
ax.quiver(X2, Y2, -dFdx, -dFdy)

# 軸
ax.set_xlabel("x")
ax.set_ylabel("y")
fig.suptitle("$z = \\frac{1}{20}x^2 + y^2$", y=0.95)

# 画像の保存
fig.savefig("slides/images/anti.png")
