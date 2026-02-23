from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Score

def calculate_handicap(scores):
    if len(scores) < 3:
        return None
    
    differentials = sorted(
        score.score_differential() for score in scores)