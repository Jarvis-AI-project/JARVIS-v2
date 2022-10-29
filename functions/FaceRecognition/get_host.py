# curl \-H "Authorization: Bearer {ak_2GXr2bzSiGmkzicHtfgvauQcQSf}" \-H "ngrok-version: 2" \https://api.ngrok.com/endpoints
# https://python-api.docs.ngrok.com/

def get_host():
    import ngrok
    client = ngrok.Client("2GY9HT5G5iRcmXI6OhVwD818gUq_4PDnxtteqNmFZvjnNkVri")
    try:
        for token in client.tunnels.list():
            print('SERVER ENDPOINT URL:', token.public_url)
            print('SERVER ENDPOINT START TIME:', token.started_at)
            print('SERVER ENDPOINT FORWARDED FROM:', token.forwards_to)
            return token.public_url
        return False
    except Exception as e:
        print('HOST: Error')
        print(e)
        return False

if __name__ == '__main__':
    print(get_host())