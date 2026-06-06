import pytest
import pandas as pd
import os

def test_data_folder_exists():
    """Test that data folder exists"""
    assert os.path.exists('data/raw'), "data/raw folder should exist"

def test_fraud_data_exists():
    """Test that fraud data CSV exists"""
    assert os.path.exists('data/raw/Fraud_Data.csv'), "Fraud_Data.csv should exist"

def test_creditcard_data_exists():
    """Test that creditcard data CSV exists"""
    assert os.path.exists('data/raw/creditcard.csv'), "creditcard.csv should exist"

def test_ip_data_exists():
    """Test that IP to country data exists"""
    assert os.path.exists('data/raw/IpAddress_to_Country.csv'), "IpAddress_to_Country.csv should exist"

def test_notebooks_folder_exists():
    """Test that notebooks folder exists"""
    assert os.path.exists('notebooks'), "notebooks folder should exist"

def test_models_folder_exists():
    """Test that models folder exists"""
    assert os.path.exists('models'), "models folder should exist"