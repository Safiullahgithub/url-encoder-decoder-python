import urllib.parse

url = input("Enter the URL: ")
print("1. Encode the URL")
print("2. Decode the URL")
choice = int(input("Enter your choice: "))

if choice == 1:
    encoded_url = urllib.parse.quote(url, safe='')
    print(f"The encoded URL is: {encoded_url}")
elif choice == 2:
    decoded_url = urllib.parse.unquote(url)
    print(f"The decoded URL is: {decoded_url}")
else:
    print("Invalid choice. Please enter either 1 or 2.")
