Use the precompiler to be able to define macros.
And it remembers about semi-colons at the end of the line SO YOU DON'T HAVE TO!
See example for more. To use

> make

you have to have

lpsolve

defined as the LPsolve executable.




All in all, just run 

> precompiler.rb filename

to get filename.lp



You can use makefile to generate output for all models and particular params.

Also, you can repeat it for all params with solve.sh.
To do that build this hierarchy:
\
 |-- makefile
 |-- solve.sh
 |-- precompiler
 |-- params
     \
      |-- 1
      |-- 2
      |-- dupa
      |-- czy
      |-- jak
      |-- chcesz
      |-- nazywac
      |-- kolejne
      ...
      |-- testy
  |-- model_1.in
  |-- model_2.in
  ...
  |-- model_n.in
  
Then you have to set your makefile correctly to use all models.


The example doesn't have correct paths. Beware.
