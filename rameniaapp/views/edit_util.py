from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from django.core.files.images import ImageFile

def add_noodle(edit):
    '''Creates new noodle object'''
    name = edit.change["Name"]
    metadata = { "Description": edit.change["Description"], \
                 "Flavor": edit.change["Flavor"], \
                 "Manufacturer": edit.change["Manufacturer"], \
                 "Released": edit.change["Released"], "Line": edit.change["Line"] }
    editor = edit.editor
    noodle = Noodle(name=name, metadata=metadata, editor=editor)
    noodle.save()
    return noodle

def update_tags(edit, noodle):
    '''Adds/removes tags from noodle object'''
    if "add_tags" in edit.change:
        add_tags = edit.change["add_tags"]
        noodle.tags.add(*add_tags)
    if "remove_tags" in edit.change:
        remove_tags = edit.change["remove_tags"]
        noodle.tags.remove(*remove_tags)

def edit_noodle(edit):
    '''Applies edits to noodle object'''
    noodle = edit.noodle
    if "Name" in edit.change:
        noodle.name = edit.change['Name']
    if "Description" in edit.change:
        noodle.metadata["Description"] = edit.change["Description"]
    if "Flavor" in edit.change:
        noodle.metadata["Flavor"] = edit.change["Flavor"]
    if "Manufacturer" in edit.change:
        noodle.metadata["Manufacturer"] = edit.change["Manufacturer"]
    if "Released" in edit.change:
        noodle.metadata["Released"] = edit.change["Released"]
    if "Line" in edit.change:
        noodle.metadata["Line"] = edit.change["Line"]
    if edit.editor:
        noodle.editor = edit.editor
    noodle.save()


def add_image(edit, noodle):
    '''Add new image'''
    if edit.image:
        temp_image = edit.image
        noodle_image = NoodleImage(noodle=noodle, uploader=edit.editor)
        noodle_image.image = ImageFile(temp_image, temp_image.name)
        noodle_image.save()
        return noodle_image
    else:
        return None

def remove_image(edit):
    '''Remove an image'''
    if "remove_image" in edit.change:
        images = edit.change["remove_image"]
        print(images)
        # NOTE: At the moment, assuming an attempt to remove the main image
        # will require setting a new one. If this is unreasonable, please
        # create support issue to handle doing this automatically here.
        for img_key in images:
            img = NoodleImage.objects.get(pk=img_key)
            img.delete()

def set_as_main(edit, image):
    '''Set a main image'''
    if "set_main" in edit.change and edit.change["set_main"]:
        main_image = NoodleImage.objects.filter(noodle=edit.noodle, main=True)[0]
        if main_image:
            main_image.main = False
            main_image.save()
        image.main = True
        image.save()

def apply_change(edit):
    '''Apply an edit in the expected format to a noodle'''
    noodle = None
    if edit.noodle:
        edit_noodle(edit)
        noodle = edit.noodle
    else:
        noodle = add_noodle(edit)
    update_tags(edit, noodle)
    image = add_image(edit, noodle)
    if image:
        set_as_main(edit, image)
    remove_image(edit)
    edit.delete()

