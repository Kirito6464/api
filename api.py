import requests


def int_superhero():
    global hulk_int, captain_america_int, thanos_int
    url = "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    resp = requests.get(url)
    all = resp.json()
    for i in range(len(all)):
        biography = all[i]
        if 'Hulk' == biography['name']:
            hulk_int = all[i]['powerstats']['intelligence']
        elif 'Captain America' == biography['name']:
            captain_america_int = all[i]['powerstats']['intelligence']
        elif 'Thanos' == biography['name']:
            thanos_int = all[i]['powerstats']['intelligence']
    max_int = max(hulk_int, captain_america_int, thanos_int)
    if hulk_int == max_int:
        print('Hulk')
    elif captain_america_int == max_int:
        print('Captain America')
    elif thanos_int == max_int:
        print('Thanos')


if __name__ == '__main__':
    int_superhero()
