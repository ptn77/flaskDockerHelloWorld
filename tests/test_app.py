from app import hello_geek

def test_app():
    assert hello_geek() == 'Hello from Flask and Docker'