import spotipy.util as util


def login(username: str = None,
          scope='user-library-read',
          client_id='8dc4d83d8d5646a2b4838a873d23a6ec',
          client_secret='447f394bc3374e5dbbc2153f0d1a81a8',
          redirect_uri='http://localhost/'):

    if username is None:
        username = input("Spotify/facebook username: ")

    token = util.prompt_for_user_token(username, scope,
                                       client_id=client_id,
                                       client_secret=client_secret,
                                       redirect_uri=redirect_uri)

    if not token:
        print("Can't get token for", username)
        exit(1)

    return token
