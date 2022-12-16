void mlk(){
    TTree *data = new TTree("mlk", "");
    data->ReadFile("Millikan.txt", "t/D");
    TH1D * h_mlk = new TH1D("h_mlk", "", 100, 0, 0);
    data->Draw("t >> h_mlk");


    TF1 *f = new TF1("f", "[3]*TMath::Gaus(x, [0], [2]) + [4]*TMath::Gaus(x, [0]+[1], [2])+[5] * TMath::Gaus(x, [0]+2*[1], [2])", 0, 6.15);
    f->SetParameters(2.,0.3,1.6);
    f->FixParameter(3,1);
    f->FixParameter(4,1);
    f->FixParameter(5,1);
    data->UnbinnedFit("f", "t");
}