"""
statistics.py

Responsável pelos cálculos do Dashboard.
"""

from collections import Counter

class StatisticsService:
    
    @staticmethod
    def total_stars(repositories):
        
        total =  0 
        
        for repo in repositories:
            total += repo["forks_count"]
                          
        return total      
    
    @staticmethod
    def total_repositories(repositories):
        
        return len(repositories)
    
    @staticmethod
    def languages(repositories):

        languages = []

        for repo in repositories:

            if repo["language"] is not None:
                languages.append(repo["language"])

        return Counter(languages)

    @staticmethod
    def most_used_language(repositories):

        counter = StatisticsService.languages(repositories)

        if len(counter) == 0:
            return "Nenhuma"

        return counter.most_common(1)[0][0]
    
    @staticmethod
    def most_starred_repository(repositories):

        if not repositories:
            return None

        return max(
            repositories,
            key=lambda repo: repo["stargazers_count"]
        )
    @staticmethod
    def most_forked_repository(repositories):

        if not repositories:
            return None

        return max(
            repositories,
            key=lambda repo: repo["forks_count"]
        )
    @staticmethod
    def newest_repository(repositories):

        if not repositories:
            return None

        return max(
            repositories,
            key=lambda repo: repo["created_at"]
        )
    @staticmethod
    def last_updated_repository(repositories):

        if not repositories:
            return None

        return max(
            repositories,
            key=lambda repo: repo["updated_at"]
        )    
    