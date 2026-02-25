import heapq
import numpy as np

qualification_scores = {
    "PhD": 100,
    "M.Tech": 80,
    "B.Tech": 60
}


class Candidate:
    def __init__(self, data, required_skills, preferred_qualification):
        self.name = data["name"]
        self.qualification = data["qualification"]
        self.experience = data["experience"]
        self.skills = data["skills"]
        self.profile_link = data.get("profile_link", "#")
        self.score = self.calculate_score(required_skills, preferred_qualification)

    def calculate_score(self, required_skills, preferred_qualification):
        # Qualification score
        q_score = qualification_scores.get(self.qualification, 50)

        # Bonus for preferred qualification
        if preferred_qualification and self.qualification == preferred_qualification:
            q_score += 20

        # Experience score
        exp_score = min(self.experience * 10, 100)

        # Skills score
        if required_skills:
            matched = len(set(required_skills).intersection(set(self.skills)))
            skill_score = (matched / len(required_skills)) * 100
        else:
            skill_score = 0

        # Proper weighted sum
        final_score = (
            0.3 * q_score +
            0.4 * exp_score +
            0.3 * skill_score
        )

        return round(final_score, 2)

    # Max heap behavior
    def __lt__(self, other):
        return self.score > other.score


class PriorityEngine:
    def __init__(self):
        self.heap = []

    def rank_candidates(self, candidates, required_skills, min_exp, preferred_qualification):
        self.heap = []

        for c in candidates:
            # Filter by minimum experience
            if c["experience"] < min_exp:
                continue

            candidate = Candidate(
                c,
                required_skills,
                preferred_qualification
            )

            heapq.heappush(self.heap, candidate)

        result = []
        while self.heap:
            result.append(heapq.heappop(self.heap))

        return result