import random
import string
import asyncio
from typing import List

async def generate_password(length: int = 12) -> str:
    """Generate a secure random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

async def generate_multiple_passwords(n: int, length: int = 12) -> List[str]:
    """Generate multiple passwords concurrently"""
    tasks = [generate_password(length) for _ in range(n)]
    passwords = await asyncio.gather(*tasks)
    return passwords

async def main():
    """Interactive main function"""
    print("🔐 Async Password Generator")
    print("-" * 30)
    
    try:
        count = int(input("How many passwords? (default: 5): ") or 5)
        length = int(input("Password length? (default: 12): ") or 12)
        
        print(f"\n⏳ Generating {count} passwords...")
        passwords = await generate_multiple_passwords(count, length)
        
        print("\n✅ Generated Passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i:2d}. {pwd}")
            
        # Optional: Save to file
        save = input("\n💾 Save to file? (y/n): ").lower()
        if save == 'y':
            filename = input("Filename (default: passwords.txt): ") or "passwords.txt"
            with open(filename, 'w') as f:
                for i, pwd in enumerate(passwords, 1):
                    f.write(f"Password {i}: {pwd}\n")
            print(f"✅ Saved to {filename}")
            
    except ValueError:
        print("❌ Please enter valid numbers")
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())
