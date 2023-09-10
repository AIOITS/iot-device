import requests

class api():
  base_url = 'https://aioits-backend-q6ihv4us2q-uc.a.run.app'
  
  @staticmethod
  def get(data):
    query = '''
      query{
        user(where: {id: {equals: 1}}){
          %s
        }
      }
    ''' % (data)

    return requests.post(
      url= f"{api.base_url}/graphql",
      headers = {
        "Content-Type": "application/json",
      },
      json= {
        "query": query
      }
      ).json()
  
  def post(endpoint, body):
    return requests.post(
      url= f"{api.base_url}/{endpoint}",
      headers = {
        "Content-Type": "application/json",
      },
      json=body
      ).json()