This is a very stupid script for letting my friend use ChatGPT 3.5 in Hong Kong.

Basically it is just using Openai API to generate text.

# How to use

1. Install python and `requests` module
   - pip install requests
2. Contact Victor to get the API key
3. Open main.py, change the API key and the text to whatever you want
4. Run main.py and then the text will be generated (several seconds or 10-20 seconds depending on the length of the 
   text gpt3 needs to generate), then the result would be saved to a file called response.md or txt depending on the
   format you choose.


Victor used very simple Flask to build the whole thing, and it's only for his friends' use and for himself don't hesitate to contact him if you have any questions.
