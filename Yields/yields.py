#--------------------------
#input PDG + LHCb + FCC
#--------------------------
BR_Bd2Kstmm =1.7e-7 #from MH notes  0.342e-7 * multiply by q2 range = (6-1.1) GeV2https://arxiv.org/pdf/1403.8044.pdf
BR_Bu2Kmm  = 24.2e-9 * 4.9  #https://arxiv.org/pdf/1403.8044.pdf * multiply by q2 range = (6-1.1) GeV2
KstarToKpi = 2./3.
K0ToKs = 1./2. * 0.68
VtdOverVtsSquared = 1./25
fsOverfdLHCb= 0.259 #from MH notes
#--------------------------
#input LHCb
#--------------------------
N_BdKstmm_4point7fb = 1200  #from MH notes   @ 4.7 fb-1 [1fb(7)+2fb(8)+1.7fb(13)]
N_BdKstmm_1fb_7TeV = 186

N_BuKmm_5fb = 1943   #from 1903.09252 @ 5 fb-1  [3fb(7,8)+ 2fb(13)]
N_BuKmm_1fb_7TeV = 272

N_BdKstmm_50fb =  N_BdKstmm_4point7fb  +  N_BdKstmm_1fb_7TeV  *  45.3 * 2  # 50fb = 3fb (7,8 TeV) + 47fb (13 TeV)
N_BuKmm_50fb   =  N_BuKmm_5fb    +  N_BuKmm_1fb_7TeV    *  45 * 2  # 50fb = 5fb (7,8,13 TeV) + 45fb (13 TeV)

N_BdKstmm_300fb =  N_BdKstmm_50fb + N_BdKstmm_1fb_7TeV * 250 * 2 # 300 fb = 50fb (above) + 250fb (13 TeV)
N_BuKmm_300fb   =  N_BuKmm_50fb   +  N_BuKmm_1fb_7TeV  * 250 * 2



#------------------------------
#We all love multiplications
#------------------------------
N_BsKstmm_50fb = VtdOverVtsSquared  * N_BdKstmm_50fb * fsOverfdLHCb
N_BdRhomm_50fb = VtdOverVtsSquared  * N_BdKstmm_50fb *  (1./KstarToKpi)

N_BsKstmm_300fb = VtdOverVtsSquared  * N_BdKstmm_300fb * fsOverfdLHCb
N_BdRhomm_300fb = VtdOverVtsSquared  * N_BdKstmm_300fb * (1./KstarToKpi)
#---
N_BuPimm_50fb =  VtdOverVtsSquared  * N_BuKmm_50fb
N_BsKsmm_50fb  = VtdOverVtsSquared  * N_BuKmm_50fb * fsOverfdLHCb *  K0ToKs

N_BuPimm_300fb =  VtdOverVtsSquared * N_BuKmm_300fb
N_BsKsmm_300fb  = VtdOverVtsSquared * N_BuKmm_300fb * fsOverfdLHCb *  K0ToKs

#----------------
#input for FCC
#----------------
NumberOfZ = 5e12 #from EU when we the EuroBillion
ZTobb = 0.1512   # from MH notes
fdFCC = 0.408    # HFLAV
fuFCC = 0.408    #  HFLAV
fsOverfdFCC = 0.246  #HFLAV
fsOverfuFCC = 0.246  #HFLAV

#----------------
#FCC
N_BdKstmm_FCCee =  NumberOfZ * 2 * ZTobb * fdFCC * BR_Bd2Kstmm *  KstarToKpi
N_BsKstmm_FCCee =  N_BdKstmm_FCCee * fsOverfdFCC * VtdOverVtsSquared
N_BdRhomm_FCCee =  N_BdKstmm_FCCee * VtdOverVtsSquared  * (1./KstarToKpi)

N_BuKmm_FCCee  =   NumberOfZ * 2 * ZTobb * fuFCC * BR_Bu2Kmm
N_BuPimm_FCCee =   N_BuKmm_FCCee * VtdOverVtsSquared
N_BsKsmm_FCCee =   N_BuKmm_FCCee * fsOverfuFCC * VtdOverVtsSquared *  K0ToKs

print ("---------------------------")
print ("Yields @ LHCb  50 fb-1")
print ("---------------------------")
print("Number of BdKstmm at LHCb 50 fb  = {} ".format(int(N_BdKstmm_50fb)))
print("Number of BdRhomm at LHCb 50 fb  = {} ".format(int(N_BdRhomm_50fb)))
print("Number of BsKstmm at LHCb 50 fb  = {} ".format(int(N_BsKstmm_50fb)))
print("-----")
print("Number of BuKmm   at LHCb 50 fb  = {} ".format(int(N_BuKmm_50fb)))
print("Number of BuPimm  at LHCb 50 fb  = {} ".format(int(N_BuPimm_50fb)))
print("Number of BsKsmm  at LHCb 50 fb  = {} ".format(int(N_BsKsmm_50fb)))
print ("---------------------------")
print ("Yields @ LHCb  300 fb-1")
print ("---------------------------")
print("Number of BdKstmm at LHCb 300 fb  = {} ".format(int(N_BdKstmm_300fb)))
print("Number of BdRhomm at LHCb 300 fb  = {} ".format(int(N_BdRhomm_300fb)))
print("Number of BsKstmm at LHCb 300 fb  = {} ".format(int(N_BsKstmm_300fb)))
print("-----")
print("Number of BuKmm   at LHCb 300 fb  = {} ".format(int(N_BuKmm_300fb)))
print("Number of BuPimm  at LHCb 300 fb  = {} ".format(int(N_BuPimm_300fb)))
print("Number of BsKsmm  at LHCb 300 fb  = {} ".format(int(N_BsKsmm_300fb)))

print ("---------------------------")
print ("Yields @ FCC  5x10^12 Z0")
print ("---------------------------")
print("Number of BdKstmm at FCC = {} ".format(int(N_BdKstmm_FCCee)))
print("Number of BdRhomm at FCC = {} ".format(int(N_BdRhomm_FCCee)))
print("Number of BsKstmm at FCC = {} ".format(int(N_BsKstmm_FCCee)))
print("-----")
print("Number of BuKmm   at FCC = {} ".format(int(N_BuKmm_FCCee)))
print("Number of BuPimm  at FCC = {} ".format(int(N_BuPimm_FCCee)))
print("Number of BsKsmm  at FCC = {} ".format(int(N_BsKsmm_FCCee)))
