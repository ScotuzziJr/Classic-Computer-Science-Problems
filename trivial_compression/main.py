# Compression algorithm to reduce the memory use to store DNA data using bitwise operations

class CompressedGene:
    def __init__(self, gene: str) -> None:
        self._compress(gene)

    def _compress(self, gene: str) -> None:
        self.bit_string: int = 1

        for nucleotide in gene.upper():
            self.bit_string <<= 2 # push 2 bits left

            if nucleotide == "A":
                self.bit_string |= 0b00
            elif nucleotide == "C":
                self.bit_string |= 0b01
            elif nucleotide == "G":
                self.bit_string |= 0b10
            elif nucleotide == "T":
                self.bit_string |= 0b11
            else:
                raise ValueError(f"Invalid Nucleotide {nucleotide}")

    def decompress(self) -> str:
        gene: str = ""

        for i in range(0, self.bit_string.bit_length() - 1, 2):
            bits: int = self.bit_string >> i & 0b11

            match bits:
                case 0b00:
                    gene += "A"
                case 0b01:
                    gene += "C"
                case 0b10:
                    gene += "G"
                case 0b11:
                    gene += "T"
                case _:
                    raise ValueError(f"Invalid bits: {bits}")
                
        return gene[::-1] # return the reversed string

    def __str__(self) -> str:
        return self.decompress()
    
if __name__ == "__main__":
    from sys import getsizeof

    original: str = "ATTGCTGGCAAAAGATCGTCGTCGAAAAATTGGCCCACACGTTCTGTAAGC" * 100
    print(f"Original string is {getsizeof(original)} bytes")

    compressed: CompressedGene = CompressedGene(original) # compress
    print(f"Compressed string is {getsizeof(compressed.bit_string)} bytes")

    print(compressed) # decompress

    print(f"Original string and decompressed string are the same: {original == compressed.decompress()}")
