#./mg5_pp_zq-nocr.sh 1
#./mg5_pp_qq-nocr.sh 1
#for i in {10..11} ;
#do
#  echo $i
#  ./mg5_pp_zq-nocr.sh $i
#done
#
#for i in {2..3} ;
#do
#  echo $i
#  ./mg5_pp_qq-nocr.sh $i
#done
for i in { 0..20 } ;
do
  echo $i
  ./pp_jj.sh $i 500
done
