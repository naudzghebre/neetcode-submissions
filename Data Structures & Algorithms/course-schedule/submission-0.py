class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 1. Build adjacency list (course -> list of prerequisites)
        adj = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            adj[course].append(prereq)
            
        # 0 = Unvisited, 1 = Visiting, 2 = Visited
        state = [0] * numCourses

        def hasCycle(course):
            if state[course] == 1:
                return True   # Cycle detected!
            if state[course] == 2:
                return False  # Already checked and safe

            # Mark as currently visiting
            state[course] = 1

            for prereq in adj[course]:
                if hasCycle(prereq):
                    return True

            # Mark as fully processed & safe
            state[course] = 2
            return False

        # Check every course (handles disconnected graphs)
        for c in range(numCourses):
            if hasCycle(c):
                return False  # Found a cycle, impossible to finish
                
        return True