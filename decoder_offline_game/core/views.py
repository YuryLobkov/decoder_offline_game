from django.shortcuts import render
from .models import Word

def homepage_view(request):
    random_words_team1 = Word.get_words_set(num_teams=1, words_per_team=4)
    random_words_team2 = Word.get_words_set(num_teams=1, words_per_team=4)
    return render(request, 'core/index.html', {'team1words': random_words_team1, 'team2words': random_words_team2})