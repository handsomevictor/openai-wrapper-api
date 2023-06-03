import requests


def main_openai(api_key, text_you_want_to_send, max_tokens=1500, save_format='md'):
    url = "http://34.78.245.234:5001/openai_gpt35turbo"

    headers = {
        'Content-Type': 'application/json',
        'X-Api-Key': api_key
    }
    data = {
        "message": text_you_want_to_send,
        'max_tokens': max_tokens
    }
    res = requests.post(url, headers=headers, json=data)

    if res.status_code == 200:
        res = res.json()['response']
    else:
        raise Exception(f'Error: {res.status_code}, please contact Victor.')

    with open(f'response.{save_format}', 'w') as f:
        f.write(res)
