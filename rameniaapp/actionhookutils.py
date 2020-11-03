from rameniaapp.models import ActionHook, Badge
from django.contrib.auth.models import User

def dispatch_hook(user, hook_name, **kwargs):
    hooks = ActionHook.objects.filter(hook_name=hook_name)
    for hook in hooks:
        if "change-rep" in hook.params:
            cur_rep =  user.profile.metadata["Reputation"]
            user.profile.metadata["Reputation"] = cur_rep + hook.params["change-rep"]
            user.profile.save()
            dispatch_hook(user, "reputation", reputation=user.profile.metadata["Reputation"])
        if "add-badge" in hook.params:
            user.profile.badges.add(Badge.objects.get(pk=hook.params["add-badge"]))
        if "remove-badge" in hook.params:
            user.profile.badges.remove(Badge.objects.get(pk=hook.params["remove-badge"]))
        for key, value in kwargs.items():
            keyname = key + "-eq"
            if keyname in hook.params and hook.params[keyname] == value:
                dispatch_hook(hook.params[keyname])
            keyname = key + "-lt"
            if keyname in hook.params and hook.params[keyname] < value:
                dispatch_hook(hook.params[keyname])
            keyname = key + "-gt"
            if keyname in hook.params and hook.params[keyname] > value:
                dispatch_hook(hook.params[keyname])
            keyname = key + "-lte"
            if keyname in hook.params and hook.params[keyname] <= value:
                dispatch_hook(hook.params[keyname])
            keyname = key + "-gte"
            if keyname in hook.params and hook.params[keyname] >= value:
                dispatch_hook(hook.params[keyname])
    
