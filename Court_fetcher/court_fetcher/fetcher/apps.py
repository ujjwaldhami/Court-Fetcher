from django.apps import AppConfig

class FetcherConfig(AppConfig):
    name = 'fetcher'

    def ready(self):
        import fetcher.templatetags.form_filters
