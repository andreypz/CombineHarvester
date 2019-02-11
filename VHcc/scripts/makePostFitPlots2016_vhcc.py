import os

CHN_DICT_SR = {
    "Wen": [["vhcc_Wen_1_13TeV2016","1-lepton (e)"]],
    "Wmn": [["vhcc_Wmn_1_13TeV2016","1-lepton (#mu)"]],
    "Zee": [["vhcc_Zee_1_13TeV2016","2-lepton (e), High p_{T} (V)"],["vhcc_Zee_2_13TeV2016","2-lepton (e), Low p_{T} (V)"]],
    "Zmm": [["vhcc_Zmm_1_13TeV2016","2-lepton (#mu), High p_{T} (V)"],["vhcc_Zmm_2_13TeV2016","2-lepton (#mu), Low p_{T} (V)"]],
    "Znn": [["vhcc_Znn_1_13TeV2016","0-lepton"]]
}



#for MODE in ['prefit','postfit']:
for MODE in ['prefit']:
    for CHN in ['Wen','Wmn','Zee','Zmm','Znn']:
        for i in range(0,len(CHN_DICT_SR[CHN])):
              LABEL = "%s" % CHN_DICT_SR[CHN][i][1]
              OUTNAME = "%s" % CHN_DICT_SR[CHN][i][0]
              os.system(('./scripts/postFitPlot_vhcc.py' \
                  ' --file=shapes_fullPreFit_WHfFix_LF1bHF7b.root --ratio --extra_pad=0.53 --file_dir=%(OUTNAME)s ' \
                  ' --ratio_range 0.4,1.6 --empty_bin_error --channel=%(CHN)s --blind --x_blind_min 1.0 --x_blind_max 1.0 --x_title BDT' \
                  ' --outname %(OUTNAME)s --mode %(MODE)s --log_y --custom_y_range --y_axis_min "5E-4" '\
                  ' --channel_label "%(LABEL)s"' % vars()))

