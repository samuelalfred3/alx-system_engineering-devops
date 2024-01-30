#!/usr/bin/env ruby

if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <input_string>"
  exit 1
end

input_string = ARGV[0]
regex = /[A-Z]/
matches = input_string.scan(regex)
puts matches.join

