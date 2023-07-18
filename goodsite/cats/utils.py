from cats.models import Menu, Category, Cats


class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        obs = Cats.objects.all()
        # list_of_titles = list()
        # for o in obs:
        #     single_title = o.title
        #     list_of_titles.append(single_title)
        # print(list_of_titles)

        menu = list(Menu.objects.all())
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
