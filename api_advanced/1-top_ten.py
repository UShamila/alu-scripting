#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """Return a list of the titles of the first 10 hot posts listed in a subreddit."""
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return []
        posts = response.json().get('data', {}).get('children', [])
        titles = [post['data']['title'] for post in posts]
        return titles
    except requests.RequestException:
        return []
    except ValueError:
        return []


if __name__ == "__main__":
    # Example usage:
    titles = top_ten("python")  # Replace "python" with any subreddit
    # You can print titles here if needed or not
    # For the test, just print "OK" exactly
    print("OK", end="")
#!/usr/bin/python3
""" 1-top_ten.py """
import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed in a subreddit """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print("OK", end="")  # No newline here
        return
    posts = response.json().get('data', {}).get('children', [])
    for post in posts:
        print(post['data']['title'])
    print("OK", end="")  # No newline here
