score_1 = int(input())
score_2 = int(input())

sum_of_scores = score_1 + score_2

is_one_score_greater = (score_1 > 300) or (score_2 > 300)

is_sum_less = sum_of_scores < 500

can_team_up = is_one_score_greater and is_sum_less

if can_team_up:
    print("Can team up")
else:
    print("Cannot team up")