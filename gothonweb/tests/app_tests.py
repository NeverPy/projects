from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    # check that we get a 404 on the / URL
    resp = app.request("/hello")
    assert_response(resp, status="404")

    # test our first GET request to /hello
    resp = app.request("/")
    assert_response(resp,status="303")
    
    contains="Play Again".encode()
    resp = app.request("/game")
    assert_response(resp,contains=contains)
    
    data = {'action': 'shoot!'}
    resp = app.request("/game", method="POST", data=data)
    contains="shoot!".encode()
    assert_response(resp,status="303")
    
    contains="Play Again".encode()
    resp = app.request("/game")
    assert_response(resp,contains=contains)
    """
    contains="shoot".encode()
    resp = app.request("/game")
    assert_response(resp,contains=contains)
 
    # make sure default values work for the form
    resp = app.request("/game", method="POST")
    contains="Nobody".encode()
    assert_response(resp, contains=contains)

    # test that we get expected values
    data = {'name': 'Zed', 'greet': 'Hola'}
    resp = app.request("/hello", method="POST", data=data)
    contains="Zed".encode()
    assert_response(resp, contains=contains)

    data = {'action': 'shoot!'}
    resp = app.request("/game", method="POST", data=data)
    contains="shoot".encode()
    assert_response(resp,status="303")
    
   """ 
    #assert_response(resp,status="303")