from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    peoples = [
        {
            'name': 'suvam',
            'age': 21
        },
        {
            'name': 'anupama',
            'age': 27
        },
        {
            'name': 'akash',
            'age': 13
        }
    ]

    text =  """
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam nec egestas nisi, ac gravida turpis. Mauris sollicitudin tortor vel ante ultricies auctor. Integer finibus dui ac erat imperdiet, quis auctor quam tempus. Mauris vestibulum risus vitae dui laoreet, scelerisque suscipit ipsum porta. Pellentesque pretium sed tortor vitae tristique. Duis ac odio orci. Quisque porttitor tellus feugiat libero facilisis varius. Pellentesque quis nisi erat. Nulla commodo, neque ac pharetra egestas, metus magna ultrices sem, quis rutrum ipsum dolor sed neque. Nunc odio elit, bibendum sit amet finibus vel, pharetra a nisi. Praesent quis condimentum lacus. Ut massa ipsum, imperdiet in interdum at, auctor non ante. Quisque massa orci, mollis nec nibh sed, placerat egestas nisi. Ut suscipit id tortor et semper. Vivamus efficitur molestie sem, in venenatis diam. Aenean id odio nec erat ultrices interdum. Ut eleifend metus ac lectus sollicitudin, et malesuada odio facilisis. Etiam interdum ligula a semper elementum. In vitae orci quis nunc vehicula tincidunt. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec hendrerit orci felis, in viverra dui luctus non. Pellentesque dapibus nisi non tincidunt lobortis. Morbi posuere arcu tellus, a vulputate enim imperdiet in. In eget fringilla nisi. Pellentesque consectetur congue mauris nec interdum. Vestibulum ac rutrum libero. Sed nec ipsum sapien. Curabitur scelerisque ex erat, efficitur auctor lorem euismod eget. Maecenas vehicula velit venenatis enim interdum dictum. Duis id cursus arcu, eu tristique massa. Duis quis convallis eros. Suspendisse malesuada vehicula eros id tincidunt. Donec vulputate mauris quis sapien fringilla facilisis. Nulla a egestas erat. Quisque eu velit id nisl luctus sodales. Aliquam volutpat neque augue, eu dignissim orci vestibulum ut. In placerat mauris lorem. Pellentesque sed efficitur elit, sit amet tristique est. Donec et justo quam. Etiam tempus mauris quis odio hendrerit tristique.
            """
    
    vegetables = ['pumpkin', 'tomato', 'potato', 'cucumber']

    # context helps sending data from backend to frontend in django
    return render(req, 'home/index.html', context={'peoples': peoples, 'text': text, 'vegetables': vegetables, 'page': "Home - Django Learning"})

def success_page(req):
    return HttpResponse("This is a success page")

def contact(req):
    context = {'page': 'Contact'}
    return render(req, 'home/contact.html', context)

def about(req):
    context = {'page': 'About'}
    return render(req, 'home/about.html', context)