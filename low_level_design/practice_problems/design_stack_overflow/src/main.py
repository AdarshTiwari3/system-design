"""Main runner"""
from client.client import StackOverflowClient


if __name__ == "__main__":
    print("Running Stackoverflow LLD Problem")
    client=StackOverflowClient()
    client.main()