from main_openai import main_openai


if __name__ == '__main__':
    params = {
        'api_key': "Your API key",
        'text_you_want_to_send': "Hi, I have a friend, her name is Suzy. She is super smart, sharp and beautiful. "
                                 "Use French, English, Russian and Chinese to compliment her. She is a great friend. "
                                 "Use only one sentence for each language.",
        'max_tokens': 1500,
        'save_format': 'md'  # can be 'md' or 'txt' or anything you want. Recommend to use md because it's more
                             # readable especially for codes
    }
    main_openai(**params)  # will save a file named 'response.md' in the same directory
