import numpy as np
import matplotlib.pyplot as plt
def Fehl45(odefunc,tnow,unow,h):
    #二つののFehlberg法（頑張って写経する）
    k1 = odefunc(tnow, unow)
    k2 = odefunc(tnow+h/4, unow+(h/4)*k1)
    k3 = odefunc(tnow+(3*h/8), unow+(3*k1+9*k2)*h/32)
    k4 = odefunc(tnow+12*h/13, unow+(1932*k1-7200*k2+7296*k3)/2197)
    k5 = odefunc(tnow+h, unow+h*((439/216)*k1+8*k2+(3680/513)*k3-(845/4104)*k4))
    k6 = odefunc(tnow+h/2, unow+h*(-(8/27)*k1+2*k2-(3544/2565)*k3+(1859/4104)*k4-(11/40)*k5))
    unow = unow + h*((16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6)
    fmf = (2090*k1-22528*k3-21970*k4+15048*k5+27360*k6)/752400
    return unow,fmf
def rk45vec(odefunc, t0, T, initial, h0,epsilon,gamma):
  # if h>0, T must be > t0
  # if h<0, T must be < t0
  h=h0
  n=0
  unow=initial
  tnow=t0
  u=unow
  t=tnow
  #エラー検出用
  loop_cnt = 0
  loop_cnt2 = 0
  while (T-t0)*(T-tnow-h) >=0.0:
    h=h0
    u_next,fmf = Fehl45(odefunc,tnow,unow,h)
    e = np.linalg.norm(fmf)
    while e > epsilon*h/T:
      h = gamma*h*((epsilon*h/(T*e))**(1/4))
      u_next,fmf = Fehl45(odefunc,tnow,unow,h)
      #print(e,h,epsilon*h/T)
      e = np.linalg.norm(fmf)
      #ループが終わりそうにないならエラーを吐く
      loop_cnt+=1
      if loop_cnt<10**3:
         break
    n += 1
    #刻み幅だけ足しておく
    tnow += h
    unow= np.copy(u_next)
    print(unow,t)
    u = np.vstack((u, unow))
    t = np.append(t, tnow)
    loop_cnt2+=1
    assert loop_cnt2<10**2
  return t, u
def planet(t,u):
    R=(u[0]**2+u[1]**2)**(3/2)
    return np.array([u[2],u[3],-u[0]/R,-u[1]/R])
import time
time_sta = time.perf_counter()
t0=0.0
T=2*np.pi

k=0.8
u0=np.array([1-k, 0, 0, np.sqrt((1+k)/(1-k))])

h=0.001
t, u = rk45vec(planet, t0, T, u0, h,50,0.9)
time_end = time.perf_counter()
print("time:")
print(time_end-time_sta)
 
plt.plot(u[:,0],u[:,1],'b')
plt.xlabel('x')
plt.ylabel('y')
plt.grid('on')
plt.gca().set_aspect('equal', adjustable='box') 
plt.show()