# branding.py
#
# Copyright 2024 Nexus Foundation
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

"""
Nexus Foundation Brand Colors and Styling

This module provides the official Nexus Foundation brand colors and utilities
for applying them to GTK applications.
"""

from gi.repository import Gtk, Gdk

# Nexus Foundation Official Brand Colors
COLORS = {
    # Primary Colors
    'primary': '#4f46e5',           # Indigo - Main brand color
    'primary_hover': '#6366f1',     # Lighter indigo for hover states
    'primary_active': '#4338ca',    # Darker indigo for active states
    
    # Secondary Colors
    'secondary': '#8b5cf6',         # Purple - Accent color
    'secondary_hover': '#a78bfa',   # Lighter purple for hover
    'secondary_active': '#7c3aed',  # Darker purple for active
    
    # Background Colors
    'background': '#0f121b',        # Dark blue - Primary background
    'surface': '#1a1d2e',           # Slightly lighter for surfaces
    'card': 'rgba(79, 70, 229, 0.1)',  # Card background with primary tint
    
    # Text Colors
    'text': '#f6f6f6',              # Light gray - Primary text
    'text_secondary': '#d1d5db',    # Dimmed text color
    
    # Border and Divider Colors
    'border': 'rgba(79, 70, 229, 0.2)',  # Semi-transparent primary
    'divider': 'rgba(246, 246, 246, 0.1)',  # Semi-transparent text
    
    # Status Colors
    'success': '#10b981',           # Green
    'warning': '#f59e0b',           # Amber
    'error': '#ef4444',             # Red
    'info': '#4f46e5',              # Primary (info same as brand)
}

# RGB Color Values (for GdkRGBA)
RGB_COLORS = {
    'primary': (79/255, 70/255, 229/255, 1.0),
    'secondary': (139/255, 92/255, 246/255, 1.0),
    'background': (15/255, 18/255, 27/255, 1.0),
    'text': (246/255, 246/255, 246/255, 1.0),
    'success': (16/255, 185/255, 129/255, 1.0),
    'warning': (245/255, 158/255, 11/255, 1.0),
    'error': (239/255, 68/255, 68/255, 1.0),
}


def get_color(color_name):
    """
    Get a color value by name.
    
    Args:
        color_name: Name of the color (e.g., 'primary', 'secondary')
    
    Returns:
        str: Hex color code
    """
    return COLORS.get(color_name, '#000000')


def get_rgba(color_name):
    """
    Get a GdkRGBA color by name.
    
    Args:
        color_name: Name of the color
    
    Returns:
        Gdk.RGBA: RGBA color object
    """
    rgba = Gdk.RGBA()
    if color_name in RGB_COLORS:
        r, g, b, a = RGB_COLORS[color_name]
        rgba.red = r
        rgba.green = g
        rgba.blue = b
        rgba.alpha = a
    else:
        rgba.parse(get_color(color_name))
    return rgba


def apply_brand_styles():
    """
    Apply Nexus Foundation brand styles to the GTK application.
    
    This function loads the custom CSS and applies it to the default display.
    Call this early in your application initialization.
    """
    css_provider = Gtk.CssProvider()
    
    # Brand colors CSS
    css = f"""
        @define-color nexus_primary {COLORS['primary']};
        @define-color nexus_primary_hover {COLORS['primary_hover']};
        @define-color nexus_primary_active {COLORS['primary_active']};
        @define-color nexus_secondary {COLORS['secondary']};
        @define-color nexus_secondary_hover {COLORS['secondary_hover']};
        @define-color nexus_secondary_active {COLORS['secondary_active']};
        @define-color nexus_background {COLORS['background']};
        @define-color nexus_surface {COLORS['surface']};
        @define-color nexus_text {COLORS['text']};
        @define-color nexus_text_secondary {COLORS['text_secondary']};
        @define-color nexus_border {COLORS['border']};
        
        window {{
            background-color: @nexus_background;
            color: @nexus_text;
        }}
        
        .suggested-action {{
            background-color: @nexus_primary;
            color: @nexus_text;
            border-radius: 6px;
        }}
        
        .suggested-action:hover {{
            background-color: @nexus_primary_hover;
        }}
        
        .suggested-action:active {{
            background-color: @nexus_primary_active;
        }}
        
        button {{
            border-radius: 6px;
        }}
        
        .card {{
            background-color: {COLORS['card']};
            border: 1px solid @nexus_border;
            border-radius: 8px;
        }}
        
        switch:checked {{
            background-color: @nexus_primary;
        }}
        
        entry:focus {{
            border-color: @nexus_primary;
            box-shadow: 0 0 0 2px rgba(79, 70, 229, 0.3);
        }}
    """
    
    css_provider.load_from_data(css.encode())
    
    # Apply to default display
    Gtk.StyleContext.add_provider_for_display(
        Gdk.Display.get_default(),
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )


def create_color_button(color_hex, selected=False):
    """
    Create a circular color button with the specified color.
    
    Args:
        color_hex: Hex color code (e.g., '#4f46e5')
        selected: Whether this button is currently selected
    
    Returns:
        Gtk.Button: Configured color button
    """
    button = Gtk.Button()
    button.set_css_classes(['circular'])
    
    css_provider = Gtk.CssProvider()
    css = f"""
        button {{
            background-color: {color_hex};
            border-radius: 999px;
            min-width: 48px;
            min-height: 48px;
            border: 3px solid {'#ffffff' if selected else 'transparent'};
        }}
        button:hover {{
            border-color: #ffffff;
            opacity: 0.9;
        }}
    """
    css_provider.load_from_data(css.encode())
    button.get_style_context().add_provider(
        css_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    
    if selected:
        button.set_icon_name('object-select-symbolic')
    
    return button


# Application metadata
APP_NAME = 'NexaOS Customize'
APP_ID = 'org.nexuspenn.nexaos.customize'
ORGANIZATION = 'Nexus Foundation'
VERSION = '1.0.0'
WEBSITE = 'https://nexuspenn.org'
ISSUES_URL = 'https://github.com/Nexuspenn/NexaCustomize/issues'
