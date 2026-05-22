class Solution:

    def encode(self, strs: List[str]) -> str:
        secret = '🥺'
        encoded_string = ''

        for st in strs:
            encoded_string += st
            encoded_string += secret
        
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = s.split('🥺')
        return decoded_strs[0:-1]