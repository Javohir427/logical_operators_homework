def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (9999<a<100000 and a%10<a%100//10<a//100%10<a//1000%10<a//10000)

print(main(57321))