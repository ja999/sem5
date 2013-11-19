all:
	./precompiler.rb first_seq && cat first_seq.lp | lp_solve > first_seq.out
	./precompiler.rb second_seq && cat second_seq.lp | lp_solve > second_seq.out
	./precompiler.rb third_seq && cat third_seq.lp | lp_solve > third_seq.out
