inp = open("input.txt").read().split("\n\n")
AQ = [x.split("\n") for x in inp]

# Part 1 -> total amount of questions answered 'yes'
Q = [set(x) for x in [''.join(q) for q in AQ]]
p1 = [len(x) for x in Q]
print(f"Part 1: {sum(p1)}")

# Part 2 -> total amount of times a question was answered 'yes'
# by all members in the group
# Since the list of questions per group (AQ) and 
# unique answered questions (Q) are in the same order,
# can just compare using to index
# I.E. -> ['ab', 'a', 'ac'] and set('a', 'b', 'c') => 1
# since each group member answered 'yes' to 'a'
tlt = 0
for i, q in enumerate(AQ):
    for x in Q[i]:
        if all(x in n for n in q):
            tlt+=1
print(tlt)