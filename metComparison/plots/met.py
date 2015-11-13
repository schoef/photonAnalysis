import ROOT
c = ROOT.TChain("Delphes")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run1/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run2/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run3/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run4/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run5/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run6/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run7/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run8/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run9/output.root")
c.Add("/scratch/skulkarni/monophoton_backgrounds/pp-gammaj/Events/pp-gammaj_13TeV_100k_run10/output.root")

c.Draw("JetMA5_size")
coll = [
["EFlowTrack","PT"], 
["EFlowPhoton", "ET"],
["EFlowNeutralHadron", "ET"],
]

def metFormula(coll=coll):
  sstring = " + ".join(["Sum$("+s[0]+"."+s[1]+"*cos("+s[0]+".Phi))" for s in coll])
  return "sqrt(("+sstring+")**2 + ("+sstring.replace("cos","sin")+")**2)"

#"(EFlowTrack.PT*cos(EFlowTrack.Phi) +  + EFlowTrack.PT*sin(EFlowTrack.Phi)"
c1 = ROOT.TCanvas()
c.Draw(metFormula()+":MissingET.MET>>h3(50,0,400,50,0,400)","","COLZ")
c1.SetLogz()

#c.GetEntries("MissingET.MET>150&&PhotonMA5[0].PT>125&&abs(PhotonMA5[0].Eta)<1.37&&cos(MissingET.Phi-PhotonMA5[0].Phi)<cos(0.4)&&JetMA5_size<3")
