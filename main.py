# Author: Hannah Johnston hlj5107@psu.edu
# Collaborator: Matthew Beatty mrb6319@psu.edu
# Collaborator: Vincent Barnes vbj5182@psu.edu
# Collaborator: Craig Pena cmp6428@psu.edu
# Section: 3
# Breakout: 7

def GetLetterGrade(grade): 
  if grade >= 93.0: 
    print(f"Your letter grade for CMPSC 131 is A.")
  elif grade >= 90.0:
    print(f"Your letter grade for CMPSC 131 is A-.")
  elif grade >= 87.0:
    print(f"Your letter grade for CMPSC 131 is B+.")
  elif grade >= 83.0:
    print(f"Your letter grade for CMPSC 131 is B.")
  elif grade >= 80.0:
    print(f"Your letter grade for CMPSC 131 is B-.")
  elif grade >= 77.0:
    print(f"Your letter grade for CMPSC 131 is C+.")
  elif grade >= 70.0:
    print(f"Your letter grade for CMPSC 131 is C.")
  elif grade >= 60.0:
    print(f"Your letter grade for CMPSC 131 is D.")
  elif grade < 60.0:
    print(f"Your letter grade for CMPSC 131 is F.")
  else:
    print(f"Your letter grade for for CMPSC 131 is A.")
def run():
  variable=float(input("Enter your CMPSC 131 grade: "))
  grade=GetLetterGrade(variable)