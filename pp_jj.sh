#!/bin/sh

RUN=$1
pt=$2
PYTHIA8DATA=/home/yulee/generate/mg5/HEPTools/pythia8/share/Pythia8/xmldoc
export PYTHIA8DATA
echo "Running PP->JJ ${pt}"
NAME="temp_pp_jj_${pt}_${RUN}"
PROCESS="p p > j j"
# Could be "add process p p > mu+ mu- g g" for instance
ADDITIONAL_PROCESS=
# Could be "MG5/run_card_jj.dat" for instance. By default, only the CMS card is added
ADDITIONAL_CARDS="run_card_jj_${pt}.dat"

CMD="
define j = g u d s u~ d~ s~
define q = u d s u~ d~ s~
generate $PROCESS
$ADDITIONAL_PROCESS
output $NAME
launch
shower=PYTHIA8
detector=DELPHES
done
Cards/delphes_card_CMS.tcl
$ADDITIONAL_CARDS
"

echo "$CMD" | mg5/bin/mg5_aMC 
mv $NAME/Events/run_01/tag_1_delphes_events.root root/$NAME.root
rm -rf $NAME
