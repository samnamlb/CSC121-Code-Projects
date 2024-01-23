#
# Aleem Azimov
# September 24, 2022
# Create nested lists
#
g_list = []
t_list = []
s_list = []


def main():
    # Step a
    print("Please enter Gerald's scores one by one.")
    for i in range(4):
        score = float(input("Enter a score: "))
        g_list.append(score)
    print(f"Gerald's scores: {g_list}\n")

    # Step b
    print("Please enter Tammy's scores one by one.")
    for i in range(4):
        score = float(input("Enter a score: "))
        t_list.append(score)
    print(f"Tammy's scores: {t_list}\n")

    # Step c
    print("Please enter Sumi's scores one by one.")
    for i in range(4):
        score = float(input("Enter a score: "))
        s_list.append(score)
    print(f"Sumi's scores: {s_list}\n")

    # Step d
    all_scores = [g_list[:], t_list[:], s_list[:]]
    print(f"All scores: {all_scores}")

    # Step e
    for name in range(3):
        for i in range(4):
            all_scores[name][i] += 4
    print(f"All scores after extra point: {all_scores}")

    # Step f
    avg_scores = []
    for i in range(3):
        average = sum(all_scores[i]) / len(all_scores[i])
        avg_scores.append(average)
    print(f"Average scores: {avg_scores}\n")

    # Step g
    print("Original Scores")
    print(f"Gerald's scores: {g_list}")
    print(f"Tammy's scores: {t_list}")
    print(f"Sumi's scores: {s_list}")


main()
