for f in /home/yulee/generate/root/temp_pp_jj_200_*;
  do
    a=`basename $f`
    a='gen'${a:4}
    echo "/home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/jettest ${f} /home/yulee/generate/genroot/${a}"
    /home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/jettest ${f} /home/yulee/generate/genroot/${a}
    #/home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/jetPF21 ${f} /home/yulee/generate/genroot/${a}
    #/home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/21QGJets $f /home/yulee/generate/genroot/${a}
    #/home/yulee/QGJets_10_5_0_pre1/bin/slc7_amd64_gcc700/threejet $f /home/yulee/generate/genroot/`basename $f`
  done
#python merge.py
