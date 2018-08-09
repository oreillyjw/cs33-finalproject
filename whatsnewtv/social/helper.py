from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def setup_paging_controls(data, page=1, num_per_page=20):
    paginator = Paginator(data, num_per_page)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)

    return data
