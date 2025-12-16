"""
Sum at even and odd positions 
"""

def sumAtEvenOddPositions(n):
    
    s = str(n)
    even_sum = 0
    odd_sum = 0

    for pos in range(len(s)):
        digit = int(s[len(s)-1-pos])
        if (pos + 1)%2 == 0:  # Position starts from 1 rightmost digit is at the position 1
            even_sum += digit
        else:
            odd_sum += digit
    return even_sum, odd_sum
n = int(input())
even, odd = sumAtEvenOddPositions(n)
print(even)
print(odd)

