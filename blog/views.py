from django.shortcuts import render

def blog_list(request):
    posts = [
        {
            'title': 'How to Master Organic Chemistry',
            'date': 'Feb 11, 2024',
            'excerpt': 'Mastering molecular structures doesn\'t have to be a nightmare. Here are 5 tips...',
            'category': 'Study Tips'
        },
        {
            'title': 'Top 10 Engineering Tools for 2024',
            'date': 'Feb 09, 2024',
            'excerpt': 'From drafting sets to specialized software, stay ahead in your engineering degree.',
            'category': 'Academic News'
        }
    ]
    return render(request, 'blog/list.html', {'posts': posts})
