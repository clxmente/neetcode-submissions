class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # do we have a need for implementing a queue?
        # could gather the count of prefs and decrement as we iterate the sandwiches array

        preferences = {}
        for n in students:
            preferences[n] = 1 + preferences.get(n, 0)


        for n in sandwiches:
            if preferences.get(n, 0) > 0:
                preferences[n] = preferences[n] - 1
            else:
                break
        
        # sum up all the remaining students
        remaining = 0
        for num_of_students in preferences.values():
            remaining += num_of_students

        return remaining
