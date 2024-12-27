import requests

def scrape_roblox_group(group_id):
    """
    Scrapes a Roblox group by its ID and logs usernames of all group members into Users.txt.

    :param group_id: The ID of the Roblox group to scrape.
    """
    base_url = f"https://groups.roblox.com/v1/groups/{group_id}/users"
    cursor = ""
    logged_count = 0

    print("Starting to scrape the group...")
    with open("Users.txt", "w") as file:
        while True:
            # Make a GET request to fetch group members
            response = requests.get(f"{base_url}?cursor={cursor}")

            if response.status_code != 200:
                print(f"Failed to fetch group members: {response.status_code}")
                return

            data = response.json()
            
            # Extract usernames from the response
            for user in data.get("data", []):
                username = user.get("user", {}).get("username")
                if username:
                    file.write(username + "\n")
                    logged_count += 1
                    print(f"Logged {logged_count} users...")

            # Check if there is another page of results
            cursor = data.get("nextPageCursor")
            if not cursor:
                break

    print(f"Scraping complete. {logged_count} usernames saved to Users.txt.")

if __name__ == "__main__":
    group_id = input("Enter the Roblox group ID: ").strip()
    scrape_roblox_group(group_id)
