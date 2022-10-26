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


#-----<volume>-----#
#https://developer.spotify.com/console/put-volume/
# def volume(volume_percent, device_name):
#     try:
#         sp = take_sp_oauth(scope='user-modify-playback-state')
#         device_id = get_device_id(device_name)
#         sp.volume(volume_percent, device_id)
#         print('Volume of {} set to {}%'.format(device_name, get_devices()['devices']))
#         return True
#     except Exception as e:
#         print('Spotify volume failed.')
#         print(e)
#         return False
#-----</volume>-----#


def spotify_sdk(command):
    try:
        output = azure_sdk.azure_query(command)
        intent = output['intent']
        if intent == 'Spotify.ChangeVolume':  # control volume of active spotify device
            devices = get_devices()['devices']
            for device in devices:
                if device['is_active'] == True:
                    active_device = device['name']
                    print('Currently active device : ',active_device)
                    # output = azure_sdk.azure_query(command)
                    if intent == 'Spotify.ChangeVolume':
                        for entity in output['entities']:
                            if entity['entity'] == 'Spotify.ChangeVolume.Value':
                                volume = entity['entity_value']
                                try:
                                    volume = int(volume)
                                    if volume > 100:
                                        volume = 100
                                    elif volume < 0:
                                        volume = 0
                                    print('Setting volume to {}% using Spotify.ChangeVolume.Value of devce "{}"'.format(volume, active_device))
                                    sp_modify = take_sp_oauth(scope='user-modify-playback-state')
                                    sp_modify.volume(volume, device['id'])
                                    print('Volume of "{}" set to {}%'.format(active_device, volume))
                                    return True
                                except Exception as e:
                                    print('Spotify.ChangeVolume.Value failed')
                                    print(e)
                                    return False
                        for entity in output['entities']:
                            if entity['entity'] == 'Spotify.ChangeVolume.Key.Increase':
                                try:
                                    current_volume = device['volume_percent']
                                    volume = current_volume + 10
                                    print('Increasing volume to {}% using Spotify.ChangeVolume.Key.Increase of devce "{}"'.format(volume, active_device))
                                    sp_modify = take_sp_oauth(scope='user-modify-playback-state')
                                    if volume > 100:
                                        volume = 100
                                    elif volume < 0:
                                        volume = 0
                                    sp_modify.volume(volume, device['id'])
                                    print('Volume of "{}" increased to {}%'.format(active_device, volume))
                                    return True
                                except Exception as e:
                                    print('Spotify.ChangeVolume.Key.Increase failed')
                                    print(e)
                                    return False
                            elif entity['entity'] == 'Spotify.ChangeVolume.Key.Decrease':
                                try:
                                    current_volume = device['volume_percent']
                                    volume = current_volume - 10
                                    print('Decreasing volume to {}% using Spotify.ChangeVolume.Key.Decrease of devce "{}"'.format(volume, active_device))
                                    sp_modify = take_sp_oauth(scope='user-modify-playback-state')
                                    if volume > 100:
                                        volume = 100
                                    elif volume < 0:
                                        volume = 0
                                    sp_modify.volume(volume, device['id'])
                                    print('Volume of "{}" decreased to {}%'.format(active_device, volume))
                                    return True
                                except Exception as e:
                                    print('Spotify.ChangeVolume.Key.Decrease failed')
                                    print(e)
                                    return False
                    else:
                        print('User has no intent to change volume.')
                        return False
        
        #elif

        else:
            print('Command not found.')
            return True
        return True


    except Exception as e:
        print('Spotify SDK failed.')
        print(e)
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type,  fname,  exc_tb.tb_lineno)
        return False



if __name__ == '__main__':
    spotify_sdk('decrease spotify volume by 50')

#-----<play>-----#
# if __name__ == '__main__':
#     volume(50, device_name='INSPIRON-5593')
#     devices=get_devices()
#     json(devices)