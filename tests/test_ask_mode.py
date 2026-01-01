#!/usr/bin/env python3
"""
"""

import sys
import os


class TestAskMode(unittest.TestCase):
    """Test the interactive confirmation mode functionality."""

    def test_set_ask_mode(self):
        """Test that ask mode can be enabled and disabled."""
        from unused_categories_bot import set_ask_mode, is_ask_mode

        # Initially should be False (default)
        set_ask_mode(False)
        self.assertFalse(is_ask_mode())

        # Enable ask mode
        set_ask_mode(True)
        self.assertTrue(is_ask_mode())

        # Disable ask mode
        set_ask_mode(False)
        self.assertFalse(is_ask_mode())

    def test_confirm_edit_without_ask_mode(self):
        """Test that confirm_edit returns True when ask mode is disabled."""
        from unused_categories_bot import confirm_edit, set_ask_mode

        set_ask_mode(False)
        result = confirm_edit("Test Page", "old text", "new text")
        self.assertTrue(result)

    def test_confirm_edit_with_yes_response(self):
        """Test that confirm_edit returns True when user enters 'y'."""
        from unused_categories_bot import confirm_edit, set_ask_mode
        from unittest.mock import patch
        import unused_categories_bot

        # Reset auto_approve_all state
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(True)

        with patch('builtins.input', return_value='y'):
            result = confirm_edit("Test Page", "old text", "new text")
            self.assertTrue(result)

        set_ask_mode(False)

    def test_confirm_edit_with_empty_response(self):
        """Test that confirm_edit returns True when user enters empty string."""
        from unused_categories_bot import confirm_edit, set_ask_mode
        from unittest.mock import patch
        import unused_categories_bot

        # Reset auto_approve_all state
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(True)

        with patch('builtins.input', return_value=''):
            result = confirm_edit("Test Page", "old text", "new text")
            self.assertTrue(result)

        set_ask_mode(False)

    def test_confirm_edit_with_no_response(self):
        """Test that confirm_edit returns False when user enters 'n'."""
        from unused_categories_bot import confirm_edit, set_ask_mode
        from unittest.mock import patch
        import unused_categories_bot

        # Reset auto_approve_all state
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(True)

        with patch('builtins.input', return_value='n'):
            result = confirm_edit("Test Page", "old text", "new text")
            self.assertFalse(result)

        set_ask_mode(False)

    def test_confirm_edit_with_all_response(self):
        """Test that confirm_edit sets auto_approve_all when user enters 'a'."""
        from unused_categories_bot import confirm_edit, set_ask_mode
        from unittest.mock import patch
        import unused_categories_bot

        # Reset auto_approve_all state
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(True)

        with patch('builtins.input', return_value='a'):
            result = confirm_edit("Test Page", "old text", "new text")
            self.assertTrue(result)
            self.assertTrue(unused_categories_bot._auto_approve_all)

        # Reset for other tests
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(False)

    def test_confirm_edit_auto_approve_skips_prompt(self):
        """Test that confirm_edit skips prompt when auto_approve_all is True."""
        from unused_categories_bot import confirm_edit, set_ask_mode
        from unittest.mock import patch
        import unused_categories_bot

        # Set auto_approve_all to True
        unused_categories_bot._auto_approve_all = True
        set_ask_mode(True)

        # input should not be called when auto_approve_all is True
        with patch('builtins.input') as mock_input:
            result = confirm_edit("Test Page", "old text", "new text")
            self.assertTrue(result)
            mock_input.assert_not_called()

        # Reset for other tests
        unused_categories_bot._auto_approve_all = False
        set_ask_mode(False)
