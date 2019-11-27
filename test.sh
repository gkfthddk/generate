cd analysis
rm /home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/jettest
scram b -j8
cd ..
/home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/jettest root/temp_pp_jj_500_10.root /home/yulee/generate/genroot/gentest.root
