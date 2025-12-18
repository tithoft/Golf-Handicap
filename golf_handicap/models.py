from django.db import models

class Course(models.Model):
    """Course user enters a score for."""
    course_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns string representation of the course name."""
        return self.course_name
    
class CourseTee(models.Model):
    """Course tee information about each course."""
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # Tee name is color (ex. Blue, White, Red)
    tee_name = models.CharField(max_length=200)
    course_rating = models.DecimalField(max_digits=4, decimal_places=1)
    slope_rating = models.IntegerField()
    course_par = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representing the tee."""
        return f"{self.course.course_name} - {self.tee_name}"
    
class Score(models.Model):
    """Score for each round."""
    tee = models.ForeignKey(CourseTee, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_played = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)

    def score_differential(self):
        """Calculates round differential using USGA rules. Differential used to calculate golfer's handicap."""
        return (((self.score - self.tee.course_rating) * 13) / self.tee.slope_rating)

    def __int__(self):
        """Returns a string representing the score."""
        return self.score