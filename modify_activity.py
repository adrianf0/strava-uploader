#!/usr/bin/env python

"""
    Small script to modify in batch the sport activity type for some imported activites
"""

from uploader import Setup, StravaClientUtils

Setup.set_up_env_vars()
Setup.set_up_logger()

client = StravaClientUtils.get_client()

# Fetch your activities (adjust limit as needed)
activities = client.get_activities(limit=1000)

for activity in activities:
    # Check if activity meets your criteria
    if activity.type == 'Ride' and activity.total_elevation_gain == 0:
        print(f"Updating Activity {activity.id}: {activity.name}")
        # Update activity type to 'Swim'
        client.update_activity(activity.id, sport_type='Swim')
        print(f"Activity {activity.id} updated to Swim.")

print("Batch update complete.")
