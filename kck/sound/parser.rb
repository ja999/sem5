#!/usr/bin/env ruby

def fire_all
  files = Dir.entries('train').select { |e| e =~ /wav/ }
  percentage = 0
  files.each do |f|
    file = "train/#{f}"
    output = %x(python wave.py #{file})
    result = $?.exitstatus
    percentage += result
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
