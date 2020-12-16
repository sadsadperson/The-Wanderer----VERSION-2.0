from replit import db
def save(data):
    name = data['name']
    db[name] = data
def restore(name):
    return db[name]
def does_user_exist(user):
    try:
        name = db[user]
        return True
    except:
        return False
def set_skill(skill):
    if skill == '1':
        return 'Swordsmen'
    elif skill == '2':
        return 'Archer'
    elif skill == '3':
        return 'Healer'
    elif skill == '4':
        return 'Thorgslayer'
    elif skill == '5':
        return 'Thug'
    elif skill == '6':
        return 'Spearmen'
    elif skill == '7':
        return 'Specialist'
    else:
        print("ERROR!")
        exit()
