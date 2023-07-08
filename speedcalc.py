import math

v0 = 0
m0 = 100
gas_velocity = [1.0,2.0,3.0,4.0]
mass_ratio = [0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]
mrate = 0.9
for u in gas_velocity:
    for mratio in mass_ratio:
        mf = mratio * m0
        vf = u * math.log(m0/mf) + v0
        print("u = ",u," mratio=",mratio,"  Vf=","{:.2f}".format(vf))
