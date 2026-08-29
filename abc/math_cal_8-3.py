import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML
import plotly.graph_objects as go
import plotly.offline as pyo
#（斉次）熱方程式、零Dirichlet境界条件、陽的スキーム
def heat_0dbc_ex1(L, kappa, initial, N, T, lam, num):
    
  h = L/(N+1)
  tau = lam*h*h/kappa
  nmax = int(T/tau)
  step=int(max(1, nmax/num))
  
  xgrid=np.linspace(0.0, L, N+2)
  tgrid=np.array([0.0])
  u=np.vectorize(initial)(xgrid)
  sol=np.copy(u)
  
  for n in range(nmax):
    u[1:N+1] = (1-2*lam)*u[1:N+1]+lam*(u[0:N]+u[2:N+2])+tau*np.exp(u[1:N+1])
    tnow = (n+1)*tau
    if (n+1)%step==0:
      sol=np.vstack((sol,u))
      tgrid=np.append(tgrid, tnow)

  return xgrid, tgrid, sol 
#図のプロット、一枚の図に、グラフを重ねる
def plot_solution(xgrid, uvect):
  # 描画に関するパラメータの設定
  umax = np.max(sol)
  umin = np.min(sol)
  ulength = umax - umin
  umax += 0.05 * ulength
  umin -= 0.05 * ulength
  # t = 0                  
  plt.plot(xgrid,uvect[0,:],color='#ff8c00')
  # t > 0
  for n in range(1,uvect.shape[0]):
    plt.plot(xgrid,uvect[n,:],color='#00bfff')
  
  plt.xlabel('x')
  plt.ylabel('u')
  plt.ylim(umin, umax)
  plt.grid('on')
  plt.show()
# xtu空間での曲線の描画
# plotly.graph_objects，plotly.offline モジュールを使う
# xgrid.shape <= tgrid.shape でないと上手く描けない
def plot_solution3d(xgrid, tgrid, uvect):  
  # 3Dプロットの作成
  fig = go.Figure()
  
  Nt = tgrid.shape[0]
  # t = 0
  n = 0
  tval = tgrid[n]*np.ones(Nt)
  fig.add_trace(go.Scatter3d(x=xgrid, y=tval, z=uvect[n,:], mode='lines',line=dict(color='#ff8c00', width=2)))
  # t > 0 
  for n in range(1, Nt):
    tval = tgrid[n]*np.ones(Nt)
    fig.add_trace(go.Scatter3d(x=xgrid, y=tval, z=uvect[n,:], mode='lines',line=dict(color='#00bfff', width=2)))

  # レイアウトの設定
  fig.update_layout(scene=dict(xaxis_title='x', yaxis_title='time', zaxis_title='u'))
  fig.update_layout(scene=dict(camera=dict(eye=dict(x=1.5, y=-1.5, z=1))))
  fig.update_layout(showlegend=False)

  # プロットの表示
  pyo.plot(fig)
  with open('temp-plot.html', 'r') as file:
    html_content = file.read()
  display(HTML(html_content))
  # Google Colaboratoryでなければ、上の4行は、以下の1行で置き換えられる（はず）
  # fig.show()
#アニメーションの作成
# IPython.displayモジュールを使う
def plot_animation(xgrid, tgrid, uvect):
  # 描画に関するパラメータの設定
  umax = np.max(sol)
  umin = np.min(sol)
  xmax = np.max(xgrid)
  xmin = np.min(xgrid)
  ulength = umax - umin
  utop = umax + 0.1*ulength
  umax += 0.05*ulength
  umin -= 0.05*ulength
  xmid = (xmax+xmin)/2
  xlength = xmax - xmin
  xmax += 0.05*xlength
  xmin -= 0.05*xlength
  
  # fig, axオブジェクトを作成
  fig, ax = plt.subplots()
  ims = []
  
  # t = 0
  n = 0
  im, = ax.plot(xgrid, uvect[n, :], color='#ff8c00')
  title = ax.text(xmid, utop, f'time={tgrid[n]:.4f}', ha='center', va='center', fontsize=15)
  ims.append([im, title])
    
  # t > 0
  for n in range(1, uvect.shape[0]):
    im, = ax.plot(xgrid, uvect[n, :], color='#00bfff')
    title = ax.text(xmid, utop, f'time={tgrid[n]:.4f}', ha='center', va='center', fontsize=15)
    ims.append([im, title])
    
  # 各軸のラベル
  ax.set_xlabel(r"$x$", fontsize=15)
  ax.set_ylabel(r"$u$", fontsize=15)
  # グラフの範囲を設定
  ax.set_xlim([xmin, xmax])
  ax.set_ylim([umin, umax])
  ax.grid(True)

  # ArtistAnimationにfigオブジェクトとimsを代入してアニメーションを作成
  return animation.ArtistAnimation(fig, ims)
# 初期値
def initial1(x):
  return np.sin(np.pi*x)
  
#パラメータの設定
L = 1.0
kappa = 2.0
N = 51
T = 1.0
lam = 0.4
num = 60

#熱方程式の計算
x, tn, sol = heat_0dbc_ex1(L, kappa, initial1, N, T, lam, num)

#図の表示
plot_solution(x, sol)

#3D図の表示
plot_solution3d(x, tn, sol)

#アニメーションを表示
anim = plot_animation(x, tn, sol)
#結果をheat.gifに保存（Googleドライブをマウントしておくこと！）
anim.save('/content/drive/MyDrive/Colab Notebooks/fig/heat.gif', writer='pillow')
rc('animation', html='jshtml')
plt.close()
anim
