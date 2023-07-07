import numpy as np
import csv

# 状態空間
states = ["1", "2", "3", "4", "5"]

# 各状態での観測可能な結果
observations = ["f", "g"]

# スタート状態
start_probability = {"1": 1.0, "2": 0.0, "3": 0.0, "4": 0.0, "5": 0.0}

# 状態遷移確率（全ての可能な状態遷移組み合わせの確率）
transition_probability = {
    "1": {"1": 0.3, "2": 0.5, "3": 0.2},
    "2": {"2": 0.2, "3": 0.6, "4": 0.2},
    "3": {"3": 0.2, "4": 0.6, "5": 0.2},
    "4": {"4": 0.5, "5": 0.5},
    "5": {"5": 1.0},
}

# 出力確率（各状態での観測結果の確率）
emission_probability = {
    "1": {"f": 0.7, "g": 0.3},
    "2": {"f": 0.8, "g": 0.2},
    "3": {"f": 0.5, "g": 0.5},
    "4": {"f": 0.2, "g": 0.8},
    "5": {"f": 0.4, "g": 0.6},
}

def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # 初期状態を設定
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # Viterbi計算
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max(
                (V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0)
                for y0 in states
            )
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path[state])

if __name__ == "__main__":
    # シーケンスの入力
    sequence = "fgfgfg"

    # Viterbi algorithmを実行
    prob, path = viterbi(sequence, states, start_probability, transition_probability, emission_probability)

    # 結果を表示
    print(f"最終的なパス: {path}")
    print(f"確率: {prob}")
