import cohere

co = cohere.client('ZG1hp4UsOagPS7V8vOiSxkGMljolDMPi96KAvboq')

def reply(prompt):
    
    response = co.generate(
    model='command-xlarge-nightly',
    prompt=prompt,
    max_tokens=100,
    temperature=0.8,
    stop_sequences=["--"],
    return_likelihoods='NONE',
    truncate='START')
    return response.generations[0].text