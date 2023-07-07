import find_path
from itertools import product
import csv

def calculate_likelihood(routes, transitions, probabilities, observations):
    likelihood = 0.0
    for n, transition in zip(range(len(transitions)), transitions):
        transition_probability = 1.0
        for i in range(len(transition)):
            transition_probability *= (
                probabilities[routes[transition[i]]][0]
                * probabilities[routes[transition[i]]][1 if observations[i] == 1 else 2]
            )
            """
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
            """
        likelihood += transition_probability
        #print(f" = {round(transition_probability, 5)}")
    #print(f"P({observations} | M) = {round(likelihood, 5)}")

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

# [ループ, f, g]
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

def generate_combinations(characters, max_length):
    combinations = []
    for length in range(2, max_length + 1):
        for item in product(characters, repeat=length):
            combinations.append(''.join(item))
    return combinations


if __name__ == "__main__":
    #sequential_progression = input("input sequential progression >> ")
    start_node = "1"
    end_node = "5"
    characters = "fg"

    graph = {
        "1": ["1", "2", "3"],
        "2": ["2", "3", "4"],
        "3": ["3", "4", "5"],
        "4": ["4", "5"],
        "5": ["5"],
    }
    combinations = generate_combinations(characters, int(input("num >> ")))
    print(combinations)

    # Open CSV file for writing
    with open('output.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Write header
        writer.writerow(['文字列', 'beatlesの確率', 'rolling stonesの確率', '結果'])

        for combination in combinations:
            print(combination)
            sequential_progression = combination
            steps = len(sequential_progression)
            
            paths = find_path.find_paths(graph, start_node, end_node, steps)
            transitions = find_path.translate_transitions(paths)
            observations = convert_observation(sequential_progression)

            beatlesProb = calculate_likelihood(routes, transitions, beatlesDictionary, observations)
            rollingstonesProb = calculate_likelihood(routes, transitions, rollingstonesDictionary, observations)
            
            # Decide the result
            if beatlesProb > rollingstonesProb:
                result = "beatles"
            elif rollingstonesProb > beatlesProb:
                result = "rolling stones"
            else:
                result = "both"

            # Write to CSV file
            writer.writerow([sequential_progression, beatlesProb, rollingstonesProb, result])