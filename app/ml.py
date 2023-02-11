import cohere

co = cohere.Client('ZG1hp4UsOagPS7V8vOiSxkGMljolDMPi96KAvboq')

def reply(prompt):

    response = co.generate(
    model='command-xlarge-nightly',
    prompt=prompt,
    max_tokens=150,
    temperature=0.8,
    stop_sequences=["--"],
    return_likelihoods='NONE',
    truncate='START')
    return response.generations[0].text

prompt = f"""
I am 71 years old. I will add my comfort levels as a number, with using the 
following fields below:
Banking: 7
Hardware: 4
Social Media: 7
Here is some additional info about how comfortable I am with using technology:
I struggle a lot with uploading pictures to social media specifically.

Given all this info, respond to the following question about help with technology asked by the above user
How do I send a friend request on Facebook?
"""
# print(reply(prompt))