from json import load, dump
from os import listdir, path, remove

def add_test(unitCode, testCount):
  """
  Adds a test to the unit with code `unitCode` to the `app/questions/units.json` file.
  The unit is created if it does not already exist in the file.
  The `testCount` is the number of the question set being added. For example, if we have
  created a file named `cits3401_3.json`, we will call `add_test("cits3401", 3)`.
  Returns 0 on success, and -1 if the testCount is already supported.
  """
  with open("questions/units.json", "r") as readfile: # We don't want to have to write to the file unless we have to
    units = load(readfile)
  try: # File already contains the unit
    tests = units[unitCode.upper()]
    if (testCount in tests):
      return -1 # Test count already supported
    else:
      tests.append(testCount)
      tests.sort()
  except KeyError: # File does not already contain the unit
    units[unitCode.upper()] = [testCount]
  with open("questions/units.json", "w") as writefile:
    dump(units, writefile)
    return 0


def get_tests(unitCode):
  """
  Gets the list of supported tests for the unit with code `unitCode`.
  Returns the list of test numbers, or -1 if the unit is not supported yet.
  """
  with open("questions/units.json", "r") as readfile: # We don't want to have to write to the file unless we have to
    units = load(readfile)
  try:
    tests = units[unitCode.upper()]
  except KeyError:
    tests = -1
  return tests

def get_all(filepath):
  """
  Loads and returns the entire `units.json` file containing all supported units and their test numbers.
  When referencing this function outside of the main `unitJSON.py` module file, the `filepath` variable
  is likely to be `app/questions/units.json`.
  """
  with open(filepath, "r") as readfile:
    units = load(readfile)
    return units

def remove_unit(unitCode):
  """
  Removes a unit from the `app/questions/units.json` file and deletes all the question sets.
  Returns the list of supported tests for that unit, or `-1` if the unit was not in the units file.
  """
  with open("questions/units.json", "r") as readfile:
    units = load(readfile)
  tests = units.pop(unitCode, None)
  with open("questions/units.json", "w") as writefile:
    dump(units, writefile, indent=4)
  # Delete all question set files for this unit
  for test in tests:
    questionset = "questions/{}_{}.json".format(unitCode.lower(), test)
    if path.exists(questionset):
        remove(questionset)
  if tests is not None:
    return tests
  else:
    return -1


def remove_test(unitCode, testNumber):
  """
  Removes test number `testNumber` from the unit with code `unitCode`.
  Returns `0` on successful removal of track and file, `-1` if the `testNumber` is not being tracked, and `-2` if the test file did not exist.
  The `testNumber` check occurs before the existing file check.
  """
  with open("questions/units.json", "r") as readfile:
    units = load(readfile)
  try:
    tests = units[unitCode]
    if (testNumber in tests):
      tests.remove(testNumber)
      if (len(tests) == 0):
        units.pop(unitCode) # Remove this unit if we removed the final test
      with open("questions/units.json", "w") as writefile:
        dump(units, writefile)
      # Delete the actual question set file
      questionset = "questions/{}_{}.json".format(unitCode.lower(), testNumber)
      if path.exists(questionset):
        remove(questionset)
      else:
        return -2
      return 0
    else:
      return -1 # Test number not in tests
  except KeyError:
    return -1 # Unit is not supported