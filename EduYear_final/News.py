import requests
from ss import key

api_address = f"https://newsapi.org/v2/everything?q=Apple&sortBy=popularity&apiKey={key}"
json_data = requests.get(api_address).json()

ar=[]

def news():
    for i in range(3):
        ar.append("Number "+ str(i+1) + "," + json_data['articles'][i]["title"]+".")

    return ar

# arr=news()
# print(arr)



# # Make the API Request
# response = requests.get(api_address)



# # Check the Response
# if response.status_code == 200:
#     json_data = response.json()
#     print(json_data)
# else:
#     print(f"Error: Unable to fetch news (status code: {response.status_code})")
#     print(response.text)
