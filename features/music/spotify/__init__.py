# https://spotipy.readthedocs.io/en/master/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

#-----<AUTHENTICATION>-----#
def take_sp_oauth(scope):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        return sp
    except Exception as e:
        print('Spotify OAuth failed.')
        print(e)
        return False

def sp_cred():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
        return sp
    except Exception as e:
        print('Spotify failed.')
        print(e)
        return False
#-----</AUTHENTICATION>-----#


#-----<json>-----#
def json(dict):
    try:
        import json
        with open('data.json', 'w') as file:
            json.dump(dict, file, indent=2)
        print('json saved')
        return True
    except Exception as e:
        print('JSON failed.')
        print(e)
        return False
#-----</json>-----#


#-----<get devceices on network>-----#
#https://developer.spotify.com/console/get-users-available-devices/
#https://developer.spotify.com/documentation/web-api/guides/using-connect-web-api/#viewing-device-list
#https://stackoverflow.com/questions/46879418/spotipy-invalid-username
def get_devices():
    try:

        sp = take_sp_oauth(scope='user-read-playback-state')

        devices = sp.devices()
        return devices
    except Exception as e:
        print('Spotify get devices failed.')
        print(e)
        return False
#-----</get devceices on network>-----#


#-----<volume>-----#
#https://developer.spotify.com/console/put-volume/
def volume(volume_percent, device_name):
    try:

        sp = take_sp_oauth(scope='user-modify-playback-state')

        device_id = get_device_id(get_devices(), device_name)
        sp.volume(volume_percent, device_id)
        print('Volume of {} set to {}%'.format(device_name, get_devices()['devices']))
        return True
    except Exception as e:
        print('Spotify volume failed.')
        print(e)
        return False
#-----</volume>-----#


#-----<get-device-id>-----#
def get_device_id(devices, name):
    try:
        devices = devices['devices']
        for device in devices:
            if device['name'] == name:
                return device['id']
    except Exception as e:
        print('Spotify get device id failed.')
        print(e)
        return False
#-----</get-device-id>-----#

if __name__ == '__main__':
    volume(50, device_name='INSPIRON-5593')
