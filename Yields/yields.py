


#--------------------
#input LHCb
#--------------------
N_BdKstmm_3fb = 1200 #LHCb
VtdOverVtsSquared = 1./25
fsOverfdLHCb= 0.259
BR_Bd2Kstmm =1.7e-7
#----------------
#input for FCC
#----------------
NumberOfZ = 5e12
ZTobb=0.1512
fdFCC = 0.408
fsOverfdFCC = 0.249
fsFCC = fsOverfdFCC* fdFCC
#----------------#----------------
#Scale To Lumi 50 fb-1 / 300 fb-1
#----------------#----------------
Scale_50fb = 15.6
Scale_300fb = 95.

N_BsKstmm_3fb = VtdOverVtsSquared  * N_BdKstmm_3fb * fsOverfdLHCb
N_BdRhomm_3fb = VtdOverVtsSquared  * N_BdKstmm_3fb * (3./2.)


#Scale To Lumi 50 fb-1
N_BdKstmm_50fb = Scale_50fb * N_BdKstmm_3fb
N_BsKstmm_50fb = Scale_50fb * N_BsKstmm_3fb
N_BdRhomm_50fb = Scale_50fb * N_BdRhomm_3fb
#Scale To Lumi 300 fb-1
N_BdKstmm_300fb = Scale_300fb * N_BdKstmm_3fb
N_BsKstmm_300fb = Scale_300fb * N_BsKstmm_3fb
N_BdRhomm_300fb = Scale_300fb * N_BdRhomm_3fb



N_BdKstmmFCCee =  NumberOfZ * 2 * ZTobb * fdFCC * BR_Bd2Kstmm *  (2./3.)

N_BsKstmmFCCee =  N_BdKstmmFCCee * fsOverfdFCC * VtdOverVtsSquared

N_BdRhommFCCee =  N_BdKstmmFCCee * VtdOverVtsSquared  * (3./2.)

print ("---------------------------")
print ("Yields @ LHCb  50 fb-1")
print ("---------------------------")
print("Number of BdKstmm at LHCb 50 fb  = {} ".format(int(N_BdKstmm_50fb)))
print("Number of BsKstmm at LHCb 50 fb  = {} ".format(int(N_BsKstmm_50fb)))
print("Number of BdRhomm at LHCb 50 fb  = {} ".format(int(N_BdRhomm_50fb)))
print ("---------------------------")
print ("Yields @ LHCb  300 fb-1")
print ("---------------------------")
print("Number of BdKstmm at LHCb 300 fb  = {} ".format(int(N_BdKstmm_300fb)))
print("Number of BsKstmm at LHCb 300 fb  = {} ".format(int(N_BsKstmm_300fb)))
print("Number of BdRhomm at LHCb 300 fb  = {} ".format(int(N_BdRhomm_300fb)))

print ("---------------------------")
print ("Yields @ FCC  50 fb-1")
print ("---------------------------")
print("Number of BdKstmm at FCC = {} ".format(int(N_BdKstmmFCCee)))
print("Number of BsKstmm at FCC = {} ".format(int(N_BsKstmmFCCee)))
print("Number of BdRhomm at FCC = {} ".format(int(N_BdRhommFCCee)))
