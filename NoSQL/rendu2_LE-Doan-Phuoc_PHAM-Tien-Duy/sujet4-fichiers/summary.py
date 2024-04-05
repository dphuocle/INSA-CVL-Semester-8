from collections import defaultdict, Counter

# Initialize a default dictionary to store followee (user) and their follower count
followers_count = defaultdict(int)

# Simulate the mapper output
with open("higgs-social_network.edgelist", "r") as file:
    for line in file:
        followee, _ = line.strip().split()
        followers_count[followee] += 1

# Now we'll simulate the reducer
total_followers = 0
max_followers = 0
min_followers = float('inf')
max_user = min_user = None

# Counter for more efficient calculation
followers_counter = Counter(followers_count)

for user, count in followers_counter.items():
    # Update the total followers
    total_followers += count
    
    # Check and update the maximum followers
    if count > max_followers:
        max_followers = count
        max_user = user
    
    # Check and update the minimum followers
    if count < min_followers:
        min_followers = count
        min_user = user

# Print the aggregate results
print(f"nb_users  {len(followers_counter)}")
print(f"sum    {total_followers}")
print(f"min    {min_followers};{min_user}")
print(f"max    {max_followers};{max_user}")
