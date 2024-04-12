from django.shortcuts import render
from .models import Word

def homepage_view(request):
    random_words = Word.get_words_set(num_teams=2, words_per_team=4)
    return render(request, 'core/index.html', {'words': random_words})