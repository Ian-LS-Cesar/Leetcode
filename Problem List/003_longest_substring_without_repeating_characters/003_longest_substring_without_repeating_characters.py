class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ultima_vez = {}
        esquerda = 0
        melhor = 0

        for indice, letra in enumerate(s):
            if letra in ultima_vez and ultima_vez[letra] >= esquerda:
                esquerda = ultima_vez[letra] + 1

            ultima_vez[letra] = indice
            melhor = max(melhor, indice - esquerda + 1)

        return melhor