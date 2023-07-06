import find_path

def calculate_likelihood(routes, transitions, probabilities, observations):
    likelihood = 0.0
    for n, transition in zip(range(len(transitions)), transitions):
        transition_probability = 1.0
        print(f"P {n+1}:", end=" ")
        for i in range(len(transition)):
            transition_probability *= (
                probabilities[routes[transition[i]]][0]
                * probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]
            )
            if i != len(transition) - 1:
                print(
                    f"{probabilities[routes[transition[i]]][0]} × {probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]}",
                    end=" × ",
                )
            else:
                print(
                    f"{probabilities[routes[transition[i]]][0]} × {probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]}",
                    end="",
                )
        likelihood += transition_probability
        print(f" = {round(transition_probability, 5)}")
    print(f"P({observations} | M) = {round(likelihood, 5)}")

    return likelihood


routes = {
    "1->1": 0,
    "1->2": 1,
    "1->3": 2,
    "2->2": 3,
    "2->3": 4,
    "2->4": 5,
    "3->3": 6,
    "3->4": 7,
    "3->5": 8,
    "4->4": 9,
    "4->5": 10,
    "5->5": 11,
}

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

def convert_observation(seq):
    converted_list = []
    for char in seq:
        if char == 'g':
            converted_list.append(1)
        elif char == 'f':
            converted_list.append(0)
    return converted_list

if __name__ == "__main__":
    sequential_progression = input("input sequential progression >> ")
    start_node = "1"
    end_node = "5"
    steps = len(sequential_progression)
    graph = {
        "1": ["1", "2", "3"],
        "2": ["2", "3", "4"],
        "3": ["3", "4", "5"],
        "4": ["4", "5"],
        "5": ["5"],
    }
    paths = find_path.find_paths(graph, start_node, end_node, steps)
    transitions = find_path.translate_transitions(paths)
    observations = convert_observation(sequential_progression)

    beatlesProb = calculate_likelihood(routes, transitions, beatlesDictionary, observations)
    rollingstonesProb = calculate_likelihood(routes, transitions, rollingstonesDictionary, observations)
    if beatlesProb > rollingstonesProb:
        print("ビートルズの楽曲が妥当")
    elif rollingstonesProb > beatlesProb:
        print("ローリングストーンズの楽曲が妥当")
    else:
        print("どちらとも言えない")
