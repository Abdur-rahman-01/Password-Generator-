"""
Advanced password generator module with enhanced features
"""
import random
import string
import asyncio
from typing import List, Optional
import secrets  # More secure than random for passwords

class PasswordConfig:
    """Configuration class for password generation"""
    def __init__(self, 
                 length: int = 12,
                 include_lowercase: bool = True,
                 include_uppercase: bool = True,
                 include_digits: bool = True,
                 include_symbols: bool = True,
                 exclude_ambiguous: bool = False):
        self.length = length
        self.include_lowercase = include_lowercase
        self.include_uppercase = include_uppercase
        self.include_digits = include_digits
        self.include_symbols = include_symbols
        self.exclude_ambiguous = exclude_ambiguous

async def generate_secure_password(config: PasswordConfig) -> str:
    """Generate a cryptographically secure password"""
    characters = ""
    
    if config.include_lowercase:
        chars = string.ascii_lowercase
        if config.exclude_ambiguous:
            chars = chars.replace('l', '').replace('o', '')
        characters += chars
        
    if config.include_uppercase:
        chars = string.ascii_uppercase
        if config.exclude_ambiguous:
            chars = chars.replace('I', '').replace('O', '')
        characters += chars
        
    if config.include_digits:
        chars = string.digits
        if config.exclude_ambiguous:
            chars = chars.replace('0', '').replace('1', '')
        characters += chars
        
    if config.include_symbols:
        characters += string.punctuation
    
    # Use secrets for cryptographic randomness
    password = ''.join(secrets.choice(characters) for _ in range(config.length))
    return password
