def build_petrinet(data):
    yl_transitions = set()
    for pair in data["yl"]:
        for p in pair:
            yl_transitions.add(p[0])

    appeared = data["ti"] | data["to"] | yl_transitions
    iso = data["tl"] - appeared

    petri_net = []
    petri_net.append("digraph petri_net {")
    petri_net.append("rankdir=LR;")
    for c in iso:
        petri_net.append('"{}" [shape=box];'.format(c))
    for pair in data["yl"]:
        for i in pair[0]:
            petri_net.append('"{}" -> "P({})";'.format(i, pair))
            petri_net.append('"{}" [shape=box];'.format(i))
            petri_net.append('"P({})" [shape=circle];'.format(pair))
        for i in pair[1]:
            petri_net.append('"P({})" -> "{}";'.format(pair, i))
            petri_net.append('"{}" [shape=box];'.format(i))
    for i in data["ti"]:
        petri_net.append("In -> {}".format(i))
    for o in data["to"]:
        petri_net.append("{} -> Out".format(o))
    petri_net.append("}")
    return '\n'.join(petri_net)

    # with open("result.dot", 'w') as f:
    #     f.write(result)

