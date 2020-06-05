import boto3
from pprint import pprint
client = boto3.client('rekognition')

with open('kk.jpeg','rb') as hell:
    imgbytes = hell.read()

rekresp = client.detect_faces(Image={'Bytes': imgbytes},
                              Attributes=['ALL'])

pprint(rekresp)

numfaces = len(rekresp['FaceDetails'])
print('Found:', numfaces )
if numfaces == 1:
    print('face:')
else:
    print('faces:')

for facedeets in rekresp['FaceDetails']:
    fmtstr = '{gender} age {lowage}-{highage},'

    if facedeets['Mustache']['Value'] and facedeets['Beard']['Value']:
        fmtstr += ' with beard and mustache,'
    elif facedeets['Mustache']['Value']:
        fmtstr += ' with mustache,'
    elif facedeets['Beard']['Value']:
        fmtstr += ' with beard,'

    if facedeets['Sunglasses']['Value']:
        fmtstr += ' wearing sunglasses,'
    elif facedeets['Eyeglasses']['Value']:
        fmtstr += ' wearing glasses,'

    print(
        fmtstr.format(
            gender=facedeets['Gender']['Value'],
            lowage=facedeets['AgeRange']['Low'],
            highage=facedeets['AgeRange']['High'],
        )
    )

check = facedeets['Emotions']
highest = 0
for i in check:
    if(i['Confidence'] > highest):
        type = i['Type']
        highest = i['Confidence']

print(type,highest)

