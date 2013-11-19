all:
	cat params.txt first_seq.in > first_seq && ./precompiler.rb first_seq && cat first_seq.lp | lpsolve > first_seq.out
	cat params.txt second_seq.in > second_seq && ./precompiler.rb second_seq && cat second_seq.lp | lpsolve > second_seq.out
	cat params.txt third_seq.in > third_seq && ./precompiler.rb third_seq && cat third_seq.lp | lpsolve > third_seq.out
	cat params.txt first_seq.out second_seq.out third_seq.out > output
