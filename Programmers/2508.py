def solution(skill, skill_trees):
    answer = 0
    n = len(skill)
    for skill_tree in skill_trees:
        k = 0
        for i in range(len(skill_tree)):
            if skill_tree[i] in skill:
                if skill_tree[i] == skill[k]:
                    k += 1
                else:
                    break
        else:
            answer += 1

    return answer
