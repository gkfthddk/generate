import sys
import ROOT as rt
import numpy as np
rt.gSystem.Load("libDelphes")
rt.gInterpreter.ProcessLine('.include /home/yulee/QGJets_10_5_0_pre1/src/Delphes-3.4.1')
rt.gInterpreter.ProcessLine('.include /home/yulee/QGJets_10_5_0_pre1/src/Delphes-3.4.1/external')
rt.gInterpreter.ProcessLine('#include "classes/DelphesClasses.h"')
#rt.gInterpreter.Declare('#include "/home/yulee/QGJets_10_5_0_pre1/src/Delphes-3.4.1/classes/DelphesClasses.h"')
#rt.gInterpreter.Declare('#include "/home/yulee/QGJets_10_5_0_pre1/src/Delphes-3.4.1/external/ExRootAnalysis/ExRootTreeReader.h"')
#rt.gInterpreter.Declare('#include "/home/yulee/QGJets_10_5_0_pre1/src/Delphes-3.4.1/external/ExRootAnalysis/ExRootResult.h"')
pdg = rt.TDatabasePDG();
pdg.ReadPDGTable("/home/yulee/source/root/etc/pdg_table.txt")
f=rt.TFile("~/generate/root/temp_pp_jj_500_10.root","read")
d=f.Get("Delphes")
d.GetEntry(0)
#chain = rt.TChain("Delphes")
#chain.Add("~/generate/root/temp_pp_jj_500_20.root")
#treeReader = rt.ExRootTreeReader(chain)
#branchJet = treeReader.UseBranch("Jet")
def mother(num):
  m1=int(d.GetLeaf("Particle.M1").GetValue(num))
  if(m1==-1):
    return(num)
  num=m1
  return mother(num)
  #return fm(num)
def fm(num):
  m1=int(d.GetLeaf("Particle.M1").GetValue(num))
  m2=int(d.GetLeaf("Particle.M2").GetValue(num))
  return(m1,m2)
def fd(num):
  d1=int(d.GetLeaf("Particle.D1").GetValue(num))
  d2=int(d.GetLeaf("Particle.D2").GetValue(num))
  return(d1,d2)
def pid(num):
  m1=int(d.GetLeaf("Particle.PID").GetValue(num))
  return(pdg.GetParticle(m1).GetName())
def pt(num):
  m1=d.GetLeaf("Particle.PT").GetValue(num)
  return(m1)
  #return(pdg.GetParticle(m1).GetName())
def fe(num):
  m1=d.GetLeaf("Particle.E").GetValue(num)
  return(m1)
def fp(num):
  m1=d.GetLeaf("Particle.PT").GetValue(num)
  return(m1)

def ydaus(num,ldaus):  
  d1,d2=fd(num)
  if(d1==-1 and d2==-1):
    yield num
  if(d1!=-1 and not d1 in ldaus):
    ldaus.append(d1)
    for loo in ydaus(d1,ldaus):
      yield loo
  if(d2!=-1 and not d2 in ldaus):
    ldaus.append(d2)
    for loo in ydaus(d2,ldaus):
      yield loo
def dl(num):
  return np.unique(list(ydaus(num,[])))
print("@")
