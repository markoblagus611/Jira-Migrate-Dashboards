import requests
import json
from requests.auth import HTTPBasicAuth
import auth

# # Define the URL to retrieve dashboards from your Jira site.
basic_url_cloud = "https://your-site.atlassian.net/rest/api/3/dashboard"

# Define headers for HTTP requests with and without content.
headers_with_content = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

headers_without_content = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

# Set up basic authentication using your email and API token.
basic_auth = HTTPBasicAuth("<your-email>", "<your-api-token>")


# Define the name of the dashboard you want to migrate.
dashboard_name = "Test dashboard"

# Define edit and share permission types for the dashboard you want to migrate.
dashboard_edit_permission_type = "authenticated"
dashboard_share_permission_type = "project"

# Specify the project ID of the dashboard.
dashboard_project_id = "10000"

# Define the name of the gadget you want to migrate.
gadget_name = "Test gadget"

# Define the configuration for a gadget to migrate from Data Center to cloud.
payload2 = json.dumps({
                        "id": "IwEQHAwg7ALEA",
                        "title": "Q",
                        "titleType": "MICQggSgKkA",
                        "searchType": "FIRQMkA",
                        "aggregations": "NobwRALgngDgpmAXGAwgeQKoDkAqYA0YAhgOYkBOcJREcAQlEmAJIDKrGAoq2AL4C6QA",
                        "query": "A4Jw9gVgpgxgLgAgLwIEQGUYgK4FsEAK408qQA",
                        "customColumns": "NoXSA",
                        "displayOptions": "N4IgzgFg9g7gQlATgEwKaJALgGYEMA2YqANONDACq4BG+qACugMaoB2ALmFu4gK4llYVWqgCSYMPy6Ye-UpFgAtdFABqBfgBkaqQljyEBCylHYEAwlF4dufI+QqmLUfLwC2rW3MEwA4oisABzgATy97WE1UAHM2ZHD5cgANAEEADwBLMG1qXQSfAE10rJy8mTtEoSgXdgzAgHlWOFxEAAkoADd0fNxedigAJVRsRFRIfQIiUgJ8WHrA2qhWMABZNl4e-FmYAFE0wKR2fONi7Ji4y2sj8u8TzLPY1mRGRBYbHEmBJggW9goQwKoLAgeiiHYgUiA15sdgAESygXwuDCmBAqhSmgAquDpvcAMrkF5va4GKY+ZQBIkw0p6D6GSHMGHwsCI5EUDJ0YHorE7AD69B2A3MOwAchQISAocTmayQvQMkDUdzsfzBcKxRKpUyEUiQqcuRiVQKhaLxaQmAQmLwkewGIyOLhYvVsMCKPUKBiJXRHs8oGAMotPKiUn0oF7zk9tCErNcQCH+hLauw6Cl8Bloqw3DDgeqKIKJWgwExEHVA-Q-QGMktgQh2P03BLjJiiIhRG4oWAlrhA-kmGmmABrCgQAK8aIQfLeuIDSIZNwBrAAVlItTo5h+iHYoltbjALxnMCXpD193Xv1aqHTEHYmjnC8wACYAGwABkqMFhY2LparQdkERgGlpH-d8RXcXJEEsVwPGOchxEkVB-kBCZ6RAVhwPQfwggyVhomBEV6l5XwBnqTFQRFXwJXQtwIPoUYmCyX8sAARgZaEHViOjUAY-1q0wViQEdaJRmibtf3ZLNMVYe8QFaUiBjxCUhJEsSlgk1B2l4RABlUrAAA5zXca0xK6RwzHwFCyWQFoBxWKA0EsgDHBqOpGhFXAs3aLoMDpMljEsGicNQZAACkAEcLN8gQTyyKSZMuGxSGs20ADEkDcbtgVhFICl5FLRAUiheTxOSBjNHx2hLAAvJZzNvVgxkc99VHQWoLXwLz0HqxUQJ8bqz03SxWAaphalw7rgIqEBkCyGg6FaAF0DTVgB2kUlUAAXyAA",
                        "series1": "N4IgxgFghgTgLgIQJ4EkAmIBcIAOMCWA9gXEiADQgDOApgOYC2NAdnFQMKHMBm+dArjChwizLKABuAfQASfCOJD5maGgA8sABkq1GLNlgDaofBmzS5dBZQlQANvxpYQl6yGZQmz1xSVguAKowds4QcHA4mAD0UXaEYPYQhFRwmAAcmhlR+AxQdDRU2f7MhXhEJPgFURDyAHRUEnQgAL4AupT+cTDOAMQARtwATABsmpq+EvhU+H12TphwMI7NNlIAMoQA7orKqhqYAIw69EysVEYmZiDSG9s29o7Ot74eXtjPlPjFQSHYYRHRWLxRLJVIZLI5PJVL5cUoEYj4ERVOKbeqNFrtcCELq9AAsAHY+mA0lAJlMZnMsItlqsALI0ND4fgMHYqdRYQbHPRnC5KK7SemM5kTB7zECCpksyivMUS4Wfb7BULhSIxOIJOxJFLpTKabK5fKFGElKJlBFIwpMIUMNFNNodbHEXrcbhpPpjMnTWbzak0FbXdZbApwVl7LAAZi5pwMmGMfOcNyDKRFDjFt2DL08aaTIYVgSVfxVgPVIO14L1kMNRVhpvhFWROdtGIdOOwPW4ND6wxGnopPqWftWrgzmBMbP2uKj+nOscuCdk8gz91T3kXyelWdXViXfnzvxA-1VQI1WrBuv1UKNxTh5URlUKNW3KSb9qxrZAPVxmnDgwAnLje29KkB2af1cjgSAAGUswAMUqOw0Bnbh7FoSg6BgQh+BwdgoCoBJVDgmgEKQlCaEofhaE4LoZ19ShiFUAhmCabBVDwlhGSY3wqCSTYAC0aAwzh+B5TBkLsVC32IDYwAAaywMTaGaIA",
                        "jiraFields": "NobwRAlgJmBcYAcBOED2KAuBPMAaMAdgIYC2ApnGAAoroTZ5gDGANkQK4DOZAcqRfGRpMOfKw7cAkjEG0RjTkwAWZEkTjhsCAYjn1RYTlk4ZVlIXQYBfKwF0gA",
                        "version": "1"
                    })

# Initialize a boolean variable to track whether the dashboard and gadget exist.
dashboard_updated = False

# Set the maximum number of results per API call to 50.
query = {
    "maxResults": 50
}

# Retrieve the total number of dashboards.
dashboards_response = requests.request(
    "GET",
    basic_url_cloud,
    headers=headers_without_content,
    auth=auth,
    params=query
)

# Parse the JSON response to extract data about dashboards.
data = json.loads(dashboards_response.text)

# Store the total number of dashboards in a variable.
total_dashboards = data["total"]

# Initialize the start index for pagination.
start_at = 0

# Loop through all dashboards, retrieving 50 at a time.
while start_at < total_dashboards + 50:

    # Set parameters for the API call to retrieve 50 dashboards.
    query = {
        "maxResults": 50,
        "startAt": start_at
    }

    # Retrieve 50 dashboards.
    dashboards_response = requests.request(
        "GET",
        basic_url_cloud,
        headers=headers_without_content,
        auth=auth,
        params=query
    )

    # Parse the JSON response to extract data about dashboards.
    data = json.loads(dashboards_response.text)

    # Loop through the retrieved dashboards.
    for dashboard in data["dashboards"]:

        # Check if the current dashboard matches the one you want to migrate.
        if dashboard["name"] == dashboard_name:

            # Define the URL to retrieve all gadgets from that dashboard.
            get_dashboard_gadgets_url = basic_url_cloud + "/" + dashboard["id"] + "/gadget"

            # Retrieve all gadgets from that dashboard.
            dashboard_gadgets_response = requests.request(
                "GET",
                get_dashboard_gadgets_url,
                headers=headers_without_content,
                auth=auth
            )

            # Parse the JSON response to extract data about gadgets.
            data = json.loads(dashboard_gadgets_response.text)

            # Loop through all dashboard gadgets.
            for gadget in data["gadgets"]:

                # Check if the current gadget matches the one you want to migrate.
                if gadget["title"] == gadget_name:

                    # Define the URL to update the dashboard gadget.
                    get_dashboard_gadgets_url = "https://mobsite.atlassian.net/rest/api/2/dashboard/" + str(dashboard["id"]) + "/items/" + str(
                        gadget["id"]) + "/properties/params?_r=1695727815847"

                    # Update the dashboard gadget with the specified configuration.
                    gadget_update_response = requests.request(
                        "PUT",
                        get_dashboard_gadgets_url,
                        data=payload2,
                        headers=headers_with_content,
                        auth=auth
                    )

                    # Set the 'dashboard_updated' variable to True, indicating that no new dashboard needs to be created.
                    dashboard_updated = True

    # Increment the start index by 50 to retrieve the next set of dashboards.
    start_at += 50


# Create a new dashboard and gadget in the cloud.
def create_new_dashboard_and_gadget_cloud():

    payload_dashboard = json.dumps({
        "editPermissions": [
            {
                "type": dashboard_edit_permission_type
            }
        ],
        "name": dashboard_name,
        "sharePermissions": [
            {
                "type": dashboard_share_permission_type,
                "project": {
                    "id": dashboard_project_id
                }
            }
        ]
    })

    response_dashboard = requests.request(
        "POST",
        basic_url_cloud,
        data=payload_dashboard,
        headers=headers_with_content,
        auth=auth
    )

    data_dashboard = json.loads(response_dashboard.text)

    dashboard_id = data_dashboard["id"]

    gadget_url = basic_url_cloud + "/" + dashboard_id + "/gadget"

    payload_gadget = json.dumps({
        "color": "blue",
        "ignoreUriAndModuleKeyValidation": True,
        "moduleKey": "com.atlassian.plugins.atlassian-connect-plugin:com.oldstreetsolutions.atlassian.jira.custom-charts__custom-chart-dashboard-item",
        "position": {
            "column": 1,
            "row": 0
        },
        "title": gadget_name
    })

    response_gadget = requests.request(
        "POST",
        gadget_url,
        data=payload_gadget,
        headers=headers_with_content,
        auth=auth
    )

    data_gadget = json.loads(response_gadget.text)

    gadget_id = data_gadget["id"]

    update_gadget(dashboard_id, gadget_id)


def update_gadget(dashboard_id: str, gadget_id: str):

    url_to_update_gadget = "https://mobsite.atlassian.net/rest/api/2/dashboard/" + str(dashboard_id) + "/items/" + str(
        gadget_id) + "/properties/params?_r=1695727815847"

    requests.request(
        "PUT",
        url_to_update_gadget,
        data=payload2,
        headers=headers_with_content,
        auth=auth
    )


# If the dashboard doesn't exist, create a new dashboard and gadget.
if not dashboard_updated:
    create_new_dashboard_and_gadget_cloud()