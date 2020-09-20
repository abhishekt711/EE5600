def event_probability(event_outcomes, sample_space):
    probability = (event_outcomes / sample_space) 
    return round(probability, 2)


# Sample Space
number_of_toss = 500

# Outcomes
two_heads = 105
one_head = 275
no_head = 120

# Divide possible outcomes by the sample set
probability_two_heads = event_probability(two_heads, number_of_toss)
probability_one_head = event_probability(one_head, number_of_toss)
probability_no_head = event_probability(no_head, number_of_toss)

# Print probability rounded to two decimal places
print("Probability of Two Heads = ",round(probability_two_heads, 2))
print("Probability of One Head = ",round(probability_one_head, 2))
print("Probability of No Head = ",round(probability_no_head, 2))
