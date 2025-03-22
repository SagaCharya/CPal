from django.http import Http404, JsonResponse
from django.shortcuts import render

import helpers
from . import services


def course_list_view(request):
    queryset = services.get_published_courses()
    print(queryset)
    # return JsonResponse({'data':[x.path for x in queryset]})
    context = {"object_list": queryset}
    return render(request, "courses/list.html", context)


def course_detail_view(request, course_id=None, *args, **kwargs):
    course_obj = services.get_course_detail(course_id=course_id)
    if course_obj is None:
        raise Http404
    lesson_queryset = services.get_course_lessons(course_obj)
    # return JsonResponse({'data':course_obj.id, 'lessons_ids':[x.path for x in lesson_queryset]})
    context = {
        'object': course_obj,
        'lessons_queryset': lesson_queryset
    }
    return render(request, "courses/detail.html", context)


def lesson_detail_view(request, course_id=None, lesson_id=None, *args, **kwargs):
    print(course_id, lesson_id)
    lesson_obj = services.get_lesson_detail(course_id=course_id, lesson_id=lesson_id)
    if lesson_obj is None:
        raise Http404
    
    template_name = "courses/lesson-coming-soon.html"
    context = {
        'object' : lesson_obj
    }
    if not lesson_obj.is_coming_soon and lesson_obj.has_video:
        
        template_name = "courses/lesson.html"  
        video_embed_html = helpers.get_cloudinary_video_object(lesson_obj, width=1250, field_name="video", as_html=True)  
        context['video_embed'] = video_embed_html
    
    return render(request, template_name, context)
