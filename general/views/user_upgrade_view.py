from django.views.generic import TemplateView


class UserUpgradeView(TemplateView):
    template_name = "general/user_upgrade.html"