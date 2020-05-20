from json import load, dump

def add_count(unitCode, testCount):
  """
  Adds a unit with code `unitCode` to the `app/questions/units.json` file with a test count of `testCount`.
  Returns the old count of the unit, or -1 if the unit was not originally in the units file.
  """
  with open("questions/units.json", "r") as readfile: # We don't want to have to write to the file unless we have to
    units = load(readfile)
  try: # File already contains the unit
    old = units[unitCode]
    units[unitCode] = testCount
  except KeyError: # File does not already contain the unit
    old = -1
    units[unitCode] = testCount
  with open("questions/units.json", "w") as writefile:
    dump(units, writefile, indent=4)
    return old


def get_count(unitCode):
  """
  Gets the test count for the unit with code `unitCode`.
  Returns the test count, or -1 if the unit is not supported yet.
  """
  with open("questions/units.json", "r") as readfile: # We don't want to have to write to the file unless we have to
    units = load(readfile)
  try:
    count = units[unitCode]
  except KeyError:
    count = -1
  return count


def remove_unit(unitCode):
  """
  Removes a unit from the `app/questions/units.json` file.
  Returns the test count of the unit, or `-1` if the unit was not in the units file.
  """
  with open("questions/units.json", "r") as readfile:
    units = load(readfile)
  value = units.pop(unitCode, None)
  with open("questions/units.json", "w") as writefile:
    dump(units, writefile, indent=4)
  if value is not None:
    return value
  else:
    return -1