import pytest
import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from main import generate_password, generate_multiple_passwords

@pytest.mark.asyncio
async def test_generate_password():
    """Test single password generation"""
    password = await generate_password(12)
    assert len(password) == 12
    assert isinstance(password, str)

@pytest.mark.asyncio
async def test_generate_multiple_passwords():
    """Test multiple password generation"""
    passwords = await generate_multiple_passwords(3, 8)
    assert len(passwords) == 3
    assert all(len(pwd) == 8 for pwd in passwords)
    # Ensure all passwords are unique
    assert len(set(passwords)) == 3

@pytest.mark.asyncio
async def test_password_length_variations():
    """Test different password lengths"""
    for length in [6, 12, 20, 32]:
        password = await generate_password(length)
        assert len(password) == length
