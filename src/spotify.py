import spotipy.util as util


def login(username: str = None,
          scope='user-library-read',
          client_id='8dc4d83d8d5646a2b4838a873d23a6ec',
          client_secret='8c0cbcbcaaac47dd8044e332a9c7393c',
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
