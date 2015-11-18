import ROOT
from photonAnalysis.metComparison.files_private import *
#from photonAnalysis.metComparison.files_cms import *
mg_delphes_atlas = ROOT.TChain("Delphes")
for f in MG_delphes_atlas:
  mg_delphes_atlas.Add(f)

p8_delphes_atlas = ROOT.TChain("Delphes")
for f in P8_delphes_atlas:
  p8_delphes_atlas.Add(f)

mg_delphes_cms = ROOT.TChain("Delphes")
for f in MG_delphes_cms:
  mg_delphes_cms.Add(f)

p8_delphes_cms = ROOT.TChain("Delphes")
for f in P8_delphes_cms:
  p8_delphes_cms.Add(f)

mg_hep = ROOT.TChain("Delphes")
for f in MG_hep:
  mg_hep.Add(f)

p8_hep = ROOT.TChain("Delphes")
for f in P8_hep:
  p8_hep.Add(f)

mg_delphes_atlas.AddFriend(mg_hep)
p8_delphes_atlas.AddFriend(p8_hep)
mg_delphes_cms.AddFriend(mg_hep)
p8_delphes_cms.AddFriend(p8_hep)
