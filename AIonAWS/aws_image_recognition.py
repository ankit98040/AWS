#webcam photo click
import cv2
import boto3
cap = cv2.VideoCapture(0)
#activates the camera 
#0 for internal webcam, 1 for any external web cam
myphoto = "ankit.jpg"
ret , photo = cap.read()
#clicks the photo
#print(ret)
cv2.imwrite(myphoto, photo)
cap.release()
#releases the camera
#uploading image to s3
region = "ap-southeast-1"
bucket = "aiawsankit"
s3 = boto3.resource('s3')
s3.Bucket(bucket).upload_file(myphoto, "file.jpg")
#connect rek: ask for method
rek = boto3.client('rekognition', region)
#client => resource
#but resource only has a few service so for other services, we use client
upimage = "file.jpg"
response = rek.detect_labels(
    Image={
              'S3Object': {
                  'Bucket': bucket,
                  'Name': upimage
              }
          },
          MaxLabels=10,
          MinConfidence=50
)
#response
for i in range(5):
    print( response['Labels'][i]['Name'])