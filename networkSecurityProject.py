import hashlib, binascii
import io



# write a program in python to generate md5 of string data
def hash(state: str) -> str:
    newState = io.BytesIO(state.encode('utf-8'))
    md5 = hashlib.md5()

    md5.update(newState.getvalue())
    return md5.hexdigest()



# write a program in python to generate hashes of string data using three algo. from
# the hashlib dir
def newHash(word):
    hashesOfGivenWord = []
    for idx in range(0, 3):
        if idx == 0:
            hashedWord = hashlib.sha512(word.encode())
            hashesOfGivenWord.append(hashedWord.hexdigest())
        elif idx % 2 == 0:
            hashedWord = hashlib.sha384(word.encode())
            hashesOfGivenWord.append(hashedWord.hexdigest())
        else:
            hashedWord = hashlib.sha256(word.encode())
            hashesOfGivenWord.append(hashedWord.hexdigest())
    return hashesOfGivenWord


# salting the given word with !@#$%^&*()~_-+=|\}{[]":'"';?/><,., using sha512 algorithm by 1000000 times of iterations
def salt(word):
    hashedWord = hashlib.pbkdf2_hmac('sha512', word.encode(), b"""!@#$%^&*()~_-+=|\}{[]":'"';?/><,.""", 1000000)
    return binascii.hexlify(hashedWord).decode()


if __name__ == '__main__':
    wordForHashing = input("enter value to get md5 hash : ")
    print (hash(wordForHashing))

    print('Hash using other algorithms of hashlib module')
    for hash in newHash(wordForHashing):
        print(hash)

    print("Hashed word after 1000000 times of iteration using sha512 algorithm :" + str(salt(wordForHashing)))
    