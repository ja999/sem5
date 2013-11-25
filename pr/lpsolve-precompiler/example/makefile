PARAMS=params.txt
PRECOMPILER=../precompiler.rb
SOLVER=lp_solve
OUTPUT=output

all:
	cat $(PARAMS) first_seq.in > first_seq && $(PRECOMPILER) first_seq && cat first_seq.lp | $(SOLVER) > first_seq.out
	cat $(PARAMS) second_seq.in > second_seq && $(PRECOMPILER) second_seq && cat second_seq.lp | $(SOLVER) > second_seq.out
	cat $(PARAMS) third_seq.in > third_seq && $(PRECOMPILER) third_seq && cat third_seq.lp | $(SOLVER) > third_seq.out
	cat $(PARAMS) > $(OUTPUT)
	echo "\n\n\n############################\n### First Model\n" >> $(OUTPUT)
	cat first_seq.out >> $(OUTPUT)
	echo "\n\n\n############################\n### Second Model\n" >> $(OUTPUT)
	cat second_seq.out >> $(OUTPUT)
	echo "\n\n\n############################\n### Third Model\n" >> $(OUTPUT)
	cat third_seq.out  >> $(OUTPUT)

