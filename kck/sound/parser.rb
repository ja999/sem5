#!/usr/bin/env ruby
require 'peach'

def fire_all
  files = Dir.entries('train').select { |e| e =~ /wav/ }
  percentage = 0
  files.peach(4) do |f|
    file = "train/#{f}"
    output = %x(python -W ignore wave.py #{file})
    result = $?.exitstatus
    # percentage += result - 2
    if result >= 2
      percentage += result - 2
    end
    puts "#{result} #{file}"
    # puts output
  end
  percentage = percentage * 100.0 / files.size
  puts percentage
end

if ARGV.empty?
  puts 'Gimme an option...'
else
  ARGV.each do |opt|
    if opt == 'all'
      fire_all
    end

    if opt == 'rand'
      puts 'chuj :D'
    end
  end
end
