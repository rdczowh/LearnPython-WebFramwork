import hashlib
db = {}

def get_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')
def login(username, password):
    if(db.get(username)==get_md5(password + username + 'the-Salt')):
        print("Hello,%s,Login sucessful!" % username)
    else:
        print("username or password Error!")




if __name__=='__main__':
    register("a","123")
    register("b", "123")
    login("a","123")
    login("b", "123")
    login("a","456")
    login("b", "456")
    login("c", "456")