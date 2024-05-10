#!/usr/bin/env ruby

# Check if the argument matches a 10-digit phone number
if ARGV[0] =~ /^\d{10}$/
  puts ARGV[0]
end
