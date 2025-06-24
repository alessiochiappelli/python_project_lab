from app.greeter import Greeter

def test_cases():
    names = ["Alessio", "Ada", "", "👾"]
    
    for name in names:
        greeter = Greeter(name)
        print(greeter.greet())

if __name__ == "__main__":
    test_cases()