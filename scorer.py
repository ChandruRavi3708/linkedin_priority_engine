import heapq
import numpy as np

qualification_scores = {
    "PhD": 100,
    "M.Tech": 80,
    "B.Tech": 60
}

class Candidate:
    def __init__(self, data, required_skills):
        self.name = data["name"]
        self.qualification = data["qualification"]
        self.experience = data["experience"]
        self.skills = data["skills"]
        self.score = self.calculate_score(required_skills)

    def calculate_score(self, required_skills):
        # Qualification score
        q_score = qualification_scores.get(self.qualification, 50)

        # Experience score
        exp_score = min(self.experience * 10, 100)

        # Skills score using NumPy
        matched = len(set(required_skills).intersection(set(self.skills)))
        skill_score = (matched / len(required_skills)) * 100 if required_skills else 0

        final_score = np.mean([
            0.3 * q_score,
            0.4 * exp_score,
            0.3 * skill_score
        ])

        return round(final_score, 2)

    def __lt__(self, other):
        return self.score > other.score


class PriorityEngine:
    def __init__(self):
        self.heap = []

    def rank_candidates(self, candidates, required_skills):
        self.heap = []

        for c in candidates:
            candidate = Candidate(c, required_skills)
            heapq.heappush(self.heap, candidate)

        result = []
        while self.heap:
            result.append(heapq.heappop(self.heap))

        return result