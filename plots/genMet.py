import ROOT
from MetTools.photonAnalysis.files import *

mg_hep = ROOT.TChain("Delphes")
for f in MG_hep:
  mg_hep.Add(f)

