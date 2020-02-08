from src import bingo
from src import spotify


if __name__ == "__main__":
    token = spotify.login()
    bingo.run_bingo(token)
