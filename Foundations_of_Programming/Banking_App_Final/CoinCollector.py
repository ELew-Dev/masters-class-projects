class CoinCollector:
    
    @staticmethod
    def parse_change(coins):
        """Converts a string of coins into cents."""
        coin_values = {
            'P': 1,   # Penny
            'N': 5,   # Nickel
            'D': 10,  # Dime
            'Q': 25,  # Quarter
            'H': 50,  # Half-dollar
            'W': 100  # Whole dollar
        }
        
        total_cents = 0
        for coin in coins:
            if coin in coin_values:
                total_cents += coin_values[coin]
            else:
                print(f"Invalid coin: {coin}")
        
        return total_cents
