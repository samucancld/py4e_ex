def create_url():
    print('========= INGRESA USUARIOS SEPARADOS POR ENTER =========')
    louser = list()
    usernames = 'usernames='
    while True:
        this_user = input('arroba> ')
        if len(this_user) < 1 or this_user == 'listo': break
        louser.append(this_user)
    for each_user in louser:
        usernames = usernames + each_user + ','
    usernames = usernames[:-1]
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url