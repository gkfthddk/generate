import os
import sys
import subprocess
import ROOT as rt

ls=subprocess.check_output("ls genroot/gen_pp_jj_200_*",shell=True)
#ls=subprocess.check_output("ls genroot/im25_pp_jj_200_*",shell=True)
#ls+=subprocess.check_output("ls trunk/30*jj*1000*",shell=True)
#ls+=subprocess.check_output("ls trunk/30*qq*1000*",shell=True)
#ls+=subprocess.check_output("ls trunk/30*gg*1000*",shell=True)
ls=ls.split("\n")
names=[]
nidx=[]
for ln in ls:
  #a=ln.find(".root")
  b=1
  if("-" in ln):continue
  while ln[b:].find("_")!=-1:
    b=ln[b:].find("_")+b+1
  if(b!=1):
    if(not ln[:b] in names):
      names.append(ln[:b])
      nidx.append([])
    nidx[names.index(ln[:b])].append(eval(ln[b:-5]))

print(list(set(names)))
for name in names:
  print(name,names.count(name))
  #outpath="genroot/pp_jj_200.root"
  outpath=name[name.index("gen_pp"):-1]+".root"
  #outpath="genroot/"+name[name.index("/")+1:-1]+".root"
  mychain=rt.TChain("jetAnalyser")
  for i in nidx[names.index(name)]:
    print(name+"{}.root".format(i))
    mychain.Add(name+"{}.root".format(i))
  mychain.Merge(outpath)
  
print(outpath)
