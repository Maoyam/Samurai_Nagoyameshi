from django.views.generic import TemplateView


class UpgradeTemplateView(TemplateView):
    template_name = 'general/user_upgrade.html'