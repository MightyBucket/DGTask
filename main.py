import DHLtracker

# I have implemented the main task and extra task as two functions inside the DHLtracker module.
# In this example, I use the first function to get the most recent tracking event. The address of that event is used to find the closest DHL locations in that area.

key = "BxGGD8enqdMJGKUaOAUWjAsS7vKgpgw0"

tracking_number = "7777777770"
tracking_number2 = "4112889060"

event = DHLtracker.get_last_tracking_event(tracking_number, key)
print(event)

# Get locality and remove all spaces in it
locality = event["location"]["address"]["addressLocality"].replace(" ", "")
country_code = event["location"]["address"]["countryCode"]

radius = 1000

# Get the nearby pickup points from the address of the last tracking event
DHLtracker.get_nearby_pickup_points(country_code, locality, radius)
