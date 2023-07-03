def calculate_likelihood(routes, transitions, probabilities, observations):
    likelihood = 0.0
    for n,transition in zip(range(len(transitions)),transitions):
        transition_probability = 1.0
        print(f"P {n+1}:", end=" ")
        for i in range(len(transition)):
            transition_probability *= probabilities[routes[transition[i]]][0] * probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]
            if i != len(transition) - 1:
                print(f"{probabilities[routes[transition[i]]][0]} × {probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]}", end=" × ")
            else:
                print(f"{probabilities[routes[transition[i]]][0]} × {probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]}", end="")
        likelihood += transition_probability
        print(f" = {round(transition_probability, 5)}")
    print(f"P({observations} | M) = {round(likelihood, 5)}")

    return likelihood

routes = {
    "q1->q1": 0,
    "q1->q2": 1,
    "q1->q3": 2,
    "q2->q2": 3,
    "q2->q3": 4,
    "q2->q4": 5,
    "q3->q3": 6,
    "q3->q4": 7,
    "q3->q5": 8,
    "q4->q4": 9,
    "q4->q5": 10,
    "q5->q5": 11,
}

transitions = [
    ["q1->q1", "q1->q3", "q3->q5"],
    ["q1->q2", "q2->q3", "q3->q5"],
    ["q1->q2", "q2->q4", "q4->q5"],
    ["q1->q3", "q3->q3", "q3->q5"],
    ["q1->q3", "q3->q4", "q4->q5"],
    ["q1->q3", "q3->q5", "q5->q5"],
]

"""
exampleDictionary = {
    0: [0.3, 0.7, 0.3],
    1: [0.5, 0.8, 0.2],
    2: [0.2, 0.5, 0.5],
    3: [0.2, 0.2, 0.8],
    4: [0.6, 0.4, 0.6],
    5: [0.2, 0.3, 0.7],
    6: [0.4, 0.9, 0.1],
    7: [0.3, 0.6, 0.4],
    8: [0.3, 0.6, 0.4],
    9: [0.5, 0.2, 0.8],
    10: [0.5, 0.4, 0.6],
    11: [1.0, 0.1, 0.9],
}
"""

beatlesDictionary = {
    0: [0.3, 0.7, 0.3],
    1: [0.5, 0.8, 0.2],
    2: [0.2, 0.5, 0.5],
    3: [0.2, 0.2, 0.8],
    4: [0.6, 0.4, 0.6],
    5: [0.2, 0.3, 0.7],
    6: [0.2, 0.9, 0.1],
    7: [0.2, 0.6, 0.4],
    8: [0.6, 0.6, 0.4],
    9: [0.5, 0.2, 0.8],
    10: [0.5, 0.4, 0.6],
    11: [1.0, 0.8, 0.2],
}

rollingstonesDictionary = {
    0: [0.1, 0.6, 0.4],
    1: [0.5, 0.3, 0.7],
    2: [0.4, 0.5, 0.5],
    3: [0.1, 0.2, 0.8],
    4: [0.6, 0.7, 0.3],
    5: [0.3, 0.5, 0.5],
    6: [0.4, 0.4, 0.6],
    7: [0.2, 0.6, 0.4],
    8: [0.4, 0.4, 0.6],
    9: [0.2, 0.7, 0.3],
    10: [0.8, 0.3, 0.7],
    11: [1.0, 0.2, 0.8],
}

observations = [1, 0, 1]  # G-F-G

beatlesProb = calculate_likelihood(routes, transitions, beatlesDictionary, observations)
rollingstonesProb = calculate_likelihood(routes, transitions, rollingstonesDictionary, observations)

if beatlesProb > rollingstonesProb:
    print("ビートルズの楽曲が妥当")
elif rollingstonesProb > beatlesProb:
    print("ローリングストーンズの楽曲が妥当")
else:
    print("どちらとも言えない")