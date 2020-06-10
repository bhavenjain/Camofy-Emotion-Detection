import boto3

#Rekognition services aws declaration
client = boto3.client('rekognition')

#Opening the image fromm the folder
with open('kid1.jpg','rb') as hell:
    imgbytes = hell.read()

#celeb check
celeb = client.recognize_celebrities(Image={'Bytes': imgbytes})
#facial expression
FaceDetect = client.detect_faces(Image={'Bytes': imgbytes},
                              Attributes=['ALL'])

#If the player is not a celebrity
if len(celeb['CelebrityFaces']) == 0:
    numfaces = len(FaceDetect['FaceDetails'])
    print('Found:', numfaces ,end=' ')
    if numfaces == 1:
        print('face,')
    else:
        print('faces,')

    #gender and age distinction
    for facedeets in FaceDetect['FaceDetails']:
        fmtstr = '{gender}, age {lowage}-{highage},'

        #Facial hairs
        if facedeets['Mustache']['Value'] and facedeets['Beard']['Value']:
            fmtstr += ' with beard and mustache,'
        elif facedeets['Mustache']['Value']:
            fmtstr += ' with mustache,'
        elif facedeets['Beard']['Value']:
            fmtstr += ' with beard,'

        #glasses
        if facedeets['Sunglasses']['Value']:
            fmtstr += ' wearing sunglasses,'
        elif facedeets['Eyeglasses']['Value']:
            fmtstr += ' wearing glasses,'

        #Printing the specs of the person
        print(
            fmtstr.format(
                gender=facedeets['Gender']['Value'],
                lowage=facedeets['AgeRange']['Low'],
                highage=facedeets['AgeRange']['High'],
            )
        )
        #Printing Emotion with highest confidence
        check = facedeets['Emotions']
        highest = 0
        for i in check:
            if(i['Confidence'] > highest):
                type = i['Type']
                highest = i['Confidence']
        #print the Emotion
        print(type,'%0.1f'%highest)

#if the player turns out to be a celebrity
else:
    celebExp = FaceDetect['FaceDetails'][0]['Emotions']
    #name of the celeb
    for face in celeb['CelebrityFaces']:
        print(face['Name'],'Confidence:', face['MatchConfidence'])

    highest = 0
    #Emotion with confidence, Result
    for i in celebExp:
        if(i['Confidence'] > highest):
            type = i['Type']
            highest = i['Confidence']

    #printing the result
    print(type,"Confidence:",'%0.1f'%highest)
