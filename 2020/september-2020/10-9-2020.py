

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        length_secret = len(secret)
        length_guess = len(guess)
        if length_secret != length_guess:
            return "-1"
        secret_values = []
        guess_values = []
        bulls_count, cows_count = 0, 0
        curr = 0
        while curr < length_secret:
            if secret[curr] == guess[curr]:
                bulls_count += 1
            else:
                secret_values.append(secret[curr])
                guess_values.append(guess[curr])
            curr += 1
        guess_values.sort()
        secret_values.sort()
        curr_guess_index, curr_secret_index = 0, 0
        print(guess_values, secret_values)
        while curr_guess_index < len(guess_values) and curr_secret_index < len(secret_values):
            if guess_values[curr_guess_index] == secret_values[curr_secret_index]:
                cows_count += 1
                curr_secret_index += 1
                curr_guess_index += 1
            elif guess_values[curr_guess_index] < secret_values[curr_secret_index]:
                curr_guess_index += 1
            else:
                curr_secret_index += 1

        return '{bulls_count}A{cows_count}B'.format(bulls_count=bulls_count, cows_count=cows_count)

print(Solution().getHint("1807", "7810"))
