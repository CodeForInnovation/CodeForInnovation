# Simple Agent Implementation

class SimpleAgent:
    def __init__(self):
        self.name = "Simple Agent"

    def greet(self):
        return f"Hello, I am {self.name}. I do not require an API key to function!"

# Example usage
if __name__ == "__main__":
    agent = SimpleAgent()
    print(agent.greet())