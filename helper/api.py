import requests

class api():
  base_url = 'https://aioits-backend-q6ihv4us2q-uc.a.run.app'
  # base_url = 'http://localhost:8080'
  
  @staticmethod
  def get_user_data(data):
    query = '''
      query{
        user(where: {id: {equals: 1}}){
          %s
        }
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
  
  def post(endpoint, body):
    return requests.post(
      url= f"{api.base_url}/{endpoint}",
      headers = {
        "Content-Type": "application/json",
      },
      json=body
      ).json()