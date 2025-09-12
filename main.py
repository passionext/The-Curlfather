import json
import requests
import readline
from datetime import datetime


# Predefined list of common HTTP headers.
COMMON_HTTP_HEADERS = [
    "Accept", "Accept-Charset", "Accept-Encoding", "Accept-Language",
    "Authorization", "Cache-Control", "Connection", "Content-Length",
    "Content-Type", "Cookie", "Date", "DNT", "Expect", "From", "Host",
    "If-Match", "If-Modified-Since", "If-None-Match", "If-Range",
    "If-Unmodified-Since", "Max-Forwards", "Origin", "Pragma",
    "Proxy-Authorization", "Range", "Referer", "TE", "Upgrade",
    "User-Agent", "Via", "Warning", "X-Requested-With", "X-Forwarded-For",
    "X-Forwarded-Host", "X-Forwarded-Proto", "X-Real-IP", "X-CSRF-Token",
    "X-API-Key"
]


def completer(text, state):

    """The completer function provides auto-completion suggestions for HTTP headers based on the user's current input.

    Parameters:
        text (str): The current text typed by the user.
        state (int): The current state of the auto-completion suggestions.

    Returns:
        str or None: The matching header at the given state, or None if there are no more match."""

    # Create a list called 'options' that stores all headers name from COMMON_HTTP_HEADERS that start with the string
    # 'text' typed by the user. The list comprehension loops through each header in COMMON_HTTP_HEADERS, using 'h' as
    # the loop variable, where 'h' represents the current HTTP header string being checked.
    #
    # For each 'h', both 'h' and the user input 'text' are converted to lowercase to ensure the comparison is
    # case-insensitive. Then check if 'h' starts with 'text' (case-insensitive) using the string method .startswith().
    # Only those headers that satisfy this condition are included in the 'options' list.
    options = [h for h in COMMON_HTTP_HEADERS if h.lower().startswith(text.lower())]

    # 'state' is an integer provided by the readline library (or whatever autocomplete system is calling this function).
    # It represents the index of the autocomplete suggestion to return at this moment.
    #
    # For example:
    #   - When the user presses TAB for the first time, state = 0 (requesting the first suggestion),
    #   - The second press means state = 1 (second suggestion),
    #   - and so on.
    #
    # This mechanism allows the function to return suggestions one by one on repeated calls.
    #
    # We check if 'state' is less than the number of available options.
    # This is important because:
    #  - 'len(options)' gives the total number of matching headers found.
    #  - If 'state' is less than that number, we have a valid suggestion to return.
    if state < len(options):
        return options[state]
    else:
        return None



def save_url(url_to_save, filename="urls.json"):

    """Save the URL from the given URL to the given filename.
    Parameters:
        url_to_save (str): The URL to save.
        filename (str): The filename to save the URL to.
    Returns:
        It returns nothing. It just saves the URL to the given filename.
    """
    try:
        with open(filename, "r") as f:
            file = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = []

    for entry in data:
        if entry["url"] == url_to_save:
            entry["usage_count"] += 1
            break
        else:
            file.append({
                "url": url_to_save,
                "added_on": datetime.now().strftime("%Y-%m-%d"),
                "usage_count": 1
            })

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

def load_urls(filename="urls.json"):
    """Load the URLs from the given filename.
    Parameters:
        filename (str): The filename to load the URLs from.
    Returns:
        stored_urls (dict): The URLs stored in the given filename."""
    try:
        with open(filename, "r") as f:
            file = json.load(f)
            return file["urls"]
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = []
        return file



# Take the input from the user.
url = input("Enter URL: ")

# Creating the headers.
headers = {}
num_headers = int(input("Enter number of headers: "))
readline.set_completer(completer)
for i in range(num_headers):
    readline.parse_and_bind("tab: complete")
    key = input("Inserisci un header HTTP (usa TAB per completare): ") #da rivedere come frase
    print(f"Hai inserito: {key}")
    value = input(f"Enter header value for '{key}': ")
    headers[key] = value

# Creating the data in the JSON format to be sent out.
data = {}
num_fields = int(input("Enter number of JSON fields (data): "))
for i in range(num_fields):
    key = input(f"Enter data key #{i + 1}: ")
    value = input(f"Enter value for '{key}': ")
    data[key] = value

# Send a request.
response = requests.post(url, headers=headers, json=data)

# Output result.
print("\nStatus Code:", response.status_code)
print("Response Body:")
print(response.text)
