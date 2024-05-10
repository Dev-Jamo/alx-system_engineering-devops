import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "YourBot/1.0"}  # Update the User-Agent string as needed
    params = {"limit": 10}
    
    response = requests.get(url, headers=headers, params=params)
    
    if response.status_code == 200:
        data = response.json().get("data")
        if data:
            children = data.get("children")
            if children:
                for child in children:
                    title = child.get("data", {}).get("title")
                    if title:
                        print(title)
            else:
                print("No posts found in this subreddit.")
        else:
            print("No data found in the response.")
    elif response.status_code == 404:
        print("Subreddit not found.")
    else:
        print(f"Error {response.status_code}: Failed to fetch data.")
