from django.db import models

class Base(models.Model):
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Course(Base):
    title = models.CharField(max_length=120)
    url = models.URLField(unique=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        
    def __str__(self):
        return self.title


class Assessment(Base):
    course = models.ForeignKey(Course, related_name='reviews', on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    email = models.EmailField()
    comment = models.TextField(blank=True, default='')
    assessment = models.DecimalField(max_digits=2, decimal_places=1)
    
    class Meta:
        verbose_name = 'Assessment'
        verbose_name_plural = 'AAssessments'
        unique_together = ['email', 'course']
        
    def __str__(self):
        return f'{self.name} avaliou o curso {self.course} com nota {self.assessment}'
    