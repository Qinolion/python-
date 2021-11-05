import numpy as np
def xy(x): #信源熵
    H=0
    for i  in range(x.shape[0]):
        H=H-x[i]*np.log2(x[i])
    return H

def tjyx(xy):#条件熵值
    H=0
    for i in range(xy.shape[0]):
        for j in range(xy.shape[1]):
            H=H-xy[i][j]*np.log2(xd[i][j])
    return H

def py(xy):
    H=[0]*xy.shape[1]
    for i in range(xy.shape[1]):
        a=0
        for j in range(xy.shape[0]):
            a=a+xy[i][j]
        H[i]=a
    return H

def tjxy(xy):#条件熵值
    H=0
    for i in range(xy.shape[0]):
        for j in range(xy.shape[1]):
            H=H-xy[i][j]*np.log2(zs[i][j])
    return H

def tjyx(xy,xd):
    H=0
    for i in range(xy.shape[0]):
        for j in range(xy.shape[1]):
            H=H-xy[i][j]*np.log2(xd[i][j])
    return H

def lh(xy):#联合熵
    H=0
    for i in range(xy.shape[0]):
        for j in range(xy.shape[1]):
            H=H-xy[i][j]*np.log2(xy[i][j])
    return H  

def jh(xy,x):
    y=py(xy)
    H=0
    C=0.0
    for i in range(xy.shape[0]):
        for j in range(xy.shape[1]):
            H=H+xy[i][j]*np.log2(xy[i][j]/(x[i]*y[j]))
    return H


def C(xd):#计算信道容量
    xd1=xd*np.log2(xd)
    xd2=np.array(xd.shape[1]*[0.0])
    a=0
    for i in range(xd.shape[0]):
        for j in range(xd.shape[1]):
            a=a+xd[i][j]*xd1[i][j]
        xd2[i]=a
    B=np.linalg.solve(xd,xd2)
    a=0
    for i in range (B.shape[0]):
        a=a+2**B[i]
    C=np.log2(a)
    b=np.array([0.0]*xd.shape[1])
    a=np.array([0.0]*xd.shape[0])    
    for i in range (b.shape[0]):
        b[i]=2**(B[i]-C)
    a=np.linalg.solve(xd,b)
    if a.min()<0:
        c={'错误 C 不存在'}
    return C

    



#自定义 信源 信道矩阵
px=np.array([0.1,0.2,0.3,0.4])
xd=np.array([[0.2,0.3,0.1,0.4],[0.6,0.2,0.1,0.1],[0.5,0.2,0.1,0.2],[0.1,0.3,0.4,0.2]])
#计算剩余矩阵
pxy=xd*px.reshape(px.shape[0],1)
zs=pxy/py(pxy)

print("信源熵=",xy(px))
print("条件熵Y|X=",tjyx(pxy,xd))
print('条件熵X|Y=',tjxy(pxy))
print('联合熵=',lh(pxy))
print('交互熵=',jh(pxy,px))
print('信道容量=',C(xd))



