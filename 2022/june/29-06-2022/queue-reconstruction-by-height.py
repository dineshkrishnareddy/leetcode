class Solution:
    def reconstructQueue(self, people):
        if len(people) <= 1:
            return people

        people = sorted(people, key=lambda x: (-x[0], x[1]))

        for cur in range(len(people)):
            h, k = people[cur]

            if k < cur:
                p = people.pop(cur)
                people.insert(k, p)

        return people


print(Solution().reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
