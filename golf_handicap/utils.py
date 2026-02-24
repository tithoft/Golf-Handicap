from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Score

def calculate_handicap(scores):
    if len(scores) < 3:
        return None
    
    differentials = sorted(
        score.score_differential() for score in scores)

    lowest = differentials[:min(8, len(differentials))]
    avg = sum(lowest) / len(lowest)

    return round(float(avg) * 0.96, 1)