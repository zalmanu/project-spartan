from haystack.forms import SearchForm


class PostsSearchForm(SearchForm):

    def no_query_found(self):
        return self.searchqueryset.all()
