import numpy as np
import matplotlib.pyplot as plt

# Fieldクラス（最適化したいフィールド）
class Field:
    def __init__(self, func, xrange, yrange, sample=100):
        """
        Args
        ----
        func : (x, y) -> z
            x、yをとってzの値を返す関数
        xrange : (int, int)
            xの範囲
        yrange : (int, int)
            yの範囲
        sample : int
            フィールドの一片を何分割するか
        """
        self.func = func
        self.x = np.linspace(*xrange, sample)
        self.y = np.linspace(*yrange, sample)
        self.dx = (xrange[1] - xrange[0]) / sample  # 勾配の計算に使用する微少量
        self.dy = (yrange[1] - yrange[0]) / sample  # 勾配の計算に使用する微少量
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.Z = self.func(self.X, self.Y)

    def calc_grad(self, params):
        """
        数値微分を用いて、(x, y)におけるフィールドの勾配を計算する
        
        Args
        ----
        param : dict("x": float, "y": float)
            現在の位置

        Returns
        ----
        dict("x": float, "y": float)
        """
        eps = 0.001
        f = self.func
        x, y = params["x"], params["y"]
        dx, dy = self.dx, self.dy
        dfdx = ( f(x + dx, y) - f(x - dx, y) ) / (2 * dx + eps)
        dfdy = ( f(x, y + dy) - f(x, y - dy) ) / (2 * dy + eps)
        grad = {
            "x": dfdx,
            "y": dfdy,
        }
        return grad

    def plot(self, route=[]):
        """
        フィールドの状態をプロットする

        Args
        ----
        [route] : list( dict("x": float, "y": float) )
        """
        fig = plt.figure(figsize=(8, 6))
        ax = fig.add_subplot(111)
        ax.contour(self.X, self.Y, self.Z)

        # ルートを表示
        if len(route) >= 2:
            for cur, nxt in zip(route, route[1:]):
                cx, cy = cur["x"], cur["y"]
                nx, ny = nxt["x"], nxt["y"]
                u, v = nx - cx, ny - cy
                
                # プロット
                ax.quiver(cx, cy, u, v, angles='xy', scale_units='xy', scale=1, width=0.005)
        
        return fig


## Adventurer
class Adventurer:
    def __init__(self, x, y):
        self.params = {
            "x": x,
            "y": y,
        }
        self.route = [self.params.copy()]
    
    def optimize(self, field, method, rep=20):
        """
        与えられた方法で、パラメータの最適化を行う

        Args
        ----
        field : Field
            最適化を行うフィールド
        method : Optimizer
            パラメータの最適化を行うクラス
        rep : int
            最適化を行う回数
        """
        for _ in range(rep):
            grad = field.calc_grad(self.params)
            method.update(self.params, grad)
            self.route.append(self.params.copy())
