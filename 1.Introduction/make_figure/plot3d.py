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
fig = plt.figure(figsize=(8, 10), dpi=100, facecolor="white")
ax = fig.add_subplot(111, projection="3d")

# 等高線プロット
x1 = np.linspace(-10, 10, 200)
y1 = np.linspace(-5, 5, 100)
X1, Y1 = np.meshgrid(x1, y1)
Z = F(X1, Y1)

# 3Dプロット
ax.plot_surface(X1, Y1, Z, cmap="viridis")

# 画像の保存
fig.savefig("../images/anti.png")
