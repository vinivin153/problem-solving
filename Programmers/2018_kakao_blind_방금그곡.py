def replaceHash(s):
    return (
        s.replace("C#", "1")
        .replace("D#", "2")
        .replace("F#", "3")
        .replace("G#", "4")
        .replace("A#", "5")
    )


def playtime(start, end):
    s1, e1 = map(int, start.split(":"))
    s2, e2 = map(int, end.split(":"))

    return (s2 * 60 + e2) - (s1 * 60 + e1)


def solution(m, musicinfos):
    answer = []
    m = replaceHash(m)
    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(",")
        melody = replaceHash(melody)

        pt = playtime(start, end)
        q = pt // len(melody)
        r = pt % len(melody)
        listened = melody * min(q, len(m) // len(melody) + 1) + melody[:r]

        if m in listened:
            answer.append([title, pt])

    if answer:
        return max(answer, key=lambda x: x[1])[0]
    else:
        return "(None)"
