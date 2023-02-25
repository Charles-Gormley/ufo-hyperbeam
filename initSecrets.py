import os
def create_aylien_file(id, api_key):
    '''To obtain credentials please go to: https://aylien.com/product'''
    home_dir = os.path.expanduser("~")
    aylien_file = os.path.join(home_dir, ".aylien")
    with open(aylien_file, "w") as f:
        f.write(f"id={id}\n")
        f.write(f"api_key={api_key}\n")

def get_aylien_credentials():
    home_dir = os.path.expanduser("~")
    aylien_file = os.path.join(home_dir, ".aylien")
    if os.path.exists(aylien_file):
        with open(aylien_file, "r") as f:
            credentials = {}
            for line in f.readlines():
                key, value = line.strip().split("=")
                credentials[key] = value
            return credentials.get("id"), credentials.get("api_key")
    else:
        return KeyError('Could Not find api keys.') # No API Key Found. Need to create_aylien_file first and pass needed arguments

if __name__ == "__main__":
    # Example usage
    id, api_key = get_aylien_credentials()
    print(f'Your id: {id}')
    print(f'Your API Key {api_key}')