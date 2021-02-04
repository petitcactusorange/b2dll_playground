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
gROOT.ProcessLine(".x lhcbStyle.C")

gStyle.SetOptStat("")
ROOT.gSystem.Load("libMathMore") #to get Legendre

from math import pow


if __name__ == '__main__':

     fBsToKstmm = ROOT.TFile("BsToKstmm_tree.root", 'UPDATE')
     tBsToKstmm = fBsToKstmm.Get("DecayTree")

     fBdToKstmm = ROOT.TFile("BdToKstmm_tree.root", 'UPDATE')
     tBdToKstmm = fBdToKstmm.Get("DecayTree")

     fBsToKstee = ROOT.TFile("BsToKstee_tree.root", 'UPDATE')
     tBsToKstee = fBsToKstee.Get("DecayTree")

     fBdToKstee = ROOT.TFile("BdToKstee_tree.root", 'UPDATE')
     tBdToKstee = fBdToKstee.Get("DecayTree")



     BsKstmm_mass_hist = r.TH1F("BsKstmm_mass_hist", "BsKstmm_mass_hist", 100, 5100, 5700)
     BdKstmm_mass_hist = r.TH1F("BdKstmm_mass_hist", "BdKstmm_mass_hist", 100, 5100, 5700)
     BsKstee_mass_hist = r.TH1F("BsKstee_mass_hist", "BsKstee_mass_hist", 100, 4100, 5700)
     BdKstee_mass_hist = r.TH1F("BdKstee_mass_hist", "BdKstee_mass_hist", 100, 4100, 5700)


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

     cMuons.SaveAs("Kstmm.png")

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
     cElectrons.SaveAs("Kstee.png")
