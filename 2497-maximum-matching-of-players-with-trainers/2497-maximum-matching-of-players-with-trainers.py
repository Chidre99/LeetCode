class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        i ,j = 0,0
        players.sort()
        trainers.sort()
        while j < len(trainers) and i < len(players):
            if players[i] <= trainers[j]:
                i +=1
            j+=1
        return i