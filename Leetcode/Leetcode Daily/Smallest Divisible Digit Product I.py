class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digit_product(x):
            product = 1
            while x > 0:
                digit = x % 10
                product *= digit
                x //= 10
            return product

        while True:
            # Calculate the product of digits for the current number `n`
            product = digit_product(n)
            
            # Check if the product is divisible by `t`
            if product % t == 0:
                return n  # Return `n` if condition is satisfied
            
            # Increment `n` if condition is not met
            n += 1
        