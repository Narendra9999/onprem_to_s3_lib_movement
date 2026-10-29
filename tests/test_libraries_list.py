import os
import unittest
 
class TestLibrariesListFilesExist(unittest.TestCase):
    def test_files_exist(self):
        # Get the current directory of this test file
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Debug output to check the paths
        print(f"Current directory: {current_dir}")
        
        # Construct the relative path to the files.json file
        json_file_path = os.path.join(current_dir, "..", "libraries_list", "files.json")
        
        print(f"Checking for files.json at: {json_file_path}")
 
        # Assert that the file exists
        self.assertTrue(os.path.exists(json_file_path), "files.json does not exist in libraries_list folder")
        
        # Construct the relative path to the package_registry.json file
        json_file_path = os.path.join(current_dir, "..", "libraries_list", "package_registry.json")
        
        print(f"Checking for package_registry.json at: {json_file_path}")
 
        # Assert that the file exists
        self.assertTrue(os.path.exists(json_file_path), "package_registry.json does not exist in libraries_list folder")
 
if __name__ == '__main__':
    unittest.main()
 
