from home.models import Student

def test_function():
    print("this is a test function")

## this is a test file to test Django Shell

'''

    >>> from home.models import *
    >>> student = Student(name="Suvam", age=26, email="iam@suv.am")
    >>> student
    <Student: Student object (None)>
    >>> student.save()
    >>> student
    <Student: Student object (1)>
    >>> student = Student.objects.create(name="annupama", age=27, email="anu@gmail.com")
    >>> student
    <Student: Student object (2)>
    >>> Student.objects.all()
    <QuerySet [<Student: Student object (1)>, <Student: Student object (2)>]>
    >>> Student.objects.all()[0].name
    'Suvam'
    >>> Student.objects.all()[0].age
    26
    >>> Student.objects.all()[1].name
    'annupama'
    >>> Student.objects.all()[1].age
    27
    >>> from home.utils import *
    >>> test_function()
    this is a test function
    >>>

'''