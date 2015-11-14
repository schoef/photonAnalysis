import ROOT

#DELPHES
coll = [
["EFlowTrack","PT"], 
["EFlowPhoton", "ET"],
["EFlowNeutralHadron", "ET"],
]

def delphes_metFormula(coll=coll):
  sstring = " + ".join(["Sum$("+s[0]+"."+s[1]+"*cos("+s[0]+".Phi))" for s in coll])
  return "sqrt(("+sstring+")**2 + ("+sstring.replace("cos","sin")+")**2)"
def delphes_sumPtFormula(coll=coll):
  sstring = " + ".join(["Sum$("+s[0]+"."+s[1]+")" for s in coll])
  return "("+sstring+")"

#HEP MC
hep_met = "sqrt( Sum$(Particle.Px*(Particle.Status==1))**2 + Sum$(Particle.Py*(Particle.Status==1))**2 )"
hep_sumPt = " Sum$( sqrt( (Particle.Px*(Particle.Status==1))**2 + (Particle.Py*(Particle.Status==1))**2 ) )"

##"(EFlowTrack.PT*cos(EFlowTrack.Phi) +  + EFlowTrack.PT*sin(EFlowTrack.Phi)"
#c1 = ROOT.TCanvas()
#c.Draw(metFormula()+":MissingET.MET>>h3(50,0,400,50,0,400)","","COLZ")
#c1.SetLogz()

#c.GetEntries("MissingET.MET>150&&PhotonMA5[0].PT>125&&abs(PhotonMA5[0].Eta)<1.37&&cos(MissingET.Phi-PhotonMA5[0].Phi)<cos(0.4)&&JetMA5_size<3")
