import requests

def run_query(query, headers):

  # Using GraphQL API
  url = 'https://api.github.com/graphql'
  response = requests.post(url, json={'query': query}, hearders=header)

  if response.status.code == 200:
    return response.json()
  else:
    raise Exception(f'Request failed with status code {response.status_code}. {response.text}')

def main():
  github_token = 'GH_TOKEN'

# GraphQL query to get the viewer's login name
query = """
{
  viewer {
      login
    }
}
"""

header = {
  'Authorization': f'Bearer {github_token}',
}

try:
  result = run_query(query, headers)
  login_name = result['data']['viewer']['login']
  print(f'Logged in as: {login_name}')
except Exception as e:
  print(f'Error: {e}')

if __name__ == '__main__':
  main()
