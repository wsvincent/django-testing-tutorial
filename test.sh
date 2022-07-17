coverage run manage.py test
coverage json -o coverage.json
actual_coverage=$(jq ".totals.percent_covered_display"  coverage.json | cut -d '"' -f 2)
if [ $actual_coverage -lt $RATE ]
then
echo "The acutual code coverge $actual_coverage is lower than expect coverage $RATE"
exit 1
fi
