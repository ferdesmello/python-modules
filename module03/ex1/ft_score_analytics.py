import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    score_list: list[int] = []
    if len(sys.argv) > 1:
        for arg in (sys.argv[1:]):
            try:
                score_list.append(int(arg))
            except ValueError:
                print(f"Invalid parameter: '{arg}'")
        if score_list:
            print(f"Scores processed: {score_list}")
            print(f"Total players: {len(score_list)}")
            print(f"Total score: {sum(score_list)}")
            print(f"Average score: {sum(score_list) / len(score_list)}")
            print(f"High score: {max(score_list)}")
            print(f"Low score: {min(score_list)}")
            print(f"Score range: {max(score_list) - min(score_list)}")
        else:
            print("No scores provided. Usage: "
                  "python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("No scores provided. Usage: "
              "python3 ft_score_analytics.py <score1> <score2> ...")


if __name__ == "__main__":
    main()
