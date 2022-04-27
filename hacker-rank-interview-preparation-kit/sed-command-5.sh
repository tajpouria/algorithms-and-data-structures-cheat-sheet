# https://www.hackerrank.com/challenges/sed-command-5/problem
sed -E "s/([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})/\4 \3 \2 \1/g"

