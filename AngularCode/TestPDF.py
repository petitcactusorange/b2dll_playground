import ROOT as r
from ROOT import RooFit as rf
from ROOT import RooRealVar as RRV
from ROOT import RooFormulaVar as RFV
from ROOT import RooArgList as RAL
from ROOT import RooDataSet as RDS
from math import pi
import math
import pickle
import yaml

import os
REPOSYS = os.environ['REPOSYS']
PLOTSPATH = os.environ['PLOTSPATH']
import sys
sys.path.insert(0, REPOSYS+"/analysis")
figdir = PLOTSPATH
accdir = PLOTSPATH + '/acceptance/'

#loading relevant PDFs

r.gSystem.Load('./dGammaoverdctLSigPdf_cxx.so')
from ROOT import dGammaoverdctLSigPdf as dG


#Init parser arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--config', type=str, help='Global config file')
parser.add_argument('-b', '--bash', action='store_true', help='bash mode')
parser.add_argument('--Acceptance', type=str, default='no', help='use the acceptance')

args = parser.parse_args()

if ( args.bash ):
    r.gROOT.SetBatch(True)
# load config file (where physics parameters will be read)
with open(args.config) as f:
    c = yaml.safe_load(f)

nToys = c['nsamples']

nEvts=1000

theFittedParams = ['bCoeff', 'cCoeff']

### Book histograms for storing the toys results
histo_Fit = {}
histo_Err = {}
histo_Pull = {}

for par, limits in c['fitranges'].items():
    if par in theFittedParams :
        histo_Fit[par]= r.TH1D( f'h_{par}_fit', f'h_{par}_fit', 100, limits[1], limits[2])
        histo_Err[par]= r.TH1D( f'h_{par}_err', f'h_{par}_err', 100, 0., (limits[2]-limits[1])*.02 )
        histo_Pull[par]= r.TH1D( f'h_{par}_pull', f'h_{par}_pull', 100, -5., 5. )

accvars = { 'c1L', 'c2L', 'c4L'}


#-----------------------------------------------------------------------------------------------------
# we are fitting only even functions on the acceptances .. while the angular PDF code is more general
c1L = RRV("c1L","c1L",0.,-1.,1.)
c1L.setConstant()

c2L = RRV("c2L","c2L",0.,-1.,1.)
c2L.setConstant()

c4L = RRV("c4L","c4L",0.,-1.,1.)
c4L.setConstant()


#-----------------------------------------------------------------------------------------------------
# May be one day we want to have tighter ctL region
ctLMin = -1.
ctLMax = +1.

ctL = RRV("ctL","cos(#theta_{l})",0.,ctLMin,ctLMax)
obsDict = {}
obsDict['ctL'] = ctL
obsArgSet = r.RooArgSet(*obsDict.values())


wToFit = r.RooWorkspace("wToFit","wToFit")

# Load the acceptance parameters

getattr(wToFit, 'import')(r.RooArgSet(c1L), rf.Silence())
getattr(wToFit, 'import')(r.RooArgSet(c2L), rf.Silence())
getattr(wToFit, 'import')(r.RooArgSet(c4L), rf.Silence())

effParam = {}
for p in accvars:
    effParam[p] = wToFit.var(p)

# the full list of parameters
fitparnames = ['bCoeff', 'cCoeff']
fitpars = {
    'std': ['bCoeff', 'cCoeff']
}

angParamP = {}
for par, val in c['generate'].items():
    angParamP[par] = RRV(par, par, 0, -2., 2.)
    angParamP[par].setConstant()
    angParamP[par].setVal(val)

# store the values used for generating
theGenVal = {}
theGenVal['bCoeff'] =  angParamP['bCoeff'].getVal()
theGenVal['cCoeff'] =  angParamP['cCoeff'].getVal()

angp = {}
for par in fitpars['std']:
    angp[par] = RRV(par, par, 0., -1., 1.)
    getattr(wToFit, 'import')(angp[par], rf.Silence())


angPDFToGen = dG.dGammaoverdctLSigPdf('angPDFToGen','angPDFToGen',*obsDict.values(),*angParamP.values(),*effParam.values())

angPDF = dG.dGammaoverdctLSigPdf('angPDF','angPDF',*obsDict.values(),*angp.values(),*effParam.values())


getattr(wToFit, 'import')(r.RooArgSet(angPDF), rf.Silence())


for itoy in range(0,nToys):
    print(f'iToy= {itoy}')

    dataOrig = angPDFToGen.generate(obsArgSet,nEvts)

    dataOrig.Print('v')

    ##fitting
    fitRes = angPDF.fitTo(dataOrig, rf.Minos(r.kFALSE), rf.Save(r.kTRUE), rf.Strategy(2), rf.PrintLevel(0), rf.SumW2Error(r.kTRUE))

    for v in theFittedParams :
#        print(v)
        val = fitRes.floatParsFinal().find(v).getVal()
        err = fitRes.floatParsFinal().find(v).getError()
        gen = theGenVal[v]
#        print(f'val= {val} err= {err} gen = {gen}')
        histo_Fit[v].Fill(val)
        histo_Err[v].Fill(err)
        if err > 0 :
            histo_Pull[v].Fill((val-theGenVal[v])/err)

# output for only one toy
    if itoy ==0 :
        fitRes.Print()
        outfile = figdir+f'B2PSll_toy_noCuts.pkl'
        with open(outfile, 'wb') as output:
            pickle.dump(fitRes, output)
        for key in obsDict:
            canv1 = r.TCanvas('canv', 'canv', 400, 275)
            obsFrame = obsDict[key].frame(40)
            dataOrig.plotOn(obsFrame, rf.MarkerSize(0.5))
            angPDF.plotOn(obsFrame)
            obsFrame.Draw()
            obsFrame.SetTitle('')
            canv1.SaveAs(figdir + f'AngFit_B2PSll_noCuts_{key}.pdf')

########## End of loop for toy iToy #####################
r.gStyle.SetOptFit(1)
for v in theFittedParams :
    c = r.TCanvas()
    c.Divide(2,2)
    c.cd(1)
    histo_Fit[v].Draw()
    c.cd(2)
    histo_Err[v].Draw()
    c.cd(3)
    histo_Pull[v].Fit('gaus', 'LM', 'E1')

    histo_Pull[v].Draw()
    c.cd(4)
    c.SaveAs(figdir + f'AngFit__B2PSll_Toys_{v}.pdf')
