# https://spotipy.readthedocs.io/en/master/
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
import features.music.spotify.azure_sdk as azure_sdk
import sys, os
#-----<AUTHENTICATION>-----#
def take_sp_oauth(scope):
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
        return sp
    except Exception as e:
        print('Spotify OAuth failed.')
        print(e)
        return False

# def sp_cred():
#     try:
#         sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
#         return sp
#     except Exception as e:
#         print('Spotify failed.')
#         print(e)
#         return False
#-----</AUTHENTICATION>-----#


#-----<json>-----#
def json(dict):
    try:
        import json
        with open('output.json', 'w') as file:
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


def spotify_sdk(command):
    try:
        print('Spotify SDK : STARTED')

        spotify_intent = azure_sdk.azure_query(command, "JARVIS-SPOTIFY", 'v0.1-dep1')
        # print(spotify_intent)

        sp_read = take_sp_oauth(scope='user-read-playback-state')
        for device in sp_read.devices()['devices']:
            if device['is_active'] == True:
                active_device_id = device['id']
                print('Currently active device is "{}"'.format(device['name']))

        if spotify_intent['intent'] == 'Spotify.ChangeVolume.ByValue':
            for entity in spotify_intent['entities']:
                if entity['entity'] == 'Spotify.ChangeVolume.Value':
                    new_volume_value = int(entity['entity_value'].replace('%', ''))
                    if new_volume_value > 100:
                        new_volume_value = 100
                    elif new_volume_value < 0:
                        new_volume_value = 0
                    print('Current volume of device "{}" is {}%'.format(device['name'], device['volume_percent']))
                    sp_modify = take_sp_oauth(scope='user-modify-playback-state')
                    sp_modify.volume(new_volume_value, device_id=active_device_id)
                    print('Volume of device "{}" changed to {}%'.format(device['name'], new_volume_value))
            
        elif spotify_intent['intent'] == 'Spotify.ChangeVolume.Decrease':
            print('Current volume of device "{}" is {}%'.format(device['name'], device['volume_percent']))
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.volume(device['volume_percent'] - 10, device_id=active_device_id)
            print('Volume of device "{}" changed to {}%'.format(device['name'], device['volume_percent'] - 10))
        
        elif spotify_intent['intent'] == 'Spotify.ChangeVolume.Increase':
            print('Current volume of device "{}" is {}%'.format(device['name'], device['volume_percent']))
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.volume(device['volume_percent'] + 10, device_id=active_device_id)
            print('Volume of device "{}" changed to {}%'.format(device['name'], device['volume_percent'] + 10))

        elif spotify_intent['intent'] == 'Spotify.CurrentVolume':
            print('Current volume of device "{}" is {}%'.format(device['name'], device['volume_percent']))
        
        elif spotify_intent['intent'] == 'Spotify.Track.Play':
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.start_playback(device_id=active_device_id)
            print('Playback started on device "{}"'.format(device['name']))
        
        elif spotify_intent['intent'] == 'Spotify.Track.Pause-Stop':
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.pause_playback(device_id=active_device_id)
            print('Playback paused on device "{}"'.format(device['name']))
        
        elif spotify_intent['intent'] == 'Spotify.NextTrack':
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.next_track(device_id=active_device_id)
            print('Next track on device "{}"'.format(device['name']))

        elif spotify_intent['intent'] == 'Spotify.PreviousTrack':
            sp_modify = take_sp_oauth(scope='user-modify-playback-state')
            sp_modify.previous_track(device_id=active_device_id)
            print('Previous track on device "{}"'.format(device['name']))

        elif spotify_intent['intent'] == 'Spotify.CurrentTrack':
            sp_read = take_sp_oauth(scope='user-read-playback-state')
            current_track = sp_read.current_user_playing_track()
            print('Currently playing track "{}" by "{}" on device "{}"'.format(current_track['item']['name'], current_track['item']['artists'][0]['name'], device['name']))
        
        #elif

        else:
            print('This spotify intent is not supported yet.')
            return True


    except Exception as e:
        print('Spotify SDK : FAILED')
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type,  fname,  exc_tb.tb_lineno)
        return False



if __name__ == '__main__':
    spotify_sdk('decrease spotify volume by 50')