import base64 as b64

def xor_encrypt(data,key):
    ldata=len(data)
    lkey=len(key)
    secret=[]
    num=0
    for each in data:
        if num>=lkey:
            num=num%lkey
        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1
    return b64.b64encode( "".join( secret ).encode() ).decode()


def xor_decrypt(secret,key):

    data = b64.b64decode( secret.encode() ).decode()

    ldata=len(data)
    lkey=len(key)
    secret=[]
    num=0
    for each in data:
        if num>=lkey:
            num=num%lkey

        secret.append( chr( ord(each)^ord(key[num]) ) )
        num+=1

    return "".join( secret )


# data= "1234567"
# key= "owen"
# secret = xor_encrypt(data,key)
# print "cipher_text:", secret 

# plaintxt = xor_decrypt( secret, key )
# print "plain_text:",plaintxt 
