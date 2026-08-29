#複合NC則（ベクトル計算版）
import numpy as np

#複合中点則
def mid2(f, a, b, x):
  xmid=0.5*(x[1:]+x[:-1])
  h=x[1:]-x[:-1]
  return np.amax(h), np.dot(f(xmid) , h)

#複合台形則
def trape2(f, a, b, x):
  h=x[1:]-x[:-1]
  return np.amax(h), 0.5*np.dot(f(x[:-1]) + f(x[1:]) , h)

#複合Simpson則
def simp2(f, a, b, x):
  xmid=0.5*(x[1:]+x[:-1])
  h=x[1:]-x[:-1]
  return np.amax(h), np.dot(f(x[:-1]) + 4.0*f(xmid) + f(x[1:]) , h) / 6.0

#複合NC則の実行
import numpy as np

#被積分関数
a=0
b=1
def integrand(x): 
  return (x**2)*np.sin(np.pi*x)
ans1 = []
ans2 = []
ans3 = []
exact = (np.pi**2-4)/np.pi**3
for m in range(5,35):
    #分割
    m=10
    x=np.linspace(a,b,m+1)

    #数値積分
    hsize = np.empty(3)
    val = np.empty(3)
    hsize[0], val[0] = mid2(integrand, a, b, x)
    hsize[1], val[1] = trape2(integrand, a, b, x)
    hsize[2], val[2] = simp2(integrand, a, b, x)

    #厳密解
    err = np.empty(3)
    for i in range(3):
        err[i] = np.abs(val[i]-exact)
    ans1.append(err[0])
    ans2.append(err[1])
    ans3.append(err[2])
def covergence_rate(ei):
    q = np.array([np.log(ei[k+1]/ei[k]) / np.log(ei[k]/ei[k-1]) for k in range(1,len(ei)-1, 1)])
    return q
print(covergence_rate(ans1))
print(covergence_rate(ans2))
print(covergence_rate(ans3))