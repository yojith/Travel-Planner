from datetime import datetime, timedelta
import os.path
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# If modifying these SCOPES, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/calendar.events"]


def calendar_event(schedule, date):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("oauth-creds.json", SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    service = build("calendar", "v3", credentials=creds)

    for event in schedule:
        try:
            date_time_format = "%Y-%m-%d %I:%M %p"
            new_date_time_format = "%Y-%m-%dT%H:%M:%S"
            start_time = datetime.strptime(f"{date} {event['time']}", date_time_format)
            end_time = start_time + timedelta(hours=1)
            start_time = start_time.strftime(new_date_time_format)
            end_time = end_time.strftime(new_date_time_format)
            event = {
                "summary": event["location"],
                "location": event["location"],
                "description": f"Website: {event["website"]}",
                "start": {
                    "dateTime": f"{start_time}-07:00",
                    "timeZone": "America/Los_Angeles",
                },
                "end": {
                    "dateTime": f"{end_time}-07:00",
                    "timeZone": "America/Los_Angeles",
                },
                "attendees": [],
                "reminders": {"useDefault": True},
            }
            # event = {
            #     "summary": "Sample Event",
            #     "location": "800 Howard St., San Francisco, CA 94103",
            #     "description": "A chance to hear more about Google Calendar API.",
            #     "start": {
            #         "dateTime": "2024-08-10T09:00:00-07:00",
            #         "timeZone": "America/Los_Angeles",
            #     },
            #     "end": {
            #         "dateTime": "2024-08-10T17:00:00-07:00",
            #         "timeZone": "America/Los_Angeles",
            #     },
            #     "attendees": [],
            #     "reminders": {
            #         "useDefault": False,
            #         "overrides": [
            #             {"method": "email", "minutes": 24 * 60},
            #             {"method": "popup", "minutes": 10},
            #         ],
            #     },
            # }

            event = service.events().insert(calendarId="primary", body=event).execute()
            print("Event created: %s" % (event.get("htmlLink")))

        except Exception as e:
            print(f"An error occurred: {e}")

        # Define the event

        # Call the Calendar API to create the event


if __name__ == "__main__":
    pass
    # main()
