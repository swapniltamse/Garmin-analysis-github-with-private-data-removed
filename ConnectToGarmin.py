from garminconnect import Garmin
import json
import datetime

# Replace with your Garmin credentials
GARMIN_EMAIL = "xxx@gmail.com"
GARMIN_PASSWORD = "yyyyy"

def get_heart_rate_data(days=7):
    try:
        # Authenticate with Garmin
        client = Garmin(GARMIN_EMAIL, GARMIN_PASSWORD)
        client.login()

        # Fetch heart rate data for the last N days
        heart_rate_data = []
        for i in range(days):
            date = (datetime.date.today() - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
            # Fetch HR for a specific day
            hr_data = client.get_heart_rates(date) 
            heart_rate_data.append({"date": date, "heart_rate": hr_data})

        with open("garmin_heart_rate.json", "w") as f:
            json.dump(heart_rate_data, f, indent=4)

        print("Heart rate data saved to garmin_heart_rate.json")
    
    except Exception as e:
        print(f"Error: {e}")

get_heart_rate_data()
