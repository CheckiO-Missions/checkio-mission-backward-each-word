"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": [''],
            "answer": '',
        },
        {
            "input": ['world'],
            "answer": 'dlrow',
        },
        {
            "input": ['hello world'],
            "answer": 'olleh dlrow',
        },
        {
            "input": ['hello   world'],
            "answer": 'olleh   dlrow',
        },
        {
            "input": ['welcome to a game'],
            "answer": 'emoclew ot a emag',
        },
    ],
    "Extra": [
        {
            "input": ['ha ha ha   this is cool'],
            "answer": 'ah ah ah   siht si looc',
        }
    ]
}
