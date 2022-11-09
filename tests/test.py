
import sys
sys.path.append(sys.path[0]+"/..")
from geoip import GeoIP

lookup = GeoIP('YOUR_EMAIL', 'YOUR_API_KEY')

testIPs = ['8.8.8.8', '2a01:e35:8bd9:8bb0:92b:8628:5ca5:5f2b']

results = []
for IP in testIPs:
	result = lookup.get(IP)
	results.append(result)

print(results)
