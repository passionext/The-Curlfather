# The CUrlFather

**The CUrlFather** is an interactive Python utility for sending HTTP POST requests, managing frequently-used URLs, and assisting with crafting API requests. It features auto-completion for HTTP headers and URLs, persistent storage of your favorite API endpoints, and even supports TLS certificate validation for secure connections.

## Features

- **Interactive Menu:** Simple text UI for sending POST requests, removing saved URLs, and exiting.
- **Smart Auto-Completion:** Tab-completion for HTTP headers and previously used URLs.
- **Persistent URL Storage:** Frequently used URLs are stored in a JSON file with usage statistics.
- **Header and Data Input:** Easily add multiple HTTP headers and JSON body fields per request.
- **TLS Certificate Verification:** Optionally validate server certificates using your own certificate file.
- **Error Handling:** Clear error messages for timeouts, connection errors, and invalid inputs.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/passionext/The-Curlfather.git
   cd The-Curlfather
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   _Key dependencies: `requests`, `cryptography`_

## Usage

Run the script:

```bash
python main.py
```

You will see a menu:

```
Welcome to The CUrlFather.

I'm gonna make you a curl that you *cannot* refuse.

Ready to send some requests? Let's make them an offer they can't deny...

Main Menu:
1. Send a POST request
2. Remove a saved URL
3. Exit
```

### 🟢 Sending a POST Request

1. Select option `1`.
2. Enter a URL (use TAB for auto-completion if you have saved URLs).
3. Specify the number of HTTP headers, then input each header name (TAB-completes common headers) and its value.
4. Specify the number of JSON data fields, then input each key and value.
5. Optionally, verify the server's TLS certificate by providing a valid PEM certificate file.
6. The response will be printed with status code and body.

### 🟠 Removing a Saved URL

1. Select option `2`.
2. Choose the number corresponding to the URL you wish to remove.

### 🔴 Exiting

- Select option `3` to quit.

## Data Persistence

- URLs are stored in `urls.json` with added date and usage count.
- The file is updated automatically when you add or remove URLs.

## Requirements

- Python 3.6+
- All dependencies are listed in `requirements.txt`.
   - Main: `requests`, `cryptography`

## Example Session

```text
Main Menu:
1. Send a POST request
2. Remove a saved URL
3. Exit
Select an option (1-3): 1

Enter URL (use TAB for auto-completion): https://httpbin.org/post
How many HTTP headers do you want to add? 2
Enter an HTTP header (use TAB for auto-completion): Content-Type
Enter header value for 'Content-Type': application/json
Enter an HTTP header (use TAB for auto-completion): Authorization
Enter header value for 'Authorization': Bearer xyz
How many data fields do you want to add to the JSON body? 1
Enter data key #1: name
Enter value for 'name': CUrlFather
Do you want to verify the server's TLS certificate? (y/n): n

Status Code: 200
Response Body:
{
  ...
}
```

## Security

- Certificate validation uses `cryptography` to ensure your certificate file is valid before use.
- Only local file access is performed; no sensitive data leaves your machine.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the Apache License 2.0.
You may obtain a copy of the license at:

http://www.apache.org/licenses/LICENSE-2.0

_May your requests always get a favorable response. The CUrlFather is here to make sure they can't refuse!_
