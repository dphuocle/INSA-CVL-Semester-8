import numpy as np
import time
import matplotlib.pyplot as plt

# Define constants
NUM_RUNS = 1
NUM_STEPS = int(1e6)
EPSILON = 0.1

# Define the bandit with K arms
K = 10
true_rewards = np.random.rand(K)

# Define algorithms
def epsilon_greedy(Q, N):
    if np.random.rand() < EPSILON:
        return np.random.randint(K)
    else:
        return np.argmax(Q)

def epsilon_greedy_decaying(Q, N, t):
    epsilon_t = 1 / np.log(t*t)
    if np.random.rand() < epsilon_t:
        return np.random.randint(K)
    else:
        return np.argmax(Q)

def UCB(Q, N, t):
    confidence = np.sqrt(2 * np.log(t) / N)
    return np.argmax(Q + confidence)

def random_choice(Q, N):
    return np.random.randint(K)

# Scenario 1: UCB outperforms other algorithms
true_rewards_scenario1 = np.array([0.9] * 1 + [0.1] * (K - 1))  # Higher rewards closer to 1 to favor UCB

# Scenario 2: All algorithms perform similarly or ε-greedy algorithms are slightly better
true_rewards_scenario2 = np.array([0.5] * 9 + [0.45] * (K - 9))  # More uniform rewards to favor ε-greedy

# Fix the function definition by adding the missing part and completing the plotting within the function
def run_simulation_for_scenario(true_rewards):
    # Initialize performance metrics for the scenario
    cumulative_rewards_scenario = {
        'UCB': np.zeros(NUM_STEPS),
        'epsilon_greedy_dec': np.zeros(NUM_STEPS),
        'epsilon_greedy': np.zeros(NUM_STEPS),
        'random': np.zeros(NUM_STEPS)
    }
    execution_time_scenario = {
        'UCB': np.zeros(NUM_STEPS),
        'epsilon_greedy_dec': np.zeros(NUM_STEPS),
        'epsilon_greedy': np.zeros(NUM_STEPS),
        'random': np.zeros(NUM_STEPS)
    }
    
    # Run the simulation
    for run in range(NUM_RUNS):
        Q_all = {name: np.zeros(K) for name in cumulative_rewards_scenario.keys()}
        N_all = {name: np.zeros(K) for name in cumulative_rewards_scenario.keys()}
        
        for algorithm in cumulative_rewards_scenario.keys():
            np.random.seed(run)
            Q_all[algorithm][:] = 0
            N_all[algorithm][:] = 0
            
            # Initial pull of each arm
            for arm in range(K):
                reward = np.random.binomial(1, true_rewards[arm])
                Q_all[algorithm][arm] = reward
                N_all[algorithm][arm] = 1

            total_reward = np.sum(Q_all[algorithm])
            cumulative_rewards_scenario[algorithm][0] += total_reward
            
            # Run the steps for each algorithm
            for t in range(1, NUM_STEPS):
                start_time = time.time()
                if algorithm == 'UCB':
                    chosen_arm = UCB(Q_all[algorithm], N_all[algorithm], t)
                elif algorithm == 'epsilon_greedy_dec':
                    chosen_arm = epsilon_greedy_decaying(Q_all[algorithm], N_all[algorithm], t)
                elif algorithm == 'epsilon_greedy':
                    chosen_arm = epsilon_greedy(Q_all[algorithm], N_all[algorithm])
                else:
                    chosen_arm = random_choice(Q_all[algorithm], N_all[algorithm])
                
                # Function Pull
                reward = np.random.binomial(1, true_rewards[chosen_arm])
                N_all[algorithm][chosen_arm] += 1
                Q_all[algorithm][chosen_arm] += (reward - Q_all[algorithm][chosen_arm]) / N_all[algorithm][chosen_arm]
                total_reward += reward

                cumulative_rewards_scenario[algorithm][t] += total_reward
                execution_time_scenario[algorithm][t] += time.time() - start_time

    # Averaging over runs
    for algorithm in cumulative_rewards_scenario.keys():
        cumulative_rewards_scenario[algorithm] /= NUM_RUNS
        execution_time_scenario[algorithm] = np.cumsum(execution_time_scenario[algorithm]) / NUM_RUNS
    
    return cumulative_rewards_scenario, execution_time_scenario

# Run the simulations for both scenarios
cumulative_rewards_scenario1, execution_time_scenario1 = run_simulation_for_scenario(true_rewards_scenario1)
cumulative_rewards_scenario2, execution_time_scenario2 = run_simulation_for_scenario(true_rewards_scenario2)

# Define marker styles for each algorithm
marker_styles = {
    'UCB': 's',  # Square marker for UCB
    'epsilon_greedy_dec': 'o',  # Circle marker for epsilon greedy with decaying epsilon
    'epsilon_greedy': '^',  # Triangle up marker for epsilon greedy
    'random': 'x'  # X marker for random choice
}

# Now let's define the plotting function and create the plots for both scenarios.
def plot_results_for_scenario(cumulative_rewards_scenario, execution_time_scenario, scenario_label):
    plt.figure(figsize=(12, 5))
    
    # Plotting cumulative reward for the scenario
    plt.subplot(1, 2, 1)
    for algorithm in cumulative_rewards_scenario.keys():
        x_values = []
        y_values = []
        for i in range(NUM_STEPS):
            x_values.append(i)
            y_values.append(cumulative_rewards_scenario[algorithm][i])
        x_values.append(NUM_STEPS)
        y_values.append(cumulative_rewards_scenario[algorithm][NUM_STEPS-1])
        plt.plot(x_values, y_values, label=algorithm, marker=marker_styles[algorithm], markevery=NUM_STEPS//10)
    plt.xlabel('Number of pulls')
    plt.ylabel('Cumulative reward')
    plt.legend()
    plt.title(f'Cumulative Reward vs Number of pulls ({scenario_label})')

    # Plotting execution time for the scenario
    plt.subplot(1, 2, 2)
    for algorithm in execution_time_scenario.keys():
        x_values = []
        y_values = []
        for i in range(NUM_STEPS):
            x_values.append(i)
            y_values.append(execution_time_scenario[algorithm][i])
        x_values.append(NUM_STEPS)
        y_values.append(execution_time_scenario[algorithm][NUM_STEPS-1])
        plt.plot(x_values, y_values, label=algorithm, marker=marker_styles[algorithm], markevery=NUM_STEPS//10)

    plt.xlabel('Number of pulls')
    plt.ylabel('Time in seconds')
    plt.legend()
    plt.title(f'Execution Time vs Number of pulls ({scenario_label})')
    plt.tight_layout()
    plt.show()

# Plot the results for scenario 1
plot_results_for_scenario(cumulative_rewards_scenario1, execution_time_scenario1, 'scenario1')

# Plot the results for scenario 2
plot_results_for_scenario(cumulative_rewards_scenario2, execution_time_scenario2, 'scenario2')