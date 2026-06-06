import pytest
import os

def test_project_structure():
    """Test that required folders exist"""
    required_folders = ['notebooks', 'models', 'src', 'tests', 'data']
    for folder in required_folders:
        assert os.path.exists(folder), f"{folder} folder should exist"

def test_gitignore_exists():
    """Test that .gitignore exists"""
    assert os.path.exists('.gitignore'), ".gitignore should exist"

def test_readme_exists():
    """Test that README.md exists"""
    assert os.path.exists('README.md'), "README.md should exist"

def test_requirements_exists():
    """Test that requirements.txt exists"""
    assert os.path.exists('requirements.txt'), "requirements.txt should exist"

def test_notebooks_exist():
    """Test that at least one notebook exists"""
    import glob
    notebooks = glob.glob('notebooks/*.ipynb')
    assert len(notebooks) > 0, "At least one Jupyter notebook should exist"

def test_workflow_exists():
    """Test that GitHub Actions workflow exists"""
    assert os.path.exists('.github/workflows/unittests.yml'), "Workflow file should exist"

def test_models_folder_exists():
    """Test that models folder exists"""
    assert os.path.exists('models'), "models folder should exist"

def test_src_folder_exists():
    """Test that src folder exists"""
    assert os.path.exists('src'), "src folder should exist"