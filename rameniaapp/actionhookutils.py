from rameniaapp.models import ActionHook, Badge
from django.contrib.auth.models import User

def dispatch_hook(user, hook_name):
    hooks = ActionHook.objects.filter(hook_name=hook_name)
    for hook in hooks:
        if hook_name == "rep-changed":
            if "lt" in hook.params:
                if hook.params["target-val"] < user.metadata["Reputation"]:
                    dispatch_hook(user, hook.params["lt"])
            if "gteq" in hook.params:
                if hook.params["target-val"] >= user.metadata["Reputation"]:
                    dispatch_hook(user, hook.params["gteq"])
        if "change-rep" in hook.params:
            cur_rep =  user.profile.metadata["Reputation"]
            user.profile.metadata["Reputation"] = cur_rep + hook.params["change-rep"]
            user.profile.save()
        if "add-badge" in hook.params:
            user.profile.badges.add(Badge.objects.get(pk=hook.params["add-badge"]))
        if "remove-badge" in hook.params:
            user.profile.badges.remove(Badge.objects.get(pk=hook.params["remove-badge"]))
