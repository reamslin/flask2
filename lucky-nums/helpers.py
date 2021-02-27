import random
import requests

class InputError(Exception):
    """ raised when one or more inputs are invalid """

    def __init__(self):
        self.errors = {}
    
    def add(self, expr, msg):
        self.errors[expr] = msg

class Result():
    """ returns the result of fetching num/year data. 

    attributes: 
    msg: "ok" or "input error"
    value: lucky number data dict or array of error msg tuple
    """
    def __repr__(self):
        return f'<Result msg : {self.msg}, value : {self.value}>'

    def __init__(self, msg, value):
        self.msg = msg
        self.value = value
        
def getData(content):
    """ Will make API request to numbersapi if no input errors occured.
    Returns a result object with msg either 'input error' or 'ok' and value will contain fact data or error data"""
    try:
        [name, email, year, color] = check_inputs(content)
    except InputError as err:
        return Result("input error", err.errors) 
    else:
        random_num = random.randint(1, 100)

        numResp = requests.get(f'http://numbersapi.com/{random_num}?json')
        numFact = numResp.json()['text']
        yearResp = requests.get(f'http://numbersapi.com/{year}/year?json')
        yearFact = yearResp.json()['text']
        return Result("ok", {"num": {"fact": numFact,
                                        "num": random_num},
                            "year": {"fact": yearFact,
                                        "year": year}
                            })
    

def check_inputs(content):
    """ checks validity of inputs, raising an InputError if one or more are invalid """

    error = InputError()
    try:
        name = content['name']
        if name == "":
            raise ValueError()
    except:
        error.add("name", ["This field is required"])
    
    try:
        email = content['email']
        if email == "":
            raise ValueError()
    except:
        error.add("email", ["This field is required"])
    
    try:
        year = content['birthyear']
        if not (1900 <= int(year) <= 2000):
            raise ValueError()
    except:
        error.add("year", ["Invalid value. Birthyear must be a number between 1900 and 2000"])

    try:
        color = content['color']
        if not (color in ["red", "orange", "blue", "green"]):
            raise ValueError()
    except:
        error.add("color", ["Invalid value. Must be one of 'red', 'blue', 'green', or 'orange'"])

    if error.errors:
        raise error

    return [name, email, year, color] 