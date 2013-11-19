#!/usr/bin/env ruby

def precompile input
  lines = input.split("\n").map(&:strip).reject(&:empty?)
  sep_pos = lines.index { |line| line =~ /^---/ }
  if sep_pos
    lines = swap_macros(lines, sep_pos)
  end
  lines.join("\n")
end

def swap_macros lines, sep_pos
  macros = parse_macros(lines.take(sep_pos))
  eqs = lines.last(lines.length - sep_pos - 1)

  if macros.any?
    # puts "BEGIN MACROS\n"
    # puts macros.map { |m| m.join '   is eq to   ' }.join("\n")
    # puts "END MACROS\n\n\n_____\n"

    macros.each do |m|
      eqs.map! do |eq|
        eq.gsub m[0], m[1]
      end
    end

    eqs.map! do |eq|
      simplify eq
    end
  end

  eqs
end

def parse_macros macros
  macros.map { |m| m.split('=').map(&:strip) }
end

def simplify eq
  sep = /[=<>]/
  sep_sign = eq.match(sep)
  sides = eq.split(sep)
  sides.map! do |side|
    chars = side.chars
    if (chars - chars.select { |char| calculable? char }).empty?
      eval(side)
    else
      side
    end

    side.gsub(/[0-9]+\s*[*]\s*[0-9]+/) { |m| " #{eval(m)} " }.gsub(/\s+/, ' ').strip()
  end
  res = sides.join(" #{sep_sign} ")
  l = sides.last
  if l && l[-1] != ';'
    res + ';'
  else
    res
  end
end

def calculable? char
  char =~ /[0-9*+\-\/ ]/
end

def multiplicable? char
  char =~ /[0-9 *]/
end


if ARGV.empty?
  puts 'Gimme some filename'
else
  ARGV.each do |f_name|
    File.open(f_name, 'r') do |f_in|
      input = f_in.read
      output = precompile(input)
      File.open(f_name + '.lp', 'w') { |f_out| f_out.write output }
    end
  end
end

