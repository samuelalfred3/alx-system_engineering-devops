#!/usr/bin/env ruby

def extract_info(log_entry)
  regex = /\[from:(.+?)\] \[to:(.+?)\] \[flags:(.+?)\]/
  match_data = log_entry.match(regex)
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    "#{sender},#{receiver},#{flags}"
  else
    "Invalid log entry format"
  end
end

log_entries = File.read('log.txt').split("\n")

log_entries.each do |log_entry|
  puts extract_info(log_entry)
end

