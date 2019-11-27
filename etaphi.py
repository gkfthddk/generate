import numpy as np
import matplotlib.pyplot as plt
import ROOT as rt
pdg = rt.TDatabasePDG();
f=rt.TFile("~/generate/genroot/gen_pp_jj_500.root","read")
d=f.Get("jetAnalyser")
"""
415 317
487 372
72  55
343 262
144 110
271 207
216 165
199 152
288 220
127 97
542 414
360 275
55  42
470 359
432 330
17  13
398 304
"""
resphi=72
reseta=55
cyl=rt.TH2F("hist","hist",resphi,-rt.TMath.Pi(),rt.TMath.Pi(),reseta,-2.4,2.4)
jet=rt.TH2F("his2t","his2t",resphi,-rt.TMath.Pi(),rt.TMath.Pi(),reseta,-2.4,2.4)
rt.gStyle.SetOptStat(0)
ent=50000
img=np.zeros(resphi*reseta)
#img=np.zeros((55,72))
phibin,etabin=[0,0]
def dr(i=None):
  if(i==None):i=np.random.randint(ent)
  d.GetEntry(i)
  ev=d.event
  for j in range(100):
    d.GetEntry(j)
    if(ev!=d.event):
      i=i+j
      break
  cyl.Reset()
  jet.Reset()
  img=np.zeros(resphi*reseta)
  deposit=0
  d.GetEntry(i)
  print(d.num_jets)
  for j in range(d.num_jets):
    d.GetEntry(i+j)
    if(j<2):
      eta=d.eta
      phi=d.phi
      jet.Fill(phi,eta,(2-j)*100)
    deposit+=d.num_dau
    for k in range(d.num_dau):
      eta=d.dau_deta[k]+d.eta
      phi=d.dau_dphi[k]+d.phi
      pt=d.dau_pt[k]
      if(abs(eta)>2.4):continue
      if(abs(phi)>3.14159):continue
      cyl.Fill(phi,eta,pt)
      etabin=int(reseta*(eta+2.4)/(2*2.4))
      phibin=int(resphi*(phi+3.14159)/(2*3.14159))
      pix=72*int(etabin)+int(phibin)
      img[pix]=img[pix]+pt
  print("deposit ",deposit)
  #print("mean dau",d/100.,d)
  #import matplotlib.pyplot as plt
  #plt.hist(d)
  #plt.show()
  #cyl.Draw("surf5 cyl")
  cyl.Draw("col")
  jet.SetFillColor(2)
  jet.Draw("box same")
  #plt.imshow((imgset[i][2]+imgset[i][3]).reshape((reseta,resphi)),origin='lower',cmap="viridis")
  #plt.imshow(img.reshape((reseta,resphi))/img.max(),origin='lower',cmap="viridis")
  #plt.show()
dr(np.random.randint(ent))
