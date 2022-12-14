def decimal_to_bin(decimal: int) -> str:
    bin = ''
    while decimal > 0:
        bin = str(decimal % 2) + bin
        decimal //= 2
    return bin


def bin_to_decimal(bin: str) -> int:
       decimal = 0
       for i in bin:
           decimal *= 2
           decimal += int(i)
       return decimal
print(bin_to_decimal(decimal_to_bin(12)))



