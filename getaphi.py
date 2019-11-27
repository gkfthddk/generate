import numpy as np
import matplotlib.pyplot as plt
import ROOT as rt
pdg = rt.TDatabasePDG();
f=rt.TFile("~/generate/root/temp_pp_jj_500_10.root","read")
d=f.Get("Delphes")
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
ent=d.GetEntries()
img=np.zeros(resphi*reseta)
#img=np.zeros((55,72))
phibin,etabin=[0,0]
def fm(num):
  return int(d.GetLeaf("Particle.M1").GetValue(num))
def hard(num):
  m1=fm(num)
  #if(int(d.GetLeaf("Particle.M1").GetValue(m1))==-1):
  #if(m1==-1):
  if(fm(fm(m1))==-1):
    return(num)
  num=m1
  return hard(num)
def dr(i=None):
  if(i==None):i=np.random.randint(ent)
  print(i)
  d.GetEntry(i)
  cyl.Reset()
  jet.Reset()
  img=np.zeros(resphi*reseta)
  
  eta=d.GetLeaf("GenJet.Eta").GetValue(0)
  phi=d.GetLeaf("GenJet.Phi").GetValue(0)
  print("pid1 ",d.GetLeaf("GenJet.Flavor").GetValue(0))
  jet.Fill(phi,eta,200)
  eta=d.GetLeaf("GenJet.Eta").GetValue(1)
  phi=d.GetLeaf("GenJet.Phi").GetValue(1)
  print("pid2 ",d.GetLeaf("GenJet.Flavor").GetValue(1))
  jet.Fill(phi,eta,100)
  """eta=d.GetLeaf("Jet.Eta").GetValue(0)
  phi=d.GetLeaf("Jet.Phi").GetValue(0)
  jet.Fill(phi,eta,150)
  eta=d.GetLeaf("Jet.Eta").GetValue(1)
  phi=d.GetLeaf("Jet.Phi").GetValue(1)
  jet.Fill(phi,eta,130)"""
  print("particles ",d.GetLeaf("Particle.PT").GetLen())
  deposit=0
  hlist=[]
  for j in range(d.GetLeaf("Particle.PT").GetLen()):
    if(int(d.GetLeaf("Particle.D1").GetValue(j))!=-1):continue
    mh=hard(j)
    if(not mh in hlist):
      hlist.append(mh)
    pt=11+hlist.index(mh)
    deposit+=1
    eta=d.GetLeaf("Particle.Eta").GetValue(j)
    phi=d.GetLeaf("Particle.Phi").GetValue(j)
    #pt=d.GetLeaf("Particle.PT").GetValue(j)
    if(abs(eta)>2.4):continue
    if(abs(phi)>3.14159):continue
    #theta=2.*rt.TMath.ATan(rt.TMath.Exp(-seq[i][j][1]))
    #phi=seq[i][j][2]
    cyl.Fill(phi,eta,pt)
    #cyl.Fill(seq[i][j][2],seq[i][j][1],seq[i][j][0])
    etabin=int(reseta*(eta+2.4)/(2*2.4))
    phibin=int(resphi*(phi+3.14159)/(2*3.14159))
    pix=72*int(etabin)+int(phibin)
    img[pix]=img[pix]+pt
  for j in hlist:
    print("PID and E ",pdg.GetParticle(int(d.GetLeaf("Particle.PID").GetValue(j))).GetName(),d.GetLeaf("Particle.PT").GetValue(j))
  for j in range(d.GetLeaf("GenJet.PT").GetLen()):
    print("PID and E ",d.GetLeaf("GenJet.PT").GetValue(j))

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
