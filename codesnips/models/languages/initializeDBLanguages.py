#!/local/bin/python

import os, sys, inspect
pkg = "~/public_html/oop/codesnips"
sys.path.append(os.path.dirname(os.path.expanduser(pkg)))
from codesnips.data import dbCommands 

class initializeLanguages:
    
    def __init__(self):
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'JAVA', 'James_Gosling', '1995', 'Cross-Platform', '1.0', 'javaFunction1_javaFunction2_javaFunction3_javaFunction4', 'javaFunction11_javaFunction12', 'javaFunction11_javaFunction12_javaFunction10_javaFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'JAVA', 'James_Gosling', '1995', 'Cross-Platform', '2.0', 'javaFunction1_javaFunction2_javaFunction3_javaFunction4', 'javaFunction11_javaFunction12', 'javaFunction11_javaFunction12_javaFunction10_javaFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'JAVA', 'James_Gosling', '1995', 'Cross-Platform', '3.0', 'javaFunction1_javaFunction2_javaFunction3_javaFunction4', 'javaFunction11_javaFunction12', 'javaFunction11_javaFunction12_javaFunction10_javaFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PHP', 'Rasmus_Lerdorf', '1995', 'Cross-Platform', '1.0', 'phpFunction1_phpFunction2_phpFunction3_phpFunction4', 'phpFunction11_phpFunction12', 'phpFunction11_phpFunction12_phpFunction10_phpFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PHP', 'Rasmus_Lerdorf', '1995', 'Cross-Platform', '2.0', 'phpFunction1_phpFunction2_phpFunction3_phpFunction4', 'phpFunction11_phpFunction12', 'phpFunction11_phpFunction12_phpFunction10_phpFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PHP', 'Rasmus_Lerdorf', '1995', 'Cross-Platform', '3.0', 'phpFunction1_phpFunction2_phpFunction3_phpFunction4', 'phpFunction11_phpFunction12', 'phpFunction11_phpFunction12_phpFunction10_phpFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PYTHON', 'Guido_van_Rossum', '1991', 'Cross-Platform', '1.0', 'pythonFunction1_pythonFunction2_pythonFunction3_pythonFunction4', 'pythonFunction11_pythonFunction12', 'pythonFunction11_pythonFunction12_pythonFunction10_pythonFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PYTHON', 'Guido_van_Rossum', '1991', 'Cross-Platform', '2.0', 'pythonFunction1_pythonFunction2_pythonFunction3_pythonFunction4', 'pythonFunction11_pythonFunction12', 'pythonFunction11_pythonFunction12_pythonFunction10_pythonFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        cmd = dbCommands.AddToDatabaseCommand('Language', 'name, creator, yearIntroduced, operatingSystem, version, depFunctions, newFunctions, allFunctions, bugs', "'PYTHON', 'Guido_van_Rossum', '1991', 'Cross-Platform', '3.0', 'pythonFunction1_pythonFunction2_pythonFunction3_pythonFunction4', 'pythonFunction11_pythonFunction12', 'pythonFunction11_pythonFunction12_pythonFunction10_pythonFunction9', 'had_a_single_week_to_develop_code'")
        cmd.execute()
        