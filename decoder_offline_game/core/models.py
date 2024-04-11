import imp
from django.db import models
import random
# from django.core.validators import MinValueValidator, MaxValueValidator
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Word(models.Model):

    DIFFICULTY_CHOICES = [
        (1, 'Easy'),
        (2, 'Medium'),
        (3, 'Hard'),
    ]

    term = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    difficulty = models.IntegerField(choices=DIFFICULTY_CHOICES, null=True, blank=True)
    archive = models.BooleanField(default=False)
    played_counter = models.IntegerField(default=0)

    # default fields from dataset
    word_slice = models.CharField(max_length=30)
    word_answerA = models.CharField(max_length=30, null=True)
    word_probaA = models.DecimalField(max_digits=5, decimal_places=4)
    word_answerB = models.CharField(max_length=30, null=True)
    word_probaB = models.DecimalField(max_digits=5, decimal_places=4)
    word_hmAnswerA = models.CharField(max_length=30, null=True)
    word_hmAnswerb = models.CharField(max_length=30, null=True)
    word_hmRatio = models.DecimalField(max_digits=5, decimal_places=4)
    word_otherRatio = models.DecimalField(max_digits=5, decimal_places=4)

    @staticmethod
    def get_words_set(num_teams, words_per_team):
        num_words = num_teams * words_per_team
        words = Word.objects.filter(archive=False).values('word').distinct()
        if words.count() < num_words:
            raise Exception('Not enough unique words in the database.')
        words_set = random.sample(list(words), num_words)
        return [word['word'] for word in words_set]
    
    @staticmethod
    def get_word_and_increment_counter(word_id):
        word = Word.objects.get(id=word_id)
        word.played_counter += 1
        word.save()
        return word

#     ---------future update, words rating-------------
#     def update_rating(self):
#         votes = UserVote.objects.all()
#         total_votes = votes.count()
#         if total_votes > 0:
#             average_rating = sum(vote.vote for vote in votes) / total_votes
#             self.rating = round(average_rating, 1)
#             self.save()
# class UserVote(models.Model):
#     vote = models.DecimalField(max_digits=2, decimal_places=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
