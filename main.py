from main_openai import main_openai


if __name__ == '__main__':
    params = dict(api_key="Your API key",
                  text_you_want_to_send="Hi, I have a friend, her name is Victor. He is super smart, "
                                        "sharp and beautiful. Use French, English, Russian and Chinese "
                                        "to compliment him. She is a great friend. Use only one "
                                        "sentence for each language.",
                  max_tokens=1500,  # only change it if your input and output are too long
                  save_format='md')  # can be 'md' or 'txt' or anything you think is convenient

    main_openai(**params)  # will save a file named 'response' in the format you choose in the same directory

