import json
import requests
import readline
from datetime import datetime

# 77434978-5645-6348-4377-3570764d4d4f
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



def header_completer(text, state):

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



def url_completer(text, state):
    """The completer function provides auto-completion suggestions for URLs based on the user's current input.

    Parameters:
        text (str): The current text typed by the user.
        state (int): The current state of the auto-completion suggestions.

    Returns:
        str or None: The matching URL at the given state, or None if there are no more matches.
    """
    urls = [entry["url"] for entry in load_urls()]
    matches = [url for url in urls if url.startswith(text)]
    if state < len(matches):
        return matches[state]
    return None



def get_valid_int(prompt="Enter an integer: "):
    """Prompt the user for an integer input until a valid integer is provided."""
    while True:
        user_input = input(prompt)
        try:
            value = int(user_input)
            return value
        except ValueError:
            print("Oops! That's not a valid integer. Please try again.")

        

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

    # Flag to track if URL was found
    found = False

    for entry in file:
        if entry["url"] == url_to_save:
            entry["usage_count"] += 1
            found = True
            break

    if not found:
        file.append({
            "url": url_to_save,
            "added_on": datetime.now().strftime("%Y-%m-%d"),
            "usage_count": 1
        })

    with open(filename, "w") as f:
        json.dump(file, f, indent=2)

def load_urls(filename="urls.json"):
    """Load the URLs from the given filename.
    Parameters:
        filename (str): The filename to load the URLs from.
    Returns:
        stored_urls (dict): The URLs stored in the given filename."""
    try:
        with open(filename, "r") as f:
            file = json.load(f)
            return file
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = []
        return file


def remove_incorrect_url(url_to_remove, filename="urls.json"):
    """Remove a URL from the saved URLs file."""
    try:
        with open(filename, "r") as f:
            file = json.load(f)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        file = []
    new_file = [entry for entry in file if entry["url"] != url_to_remove]
    with open(filename, "w") as f:
        json.dump(new_file, f, indent=2)


if __name__ == "__main__":

    # Print a welcome message.
    print("""
        Welcome to The CUrlFather.

        I’m gonna make you a curl  
        that you *cannot* refuse. 🍝🔗

        Ready to send some requests? Let’s make 'em an offer they can't deny...
        """)
    print("Welcome to The Curlfather - Your HTTP POST Request Assistant!")

    # Load the stored URLs from the JSON file.
    url_stored = load_urls()

    # Create the headers dictionary.
    headers = {}

    # Set completer for URLs when entering the URL.
    # A completer function provides intelligent auto-completion for command arguments, offering a list of possible values when the user presses the Tab key.
    # It typically takes two arguments: the current input text and the state (index of completion suggestion), and returns a matching completion string or None 
    # when no more completions are available.
    readline.set_completer(url_completer)

    # Bind the TAB key to the completion function you just set.
    readline.parse_and_bind("tab: complete")

    # Take the URL input from the user.
    url_input = input("Enter URL (use TAB for auto-completion): ")
    
    # Call the function to save the URL.
    save_url(url_input)

    
    
    num_headers = int(input("Enter number of headers: "))
    for i in range(num_headers):
        # Set completer for headers when entering headers.
        readline.set_completer(header_completer)
        readline.parse_and_bind("tab: complete")
        key = input("Enter an HTTP header (use TAB for auto-completion): ")
        print(f"You entered: {key}")
        value = input(f"Enter header value for '{key}': ")
        headers[key] = value

    # Enter JSON data fields.
    data = {}
    num_fields = int(input("Enter number of JSON fields (data): "))
    for i in range(num_fields):
        key = input(f"Enter data key #{i + 1}: ")
        value = input(f"Enter value for '{key}': ")
        data[key] = value

    # Send a POST request with a timeout for robustness.
    try:
        response = requests.post(url_input, headers=headers, json=data, timeout=10)
        print("\nStatus Code:", response.status_code)
        print("Response Body:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", str(e))

