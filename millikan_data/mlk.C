void mlk(){
    TTree *data = new TTree("mlk", "");
    data->ReadFile("Millikan.txt", "t/D");
    TH1D * h_mlk = new TH1D("h_mlk", "", 100, 0, 0);
    data->Draw("t >> h_mlk");


    TF1 *f = new TF1("f", "[2]*TMath::Gaus(x, [0], [1]) + [3]*TMath::Gaus(x, 2*[0], [1])+(1-[2]-[3])*TMath::Gaus(x, 3*[0], [1])");
    f->SetParameters(1.6,0.3, 0.3, 0.3);
    f->SetParLimits(0, 1.5, 1.7);
    f->SetParLimits(1, 0, 0.5);
    f->SetParLimits(2, 0, 1);
    f->SetParLimits(3, 0, 1);
    data->UnbinnedFit("f", "t", "t<5.8");
}
