from django.views.generic import ListView

from .models import Student


class StudentsList(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'students'
    ordering = 'group'

    def get_queryset(self):
        return Student.objects.prefetch_related('teachers').order_by(self.ordering)
