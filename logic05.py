def main(a,b):
    """
    ven two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return (a%2==1 and b%2==1)

print(main(9,1))