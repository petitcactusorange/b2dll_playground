// $Id: $
//File Edit Options Buffers Tools C++ Help
#include<iostream>
using namespace std;
#include "Math/Boost.h"
#include "Math/LorentzVector.h"
#include "TLorentzVector.h"

double planeangle( const TLorentzVector& vecCD,
                   const TLorentzVector& vecA,
                   const TLorentzVector& vecB,
                   const TLorentzVector& vecC,
                   const TLorentzVector& vecD )
{

  TVector3 dirA ;
  TVector3 dirB ;
  TVector3 dirC ;
  TVector3 dirD ;
  dirA       = vecA.Vect().Unit();
  dirB       = vecB.Vect().Unit();
  dirC       = vecC.Vect().Unit();
  dirD       = vecD.Vect().Unit();

  TVector3 ez ;
  ez      = vecCD.Vect().Unit();

  TVector3 el ;
  TVector3 ek ;

  el = ( dirA.Cross( dirB ) ).Unit();
  ek = ( dirC.Cross( dirD ) ).Unit();


  double cosphi = ( ek.Dot( el ) );
  double sinphi = ( el.Cross( ek ) ).Dot( ez );
  double phi    = acos( cosphi ) ;

  // Resolve ambiguity
  return ( sinphi > 0.0 ? phi : -phi );
}
void add_AngVarByHand(TString name)
{
  // les resultats ont ete verifies sur le MC K*ee avec le calcul 'officiel'
  TFile* newFile = new TFile(name, "UPDATE");
  TTree *newTree = (TTree*)newFile->Get("DecayTree");
  cout << "Number of events: " << newTree->GetEntries()<<endl ;  ;

  ULong64_t eventNumber;

  Double_t Kp_PX ;
  Double_t Kp_PY ;
  Double_t Kp_PZ ;
  Double_t Kp_PE ;
  Double_t Kp_P ;

  Double_t Km_PX ;
  Double_t Km_PY ;
  Double_t Km_PZ ;
  Double_t Km_PE ;
  Double_t Km_P ;

  Double_t L1_PX ;
  Double_t L1_PY ;
  Double_t L1_PZ ;
  Double_t L1_PE ;
  Double_t L1_P ;

  Double_t L2_PX ;
  Double_t L2_PY ;
  Double_t L2_PZ ;
  Double_t L2_PE ;
  Double_t L2_P ;

  Double_t Bs_P ;

  newTree->SetBranchAddress("Km_PX" ,&Km_PX) ;
  newTree->SetBranchAddress("Km_PY" ,&Km_PY) ;
  newTree->SetBranchAddress("Km_PZ" ,&Km_PZ) ;
  newTree->SetBranchAddress("Km_P" ,&Km_P) ;

  newTree->SetBranchAddress("Kp_PX" ,&Kp_PX) ;
  newTree->SetBranchAddress("Kp_PY" ,&Kp_PY) ;
  newTree->SetBranchAddress("Kp_PZ" ,&Kp_PZ) ;
  newTree->SetBranchAddress("Kp_P" ,&Kp_P) ;

  newTree->SetBranchAddress("L1_PX" ,&L1_PX) ;
  newTree->SetBranchAddress("L1_PY" ,&L1_PY) ;
  newTree->SetBranchAddress("L1_PZ" ,&L1_PZ) ;
  newTree->SetBranchAddress("L1_P" ,&L1_P) ;

  newTree->SetBranchAddress("L2_PX" ,&L2_PX) ;
  newTree->SetBranchAddress("L2_PY" ,&L2_PY) ;
  newTree->SetBranchAddress("L2_PZ" ,&L2_PZ) ;
  newTree->SetBranchAddress("L2_P" ,&L2_P) ;


  Int_t signumberOfEntries = newTree->GetEntries();

  float ctL = -999. ;
  float ctK = -999. ;
  float phi = -999. ;

  TBranch *newbranch1 = newTree->Branch("ctL",&ctL,"ctL/F");
//  TBranch *newbranch1 = newTree->Branch("ctL",&ctL);
  TBranch *newbranch2 = newTree->Branch("ctK",&ctK,"ctK/F");
  TBranch *newbranch3 = newTree->Branch("phi",&phi,"phi/F");

  TLorentzVector VB ;
  TLorentzVector VK1 ;
  TLorentzVector VK2 ;
  TLorentzVector VE1 ;
  TLorentzVector VE2 ;

  TLorentzVector vecA  ;
  TLorentzVector vecB ;
  TLorentzVector vecC ;
  TLorentzVector vecD ;
  TLorentzVector vecAB ;
  TLorentzVector vecCD ;
  TLorentzVector boostedA ;
  TLorentzVector boostedC ;
  TVector3 boostToAB ;
  TVector3 boostToCD ;
  TVector3 dirAB     ;
  TVector3 dirboostedA ;
  TVector3 dirCD   ;
  TVector3 dirboostedC ;
  TVector3 boostToMother ;

  Double_t mK = .4937 ;
  Double_t mE = .000511 ;

  for (Int_t loopie=0; loopie < signumberOfEntries; ++loopie)
    {
    newTree->GetEntry(loopie);
    Kp_PE = TMath::Sqrt(Kp_P*Kp_P+mK*mK);
    Km_PE = TMath::Sqrt(Km_P*Km_P+mK*mK);
    L1_PE = TMath::Sqrt(L1_P*L1_P+mE*mE);
    L2_PE = TMath::Sqrt(L2_P*L2_P+mE*mE);

    VK1.SetPxPyPzE( Kp_PX, Kp_PY, Kp_PZ, Kp_PE );
    VK2.SetPxPyPzE( Km_PX, Km_PY, Km_PZ, Km_PE );
    VE1.SetPxPyPzE( L1_PX, L1_PY, L1_PZ, L1_PE );
    VE2.SetPxPyPzE( L2_PX, L2_PY, L2_PZ, L2_PE );

    VB = VK1 + VK2 + VE1 + VE2 ;


    boostToMother = -VB.BoostVector();

    // Ici le premier est toujours le e+
    vecA.SetPxPyPzE( L1_PX, L1_PY, L1_PZ, L1_PE );
    vecB.SetPxPyPzE( L2_PX, L2_PY, L2_PZ, L2_PE );
    vecC.SetPxPyPzE( Kp_PX, Kp_PY, Kp_PZ, Kp_PE );
    vecD.SetPxPyPzE( Km_PX, Km_PY, Km_PZ, Km_PE );
    vecA.Boost(boostToMother) ;
    vecB.Boost(boostToMother) ;
    vecC.Boost(boostToMother) ;
    vecD.Boost(boostToMother) ;

    vecAB = vecA + vecB;
    vecCD = vecC + vecD;
    boostToAB = -vecAB.BoostVector();
    boostedA = vecA ;
    boostedA.Boost(boostToAB) ;


    dirAB       = vecAB.Vect().Unit();
    dirboostedA = boostedA.Vect().Unit();
    ctL = - dirboostedA.Dot( dirAB );

    boostToCD = -vecCD.BoostVector();

    boostedC  = vecC ;
    boostedC.Boost(boostToCD) ;
    dirCD       = vecCD.Vect().Unit();
    dirboostedC = boostedC.Vect().Unit();

    ctK =  dirboostedC.Dot( dirCD );

    phi = planeangle( vecCD, vecA, vecB, vecC, vecD );
    if (loopie < 10)
      {
        cout<<"loopie : "<<loopie<<endl ;
        cout<<"    boostToMother"<<boostToMother.Mag()<<endl ;
        cout<<"    vecA.Mag();"<<vecA.Mag()<<endl ; ;
        cout<<"    vecAB.Mag();"<<vecAB.Mag()<<endl ; ;
        cout<<"    boostToAB"<<boostToAB.Mag()<<endl ; ;
        cout<<"    boostedA.Mag();"<<boostedA.Mag()<<endl ; ;
        cout<<"    ctL = "<<ctL <<endl ;
        cout<<"    ctK = "<<ctK <<endl ;
        cout<<"    phi  = "<<phi<<endl ;

     }
    newbranch1->Fill();
    newbranch2->Fill();
    newbranch3->Fill();
  }
  newFile->Write();
  cout << "  new Number of events: " << newTree->GetEntries()<< endl ;


}
