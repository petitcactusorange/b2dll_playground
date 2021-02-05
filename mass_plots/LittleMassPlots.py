'''
Feb 2021
Let's use a python script to make Carla happy
'''
import ROOT as r
from math import *
from ROOT import gStyle, gROOT



import ROOT
import argparse
import getopt
import numpy as np
from math import acos
from array import array
from copy import deepcopy

gStyle.SetOptStat("")
gROOT.ProcessLine(".x ../utils/lhcbStyle.C")


from math import pow


if __name__ == '__main__':


     #Hallo little files
     fBsToKstmm = ROOT.TFile("BsToKstmm_tree.root", 'UPDATE')
     tBsToKstmm = fBsToKstmm.Get("DecayTree")

     fBdToKstmm = ROOT.TFile("BdToKstmm_tree.root", 'UPDATE')
     tBdToKstmm = fBdToKstmm.Get("DecayTree")

     fBsToKstee = ROOT.TFile("BsToKstee_tree.root", 'UPDATE')
     tBsToKstee = fBsToKstee.Get("DecayTree")

     fBdToKstee = ROOT.TFile("BdToKstee_tree.root", 'UPDATE')
     tBdToKstee = fBdToKstee.Get("DecayTree")

     fBdToRhomm = ROOT.TFile("BdToRhomm_tree.root", 'UPDATE')
     tBdToRhomm = fBdToRhomm.Get("DecayTree")

     fBdToRhoee = ROOT.TFile("BdToRhoee_tree.root", 'UPDATE')
     tBdToRhoee = fBdToRhoee.Get("DecayTree")


     #Hallo little histograms
     BsKstmm_mass_hist = r.TH1F("BsKstmm_mass_hist", "BsKstmm_mass_hist", 100, 5100, 5700)
     BdKstmm_mass_hist = r.TH1F("BdKstmm_mass_hist", "BdKstmm_mass_hist", 100, 5100, 5700)
     BdRhomm_mass_hist = r.TH1F("BdRhomm_mass_hist", "BdRhomm_mass_hist", 100, 5100, 5700)

     BsKstee_mass_hist = r.TH1F("BsKstee_mass_hist", "BsKstee_mass_hist", 100, 4100, 5700)
     BdKstee_mass_hist = r.TH1F("BdKstee_mass_hist", "BdKstee_mass_hist", 100, 4100, 5700)
     BdRhoee_mass_hist = r.TH1F("BdRhoee_mass_hist", "BdRhoee_mass_hist", 100, 4100, 5700)



     #Hallo little plots
     #K* family with muons
     cMuons =  ROOT.TCanvas ("cMuons","cMuons",750,750)
     cMuons.cd()
     cMuons.SetLogy(1)
     BdKstmm_mass_hist.SetTitle("")
     BdKstmm_mass_hist.GetXaxis().SetTitle("m(K^{-}#pi^{+}#mu^{+}#mu^{-})[MeV/c^{2}]")
     BdKstmm_mass_hist.SetMarkerColor(17)
     BsKstmm_mass_hist.SetMarkerColor(9)
     tBdToKstmm.Draw("B_M*1000>>BdKstmm_mass_hist","","")
     tBsToKstmm.Draw("B_M*1000>>BsKstmm_mass_hist", "","SAME")
     BdKstmm_mass_hist.Scale(4157*1./BdKstmm_mass_hist.Integral())
     BsKstmm_mass_hist.Scale(38*1./BsKstmm_mass_hist.Integral())
     cMuons.SaveAs("plots/Kstmm.png")
     #K* family with electrons
     cElectrons =  ROOT.TCanvas ("cElectrons","cElectrons",750,750)
     cElectrons.cd()
     cElectrons.SetLogy(1)
     BdKstee_mass_hist.SetTitle("")
     BdKstee_mass_hist.GetXaxis().SetTitle("m(K^{-}#pi^{+}e^{+}e^{-})[MeV/c^{2}]")
     BdKstee_mass_hist.SetMarkerColor(17)
     BsKstee_mass_hist.SetMarkerColor(9)
     tBdToKstee.Draw("B_M*1000>>BdKstee_mass_hist", "","")
     tBsToKstee.Draw("B_M*1000>>BsKstee_mass_hist","","SAME")
     BdKstee_mass_hist.Scale(4157*1./BdKstee_mass_hist.Integral())
     BsKstee_mass_hist.Scale(38*1./BsKstee_mass_hist.Integral())
     cElectrons.SaveAs("plots/Kstee.png")




     #rho family with muons
     cMuonsRho =  ROOT.TCanvas ("cMuonsRho","cMuonsRho",750,750)
     cMuonsRho.cd()
     cMuonsRho.SetLogy(1)
     BdRhomm_mass_hist.SetTitle("")
     BdRhomm_mass_hist.GetXaxis().SetTitle("m(#pi^{-}#pi^{+}#mu^{+}#mu^{-})[MeV/c^{2}]")
     BdRhomm_mass_hist.SetMarkerColor(17)
     BdKstmm_mass_hist.SetMarkerColor(46)
     tBdToKstmm.Draw("B_M_K2pim*1000>>BdKstmm_mass_hist","","")
     tBdToRhomm.Draw("B_M*1000>>BdRhomm_mass_hist", "","SAME")
     BdKstmm_mass_hist.Scale(1./BdKstmm_mass_hist.Integral())
     BdRhomm_mass_hist.Scale(1./BdRhomm_mass_hist.Integral())
     cMuonsRho.SaveAs("plots/Rhomm.png")
     #rho family with electrons
     cElectronsRho =  ROOT.TCanvas ("cElectronsRho","cElectronsRho",750,750)
     cElectronsRho.cd()
     cElectronsRho.SetLogy(1)
     BdRhoee_mass_hist.SetTitle("")
     BdRhoee_mass_hist.GetXaxis().SetTitle("m(#pi^{-}#pi^{+}e^{+}e^{-})[MeV/c^{2}]")
     BdRhoee_mass_hist.SetMarkerColor(17)
     BdKstee_mass_hist.SetMarkerColor(46)
     tBdToKstee.Draw("B_M_K2pim*1000>>BdKstee_mass_hist","","")
     tBdToRhoee.Draw("B_M*1000>>BdRhoee_mass_hist", "","SAME")
     BdKstee_mass_hist.Scale(1./BdKstee_mass_hist.Integral())
     BdRhoee_mass_hist.Scale(1./BdRhoee_mass_hist.Integral())

     cElectronsRho.SaveAs("plots/Rhoee.png")
