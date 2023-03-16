class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.ttl = timeToLive
        self.map = {}


    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = currentTime + self.ttl

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId in self.map.keys() and self.map[tokenId] > currentTime:
            self.map[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        res = 0
        for map in self.map.values():
            if map > currentTime:
                res += 1
        return res



# Your AuthenticationManager object will be instantiated and called as such:


timeToLive = 5
obj = AuthenticationManager(timeToLive)
obj.renew("aaa", 1)
obj.generate("aaa", 2)
param_aaa = obj.countUnexpiredTokens(6)
obj.generate("bbb", 7)
obj.renew("aaa", 8)
obj.renew("bbb", 10)
param_3 = obj.countUnexpiredTokens(15)
print(param_3)