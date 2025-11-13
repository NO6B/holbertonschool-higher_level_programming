#function generate_invitations
def generate_invitations(template, attendees):

    if not isinstance(template, str):
        return "error: must be str"

    if not isinstance(attendees, list):
        return "error: attendees must be list"

    if not template:
        return "error: template must not be empty"

    if not attendees:
        return "error: attendees must not be empty"

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for index, attendee in enumerate(attendees, start=1):
        output_content = template
        for placeholder in placeholders:
            placeholder_key = f"{{{placeholder}}}"
            value = attendee.get(placeholder)

            if value is None:
                value = "N/A"

            output_content = output_content.replace(placeholder_key, str(value))

        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
