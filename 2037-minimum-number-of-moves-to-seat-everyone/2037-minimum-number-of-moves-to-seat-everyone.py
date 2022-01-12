class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats_sorted = sorted(seats)
        students_sorted=sorted(students)
        i=0
        j=0
        steps=0
        while j<len(students_sorted):
            if students_sorted[j]==seats_sorted[i]:
                i+=1
                j+=1
            else:
                steps+=abs(students_sorted[j]-seats_sorted[i])
                i+=1
                j+=1
        return steps
        