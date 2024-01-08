ENTER = "님이 들어왔습니다."
LEAVE = "님이 나갔습니다."


def solution(record):
    chat = []
    names = {}

    for r in record:
        k = r.split()
        command = k[0]
        uid = k[1]

        if command == "Leave":
            chat.append((uid, LEAVE))
        else:
            name = k[2]
            names[uid] = name
            if command == "Enter":
                chat.append((uid, ENTER))

    return [names[uid] + msg for uid, msg in chat]
