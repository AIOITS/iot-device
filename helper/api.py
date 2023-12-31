import requests

class api():
  base_url = 'https://aioits-backend-q6ihv4us2q-uc.a.run.app'
  # base_url = 'http://localhost:8080'
  
  @staticmethod
  def get_user_data(uid, data):
    query = '''
    sim (where: {uid: {equals: "%s"}}) {
      ktp{
        user{
          id
        }
      }
    }
    ''' % uid
    response_user_id = api.get(query)
    print('response_user_id')
    print(response_user_id)
    if (len(response_user_id["data"]["sim"]) <= 0): return None
    
    user_id = response_user_id["data"]["sim"][0]["ktp"]["user"]["id"]
    query = '''
      query{
        user(where: {id: {equals: %d}}){
          %s
        }
      }
    ''' % (int(user_id), data)

    response =  requests.post(
      url= f"{api.base_url}/graphql",
      headers = {
        "Content-Type": "application/json",
      },
      json= {
        "query": query
      }
      ).json()
    # print(f'GET {response}')
    return response
  
  @staticmethod
  def get(data):
    query = '''
      query{
        %s
      }
    ''' % (data)

    response =  requests.post(
      url= f"{api.base_url}/graphql",
      headers = {
        "Content-Type": "application/json",
      },
      json= {
        "query": query
      }
      ).json()
    # print(f'GET {response}')
    return response
  
  def post(endpoint, body, headers={}):
    response = requests.post(
      url= f"{api.base_url}/{endpoint}",
      headers = {
        "Content-Type": "application/json",
        **headers
      },
      json=body
      ).json()
    print(f'POST {response}')
    return response