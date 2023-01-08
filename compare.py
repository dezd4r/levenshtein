import levenshtein
import ast
import argparse


if __name__ == '__main__':
    a = "short"
    b = "ports"
    print(levenshtein.levenshtein_algorithm(a, b))
