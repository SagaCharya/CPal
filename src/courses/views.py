from django.http import Http404, JsonResponse
from django.shortcuts import render
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
    return JsonResponse({'data':lesson_obj.id})
    return render(request, "courses/lessson.html", {})
