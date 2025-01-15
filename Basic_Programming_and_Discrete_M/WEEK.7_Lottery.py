from math import comb

def main():
    print("Welcome to the Lottery Probability Calculator!")
    
    # Get inputs
    n = int(input("Enter the total number of possible numbers (n): "))
    k = int(input("Enter the number of numbers the player bets on (k): "))
    
    if k > n or k < 1:
        print("Invalid input: k must be between 1 and n.")
        return
    
    # Calculate the total number of possible combinations
    total_combinations = comb(n, k)
    
    # Calculation of probability of winning big
    big_win_probability = 1 / total_combinations  # Player hits all k numbers
    
    # Calculate the probability of winning little
    # Player hits (k-1) numbers
    combinations_hit_k_minus_1 = comb(k, k-1)  # Ways to choose (k-1) numbers out of player's k
    combinations_miss_one = comb(n-k, 1)      # Ways to choose 1 number from the remaining (n-k)
    little_win_probability = (combinations_hit_k_minus_1 * combinations_miss_one) / total_combinations
    
    # Results 
    print("\n--- Lottery Probabilities ---")
    print(f"Probability of winning big (hitting all {k} numbers): {big_win_probability:.8f}")
    print(f"Probability of winning little (hitting {k-1} numbers): {little_win_probability:.8f}")

if __name__ == "__main__":
    main()
