from rameniaapp.models import Noodle, NoodleImage, Edit, Tag
from django.core.files.images import ImageFile

def add_noodle(edit):
    name = edit.change.name
    metadata = { "Description": edit.change.description, \
                 "Flavor": edit.change.flavor, \
                 "Manufacturer": edit.change.manufacturer, \
                 "Released": edit.change.released, "Line": edit.change.line }
    editor = edit.editor
    noodle = Noodle(name=name, metadata=metadata, editor=editor)
    noodle.save()
    return noodle

def update_tags(edit, noodle):
    if edit.change.add_tags:
        add_tags = edit.change.add_tags
        noodle.tags.add(*add_tags)
    if edit.change.remove_tags:
        remove_tags = edit.change.remove_tags
        noodle.tags.remove(*remove_tags)
    #TODO: Retrieve tags PKs into Tag list
    #Use *[] to explode into args for noodle.tags.add
    #Return

def edit_noodle(edit):
    noodle = edit.noodle
    if edit.change.name:
        noodle.name = edit.change.name
    if edit.change.description:
        noodle.metadata.description = edit.change.description
    if edit.change.flavor:
        noodle.metadata.flavor = edit.change.flavor
    if edit.change.manufacturer:
        noodle.metadata.manufacturer = edit.change.manufacturer
    if edit.change.released:
        noodle.metadata.released = edit.change.released
    if edit.change.line:
        noodle.metadata.line = edit.change.line
    if edit.editor:
        noodle.editor = edit.editor
    noodle.save()
    update_tags(edit, noodle)
    add_image(edit, noodle)

def add_image(edit, noodle):
    if edit.image:
        temp_image = edit.image
        noodle_image = NoodleImage(noodle=noodle, uploader=edit.editor)
        noodle_image.image = ImageFile(temp_image, temp_image.name)
        noodle_image.save()
    else:
        pass

def apply_change(edit):
    if edit.noodle:
        edit_noodle(edit)
    else:
        noodle = add_noodle(edit)
        update_tags(edit, noodle)
        add_image(edit, noodle)
    edit.delete()