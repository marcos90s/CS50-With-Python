import sys
# Candidates have name and vote count
class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

# Array of candidates
candidates = []

# Number of candidates
candidate_count = 0

MAX = 9

# Function to update vote totals given a new vote
def vote(name):
    global candidate_count
    for i in range(candidate_count):
        if candidates[i].name == name:
            candidates[i].votes += 1
            return True
    return False

# Function to print the winner (or winners) of the election
def print_winner():
    most_votes = 0
    winner = []
    for candidate in candidates:
        if candidate.votes > most_votes :
            if winner == None:
                most_votes = candidate.votes
                winner.append(candidate.name)
            else:
                most_votes = candidate.votes
                winner = []
                winner.append(candidate.name)
            
        elif candidate.votes == most_votes:
            winner.append(candidate.name)
    if len(winner) == 1:
        print('Winner:',winner[0])
    else: 
        print('\n'.join(winner))

def main():
    global candidate_count, candidates
    
    # Check for invalid usage
    if len(sys.argv) < 2:
        print("Usage: plurality [candidate ...]")
        return 1

    # Populate array of candidates
    candidate_count = len(sys.argv) - 1
    if candidate_count > MAX:
        print("Maximum number of candidates is", MAX)
        return 2
    for i in range(candidate_count):
        candidates.append(Candidate(sys.argv[i + 1]))

    voter_count = int(input("Number of voters: "))

    # Loop over all voters
    for _ in range(voter_count):
        name = input("Vote: ")

        # Check for invalid vote
        if not vote(name):
            print("Invalid vote.")

    # Display winner of election
    print_winner()

if __name__ == "__main__":
    main()
