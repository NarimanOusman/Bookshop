from django.shortcuts import render

def blog_list(request):
    posts = [
        {
            'title': 'How to Master Organic Chemistry',
            'date': 'Feb 11, 2024',
            'excerpt': 'Mastering molecular structures doesn\'t have to be a nightmare. Here are 5 tips for visualizing bonds and reactions.',
            'category': 'Study Tips',
            'image': 'https://images.unsplash.com/photo-1532187875605-7fe3b276709b?auto=format&fit=crop&q=80&w=800'
        },
        {
            'title': 'Top 10 Engineering Tools for 2024',
            'date': 'Feb 09, 2024',
            'excerpt': 'From high-precision drafting sets to specialized simulation software, stay ahead in your engineering degree.',
            'category': 'Academic News',
            'image': 'https://images.unsplash.com/photo-1503387762-592dee58c460?auto=format&fit=crop&q=80&w=800'
        },
        {
            'title': 'Effective Exam Preparation Strategies',
            'date': 'Feb 05, 2024',
            'excerpt': 'Discover the science-backed methods for retaining complex information and staying calm during finals week.',
            'category': 'Student Life',
            'image': 'https://images.unsplash.com/photo-1434030216411-0b793f4b4173?auto=format&fit=crop&q=80&w=800'
        },
        {
            'title': 'The Future of Academic Research',
            'date': 'Feb 01, 2024',
            'excerpt': 'How digital libraries and AI-driven literature reviews are changing the landscape of graduate research.',
            'category': 'Innovation',
            'image': 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=800'
        }
    ]
    return render(request, 'blog/list.html', {'posts': posts})
