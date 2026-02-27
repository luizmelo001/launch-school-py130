"""
Write a function build_profile that takes a first name and a last name, and any number of keyword arguments to add to a user's profile.
"""

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile