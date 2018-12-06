import requests

result = requests.get('http://127.0.0.1:5011/tantargyak')
targyak = result.json()
print(targyak)
for targy in targyak:
        if targy['kepzes'] == 'bsc' and targy['spec'] == 'aut':
            for listelem in targy['targyak']:
                print('Nev:{0}\n\tTárgykód:{1}\n'.format(
                    listelem['nev'], listelem['targykod']))
