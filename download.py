import requests

url = "https://speedtest.poorhub.pro/cf.7z"
output_file = "cf.7z"

try:
    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_file, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                file.write(chunk)

    print(f"File '{output_file}' downloaded successfully.")
except requests.exceptions.RequestException as e:
    print(f"Error downloading the file: {e}")
