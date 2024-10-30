import http.client
import json

key = "BxGGD8enqdMJGKUaOAUWjAsS7vKgpgw0"
demo_key = "demo-key"

def get_last_tracking_event(tracking_number, api_key):
  # Connect to DHL API domain and make request to API endpoint
  conn = http.client.HTTPSConnection("api-eu.dhl.com")
  payload = ''
  headers = {
    'DHL-API-Key': api_key,
    'accept': 'application/json'
  }
  conn.request("GET", f"/track/shipments?trackingNumber={tracking_number}", payload, headers)

  # Parse response into JSON object
  res = conn.getresponse()
  data = res.read()
  result = json.loads(data.decode("utf-8"))

  # Get the list of shipping events inside the response
  shipping_events = result["shipments"][0]["events"]

  # Return the first (i.e most recent) event
  return shipping_events[0]


def get_nearby_pickup_points(country_code, city, radius=0):
  conn = http.client.HTTPSConnection("api.dhl.com")

  if radius == None or radius == "":
    radius = 0
  
  payload = ''
  headers = {
    'DHL-API-Key': key
  }
  conn.request("GET", f"/location-finder/v1/find-by-address?countryCode={country_code}&addressLocality={city}&radius={radius}", payload, headers)
  
  res = conn.getresponse()
  data = res.read()
  result = json.loads(data.decode("utf-8"))

  locations = result["locations"]

  print(f"There are {len(locations)} DHL locations near you")

  locationNames = [loc["name"] for loc in locations]
  
  for location in locationNames:
    print(location)