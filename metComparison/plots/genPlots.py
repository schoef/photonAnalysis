import ROOT
from photonAnalysis.metComparison.files_private import *
from photonAnalysis.metComparison.files_cms import *
ROOT.gROOT.LoadMacro("$CMSSW_BASE/src/StopsDilepton/tools/scripts/tdrstyle.C")
ROOT.setTDRStyle()

mg_hep = ROOT.TChain("Delphes")
for f in MG_hep:
  mg_hep.Add(f)

#p8_hep = ROOT.TChain("Delphes")
#for f in P8_hep:
#  p8_hep.Add(f)

from StopsDilepton.tools.helpers import getChain, getObjDict, getEList, getVarValue, getPlotFromChain
from StopsDilepton.samples.cmgTuples_Spring15_mAODv2_25ns_0l_postProcessed import GJets
gJets = getChain(GJets, histname="")

stuff=[]
for name, varP, varC, binning in [
#  ('MEx', "Sum$(Particle.Px*(Particle.Status==1))", 'met_genPt*cos(met_genPhi)',  [100,-1,1]),
  ('ptGamma', "Max$(Particle.PT*(Particle.Status==1&&abs(Particle.PID)==22))", 'Max$(genPartAll_pt*( abs(genPartAll_pdgId)==22 ))', [100,0,500]),
#  ('SumPt', "Sum$(Particle.PT*(Particle.Status==1))", 'met_sumEt', [100,0,3000]),

  ]:
  h_c =getPlotFromChain(gJets, varC, binning,"1",weight="weight")
  h_mg=getPlotFromChain(mg_hep, varP, binning,"1","1")
  h_p8=getPlotFromChain(p8_hep, varP, binning,"1","1")
  h_p8.SetLineColor(ROOT.kRed)
  h_c.SetLineColor(ROOT.kBlue)
  h_p8.SetMarkerColor(ROOT.kRed)
  h_mg.SetMarkerColor(ROOT.kBlack)
  h_c .SetMarkerColor(ROOT.kBlue)
  h_p8.SetMarkerSize(0)
  h_mg.SetMarkerSize(0)
  h_c .SetMarkerSize(0)
  h_p8.SetMarkerStyle(0)
  h_mg.SetMarkerStyle(0)
  h_c .SetMarkerStyle(0)
  c1 = ROOT.TCanvas()
  l=ROOT.TLegend(0.75,0.75,1.0,1.0)
  l.SetFillColor(0)
  l.SetShadowColor(ROOT.kWhite)
  l.SetBorderSize(1)
  l.AddEntry(h_c, "CMS")
  l.AddEntry(h_mg, "Madgraph")
  l.AddEntry(h_p8, "Pythia8")
  stuff.append(l)
  h_c.GetXaxis().SetTitle(name)
  h_c.Draw()
  h_mg.Scale(h_c.Integral()/h_mg.Integral())
  h_mg.Draw('same')
  c1.SetLogy()
  h_p8.Scale(h_c.Integral()/h_p8.Integral())
  h_p8.Draw("same")
  l.Draw()

  c1.Print("/afs/hephy.at/user/r/rschoefbeck/www/photonAna/gen_"+name+".png")

#mg_hep.Draw("Sum$(Particle.Px*(Particle.Status==1))","")
#p8_hep.Draw("Sum$(Particle.Px*(Particle.Status==1))","","same")

#mg_hep.Draw("Max$(Particle.PT*(Particle.Status==1&&abs(Particle.PID)==22))")
#p8_hep.Draw("Max$(Particle.PT*(Particle.Status==1&&abs(Particle.PID)==22))","","same")

#h_mg.Draw()
#h_p8.SetLineColor(ROOT.kRed)
#h_p8.Draw("same")

# OBJ: TLeafElement  Event_  Event_ : 0 at: 0x5fe7de0
# OBJ: TLeafElement  Event.fUniqueID fUniqueID[Event_] : 0 at: 0x5fe42f0
# OBJ: TLeafElement  Event.fBits fBits[Event_] : 0 at: 0x5ff3f20
# OBJ: TLeafElement  Event.Number  Number[Event_] : 0 at: 0x6000060
# OBJ: TLeafElement  Event.ReadTime  ReadTime[Event_] : 0 at: 0x600c1d0
# OBJ: TLeafElement  Event.ProcTime  ProcTime[Event_] : 0 at: 0x6018370
# OBJ: TLeafElement  Event.ProcessID ProcessID[Event_] : 0 at: 0x6024510
# OBJ: TLeafElement  Event.MPI MPI[Event_] : 0 at: 0x6030680
# OBJ: TLeafElement  Event.Weight  Weight[Event_] : 0 at: 0x603c7c0
# OBJ: TLeafElement  Event.Scale Scale[Event_] : 0 at: 0x6048900
# OBJ: TLeafElement  Event.AlphaQED  AlphaQED[Event_] : 0 at: 0x6054a70
# OBJ: TLeafElement  Event.AlphaQCD  AlphaQCD[Event_] : 0 at: 0x6060c10
# OBJ: TLeafElement  Event.ID1 ID1[Event_] : 0 at: 0x606cd80
# OBJ: TLeafElement  Event.ID2 ID2[Event_] : 0 at: 0x6078ec0
# OBJ: TLeafElement  Event.X1  X1[Event_] : 0 at: 0x6085000
# OBJ: TLeafElement  Event.X2  X2[Event_] : 0 at: 0x6091140
# OBJ: TLeafElement  Event.ScalePDF  ScalePDF[Event_] : 0 at: 0x609d2b0
# OBJ: TLeafElement  Event.PDF1  PDF1[Event_] : 0 at: 0x60a9420
# OBJ: TLeafElement  Event.PDF2  PDF2[Event_] : 0 at: 0x60b5560
# OBJ: TLeafI  Event_size  Event_size : 0 at: 0x60cd7e0
# OBJ: TLeafElement  Particle_ Particle_ : 0 at: 0x60db1d0
# OBJ: TLeafElement  Particle.fUniqueID  fUniqueID[Particle_] : 0 at: 0x60db0f0
# OBJ: TLeafElement  Particle.fBits  fBits[Particle_] : 0 at: 0x60eae60
# OBJ: TLeafElement  Particle.PID  PID[Particle_] : 0 at: 0x60fad50
# OBJ: TLeafElement  Particle.Status Status[Particle_] : 0 at: 0x610aa80
# OBJ: TLeafElement  Particle.IsPU IsPU[Particle_] : 0 at: 0x611a730
# OBJ: TLeafElement  Particle.M1 M1[Particle_] : 0 at: 0x612a3b0
# OBJ: TLeafElement  Particle.M2 M2[Particle_] : 0 at: 0x613a0b0
# OBJ: TLeafElement  Particle.D1 D1[Particle_] : 0 at: 0x6149db0
# OBJ: TLeafElement  Particle.D2 D2[Particle_] : 0 at: 0x6159ab0
# OBJ: TLeafElement  Particle.Charge Charge[Particle_] : 0 at: 0x6169800
# OBJ: TLeafElement  Particle.Mass Mass[Particle_] : 0 at: 0x61794d0
# OBJ: TLeafElement  Particle.E  E[Particle_] : 0 at: 0x6189150
# OBJ: TLeafElement  Particle.Px Px[Particle_] : 0 at: 0x6198e50
# OBJ: TLeafElement  Particle.Py Py[Particle_] : 0 at: 0x61a8b50
# OBJ: TLeafElement  Particle.Pz Pz[Particle_] : 0 at: 0x61b8850
# OBJ: TLeafElement  Particle.PT PT[Particle_] : 0 at: 0x61c8550
# OBJ: TLeafElement  Particle.Eta  Eta[Particle_] : 0 at: 0x61d8250
# OBJ: TLeafElement  Particle.Phi  Phi[Particle_] : 0 at: 0x61e7f50
# OBJ: TLeafElement  Particle.Rapidity Rapidity[Particle_] : 0 at: 0x61f7cb0
# OBJ: TLeafElement  Particle.T  T[Particle_] : 0 at: 0x6207970
# OBJ: TLeafElement  Particle.X  X[Particle_] : 0 at: 0x6217670
# OBJ: TLeafElement  Particle.Y  Y[Particle_] : 0 at: 0x6227370
# OBJ: TLeafElement  Particle.Z  Z[Particle_] : 0 at: 0x6237070
# OBJ: TLeafI  Particle_size Particle_size : 0 at: 0x6252830

