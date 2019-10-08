import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import time

# Use a service account
cred = credentials.Certificate('{"type": "service_account","project_id": "gomitraapp","private_key_id": "82b857a7d79a4c44883621c102be6fa64f1f7a1c","private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCG9PzmusFkDG6p\nbdirBOHqyt/UJJv6MWyUJe3Uzkl8r2mCQiUE6GNngZ1cKWzMy8nU9qqeBnENPeTi\n2O8nqkQe6Y7SwV1ZB1Trt/GyKNhDH2mXFcapZ9x+JnpbSgTyc2FQsB8J6aZm50t8\nA+woRVXjr5frJTkcwNqIMlMNfXQXBs4wQ37v950h9fVbjplfOsxdA4BtlLDAYnZ/\nlL5tCDSoJHC1h0m/K/Kl8Jwts+bn9VDpd7Xo26PN75i8oFfGaPifyPaEvLhJkWu1\nPsN1KAkKqeuLfl2lbeTFIoA1ULotjqPPY+RB75fHqKD4aIMr+l2Oy7YcWIFXfw8/\nIllo0FllAgMBAAECggEAM+KESICMUVamROVCY52g7Y/JtdnNTccqo1phsWsNva4C\ntl2Pte9SKD0grooOlj3S/tlGhzKazCh7kussJufDAM9yZXyJ0uyKrYUumvwxCL1O\n7xMkKYUQtD8+01IFzOCnDUpo5Hq7ytwpnSg05tahSsP7eB/7cR6D5dDTNWCB/UfF\nlNsNJjiBdNEkZzh24CVy8NcFzBLT9UUFnn6CXK2RYrzJL2JlIPmk0tmD8LEF9UJM\nYpRCsGkX4T3g/1r2zEvoXYDHW1N7mHkpxxAcpEqkDkLOT+24X+TFl3uso1CfFdDD\n89XPRO4an+T1JdzNomdMYGT/K/AIV+5AdiiTLwttEQKBgQC85yxuBjMydCsTv9y/\nU1D8eM5cVu8ct/r4ddsfNBnoVwtwntYNJF92ctUdD4d+in1c2GfhUdfzIhd1RCxp\nKyjBY4+/WZEh0Crt2glrEBb9VP29YzINWenLyGNOM/pqnTMY7GYW0aw3x9P/KAQ5\n8BgIhDe3UsWHtJvVAx1DGC7lywKBgQC25Ilzfwa0wTFTZnyCS60kzwNzTsQj5vyy\nttC8+umvRoJDJSo4jASNTfz8t8m+gGrkC4cuZogOXdXr0eeoJE6Dygzd9bKwz24w\nzEYXsIt+omEmh5oOuVuk9B42sHKx2cHmchJgSeI/JAvaZhhATQZ5ilczPvRZWNpx\n6LHMotJXjwKBgEgFr8fnLz/uULo/7Y842ejYun00XAhMETEH5lqYR8Rw45i1xpDO\nLGOB1sU0tYlGjhOHItwikz5M4jrAmloirXBGYHkpUg9dSfDTr8GVKd6+t9usZVn3\nzQ74QPyBDtn1Q5UeFLJgkNPXqXlgLXRVmSQuHPwVX+CkuMFXZaG+J6tPAoGAdlxu\nq+VARMhmkK/Z0kUBd7nVZNFL1GRPk6UGb9b+VuWNtcCek1viMkSPfkm+8V+QTac8\nRAYs9Qc7Q1Nj1Ygxm86uBxNUImMLz97TWc9yZ3DU6KeHRxIkQhuOVhxZDcp8VxPp\n2pDWL8C3Pw8lkK+Iii3CgzKx1gTP0joinumcsPcCgYBtTeNn9dxo8G07tKWpURQG\nrUcWsE3u3paDTScjo50kYI9gLG9D7+knhI6dTeipf1FeMumZRLlF1BPd64MNfJow\nZb5vHTM9u4qzQRN4zza++rG+yAJwk+JkkKNKMl1WiCfHZC0U2NVd4ZAia2kpmoA7\n9M3JnWaR1e3lG4s5RlXf5A==\n-----END PRIVATE KEY-----\n","client_email": "firebase-adminsdk-klqzo@gomitraapp.iam.gserviceaccount.com","client_id": "102205414454035569371","auth_uri": "https://accounts.google.com/o/oauth2/auth","token_uri": "https://oauth2.googleapis.com/token","auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs","client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-klqzo%40gomitraapp.iam.gserviceaccount.com"}')
firebase_admin.initialize_app(cred)

db = firestore.client()


def newUser(agentCode=None,authUID=None,encodedImage=None,languageCode=None,latitude=None,longitude=None,phoneNumber=None,referralLink=None,referredBy=None,userName=None):
    doc_ref = db.collection('tips').document()
    docId = doc_ref.id
    doc_ref.set({
        'agentCode':agentCode,
        'authUID': authUID,
        'dateRegistered': int(time.time()*1000),
        'encodedImage':encodedImage,
        'languageCode':languageCode,
        'location':firestore.GeoPoint(latitude, longitude),
        'phoneNumber':phoneNumber,
        'referralLink':referralLink,
        'referredBy' :referredBy,
        'userName':userName,
    })