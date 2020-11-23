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
    noodle = Noodle(name=name, metadata=metadata, editor=editor, created_timestamp=edit.timestamp)
    noodle.save()
    return noodle

def edit_noodle(edit):
    '''Applies edits to noodle object'''
    noodle = edit.noodle
    # Because of how the form is constructed, the if statements are currently
    # always true on a non-malformed Edit, but this will help if optimizations
    # are made to reduce DB calls
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
    # Prevents issues from banned user's edits, as they may still be good data
    if edit.editor:
        noodle.editor = edit.editor
    noodle.edited_timestamp = edit.timestamp
    noodle.save()


def add_image(edit, noodle):
    '''Create associated NoodleImage and delete any pre-existing defaults'''
    if edit.image:
        # This code associates the temp_image's path with a new NoodleImage
        temp_image = edit.image
        noodle_image = NoodleImage(noodle=noodle, uploader=edit.editor, timestamp=edit.timestamp)
        noodle_image.image = ImageFile(temp_image, temp_image.name)
        noodle_image.save()
        # Remove the default placeholder image if a valid image was uploaded
        default_img = NoodleImage.objects.filter(noodle=edit.noodle, is_default=True)
        if default_img:
            default_img[0].delete()
        return noodle_image
    else:
        # Upload a placeholder image to prevent issues and fill space
        # on new noodles without it
        if not edit.noodle:
            noodle_image = NoodleImage(noodle=noodle, uploader=edit.editor, is_default=True)
            noodle_image.save()
            return noodle_image
        # If the default is the only image, no point in the extra calls
        # to make it the main
        return None

def remove_image(edit):
    '''Remove an image'''
    if "remove_image" in edit.change:
        images = edit.change["remove_image"]
        # NOTE: At the moment, assuming an attempt to remove the main image
        # will require setting a new one. If this is unreasonable, please
        # create support issue to handle doing this automatically here.
        for img_key in images:
            img = NoodleImage.objects.get(pk=img_key)
            img.delete()

def set_as_main(edit, image):
    '''Set an image as the main'''
    if "set_main" in edit.change and edit.change["set_main"]:
        main_image = NoodleImage.objects.filter(noodle=edit.noodle, main=True)[0]
        if main_image:
            main_image.main = False
            main_image.save()
        image.main = True
        image.save()

def update_tags(edit, noodle):
    '''Add or remove tags to noodle given list of new tags'''
    current_tags = set(noodle.tags.values_list("name", flat=True))
    new_tags = set(edit.change["Tags"])
    tag_dict = Tag.objects.in_bulk(field_name='name')
    add_tag_list = []
    remove_tag_list = []
    # If they're sets this is a really efficient way to get the difference
    for tag in new_tags - current_tags:
        # Forgot to add this, but this prevents accidentaly whitespace 
        # being read as tag name
        tag = tag.strip(" ")
        if tag in tag_dict:
            add_tag_list.append(tag_dict[tag])
        else:
            new_tag = Tag(name=tag)
            new_tag.save()
            add_tag_list.append(new_tag.pk)
    for tag in current_tags - new_tags:
        tag = tag.strip(" ")
        if tag in tag_dict:
            remove_tag_list.append(tag_dict[tag])
    # Split off in case we want to use this elsewhere
    save_tags(noodle, add_tag_list, remove_tag_list)
    
    
def save_tags(noodle, add_tags, remove_tags):
    '''Adds/removes tags from noodle object'''
    noodle.tags.add(*add_tags)
    noodle.tags.remove(*remove_tags)
    noodle.save()

def apply_change(edit):
    '''Apply an edit in the expected format to a noodle or create a new one'''
    # Not having an assoc noodle means it's a new entry
    # and vice versa
    noodle = None
    if edit.noodle:
        edit_noodle(edit)
        noodle = edit.noodle
    else:
        noodle = add_noodle(edit)
    update_tags(edit, noodle)
    image = add_image(edit, noodle)
    # These two methods were not implemented due to time constraints and UI 
    # difficulties, but worked fine in testing
    if image:
        set_as_main(edit, image)
    remove_image(edit)
    # An applied edit is no longer needed- calling method will usually
    # have a cached version or take necessary precautions
    edit.delete()
