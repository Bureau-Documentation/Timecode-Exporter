#!/bin/bash

# Clear
clear

# Use the first argument passed (the dropped file)
input_file="$1"

# Check if the dropped file exists
if [ ! -f "$input_file" ]; then
    echo "File not found: $input_file"
    exit 1
fi

echo ""
echo ""

# Extract the desired time range and format it
time_ranges=$(awk '{
    if ($1 ~ /^[0-9]+$/) {  # Check if the first column is a number
        start_time = substr($5, 1, 8);  # Extract start time from column 5
        end_time = substr($6, 1, 8);    # Extract end time from column 6
        print start_time " to " end_time;  # Print in the desired format
    }
}' "$input_file")

# Format time ranges for clipboard (with two blank lines between)
formatted_time_ranges=$(echo "$time_ranges" | awk '{print $0 "\n\n"}')

# Copy the time ranges to clipboard
echo -e "$formatted_time_ranges" | pbcopy

# Display the copied time ranges in a dialog
osascript -e "display dialog \"Timecodes:\n\n$time_ranges\n\nThe timecodes are copied to your clipboard!\" buttons {\"OK\"} default button \"OK\""
