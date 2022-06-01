import requests


test_file = open("./Utils/1.jpg", "rb")
test_url = "http://127.0.0.2:8000/API"
test_response = requests.post(test_url, files = {"file": test_file})

if test_response.ok:
    print("Upload completed successfully!")
    print(test_response.text)
else:
    print("Something went wrong!")
    print("status = ",test_response.status_code)
    print("reason : ",test_response.reason)
    print("header : ",test_response.headers)