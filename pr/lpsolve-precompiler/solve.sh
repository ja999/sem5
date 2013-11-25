#!/bin/bash

mkdir -p out

for i in `ls params`; do
  cp params/$i params.txt;
  make && mv output out/$i.out;
done
