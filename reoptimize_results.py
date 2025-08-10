"""Tool to compute again the optimal plays for a given file of results"""

import argparse
import json

from ballmatro.card import Card
from ballmatro.hands import InvalidPlay, NoPokerHand
from ballmatro.score import Score
from ballmatro.optimizer import brute_force_optimize


def main(dataset: str, output: str):
    """Run the optimizer over a dataset of results to find the optimal plays, and recompute statistics"""
    with open(dataset, "r") as f:
        json_data = json.load(f)

    for i, score_json in enumerate(json_data["scores"]):
        if isinstance(score_json["input"], str):  # Input was not formatted correctly
            continue
        if isinstance(score_json["played"], str):  # Input was not formatted correctly
            continue
        input = "[" + ",".join(score_json["input"]) + "]"
        played = "[" + ",".join(score_json["played"]) + "]"
        score = Score(input, played)
        if isinstance(score.hand, InvalidPlay):
            if score_json["hand"] != "Invalid Play":
                print(score)
            continue
        input = [Card(card) for card in score_json["input"]]
        score_json["remaining"] = [str(card) for card in score.remaining] if score.remaining else None
        score_json["hand"] = str(score.hand.name)
        score_json["chips"] = score.chips
        score_json["multiplier"] = score.multiplier
        score_json["score"] = score.score
        opt = brute_force_optimize(input)
        json_data["normalized_scores"][i] = score.score / opt.score

    # Compute statistics
    json_data["total_score"] = sum(score["score"] for score in json_data["scores"])
    json_data["total_normalized_score"] = sum(json_data["normalized_scores"]) / len(json_data["normalized_scores"])
    json_data["invalid_hands"] = sum(1 for score in json_data["scores"] if score["hand"] in ["No Poker Hand", "Invalid Play"])
    json_data["normalized_invalid_hands"] = json_data["invalid_hands"] / len(json_data["scores"])

    # Save the results
    with open(output, "w") as f:
        json.dump(json_data, f, indent=4)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the optimizer over a dataset of results to find the optimal plays, and recompute statistics")
    parser.add_argument("dataset", type=str, help="Name of the results file to process.")
    parser.add_argument("output", type=str, help="File to save the processed results")
    args = parser.parse_args()
    main(args.dataset, args.output)
