
import sys
sys.path.append(sys.path[0]+"/..")
from geoip import GeoIP

lookup = GeoIP('i@surfy.one', '3b8797ae-569c-4e19-b101-6b248d18e462')

testIPs = ['8.8.8.8', '2a01:e35:8bd9:8bb0:92b:8628:5ca5:5f2b']

results = []
for IP in testIPs:
	result = lookup.get(IP)
	results.append(result)

print(results)
