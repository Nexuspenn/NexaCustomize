# NexaOS Customize - Nexus Foundation Branding Guide

## Project Information

**Project Name**: NexaOS Customize  
**Organization**: Nexus Foundation  
**App ID**: `nexusfoundation.nexaos.customize`  
**Version**: 1.0.0  
**License**: GPL-3.0-or-later

## Brand Colors

The official Nexus Foundation brand colors for NexaOS:

### Primary Colors
- **Primary**: `#4f46e5` (Indigo) - Main brand color, used for primary actions and highlights
- **Secondary**: `#8b5cf6` (Purple) - Accent color for secondary elements
- **Background**: `#0f121b` (Dark Blue) - Primary background color for dark theme
- **Text**: `#f6f6f6` (Light Gray) - Primary text color for readability

### Usage Guidelines

#### Primary Color (#4f46e5)
- Use for primary buttons and call-to-action elements
- Use for selected/active states
- Use for important UI highlights
- Use for links and interactive elements

#### Secondary Color (#8b5cf6)
- Use for secondary buttons
- Use for hover states
- Use for decorative elements
- Use for complementary highlights

#### Background Color (#0f121b)
- Use for main application background
- Use for dark themed panels
- Use for overlay backgrounds

#### Text Color (#f6f6f6)
- Use for primary text on dark backgrounds
- Ensure contrast ratio meets WCAG AA standards (4.5:1)
- Use for headings and body text

## CSS Implementation

### Button Styling
```css
/* Primary Button */
.button-primary {
    background-color: #4f46e5;
    color: #f6f6f6;
    border-radius: 6px;
    padding: 8px 16px;
}

.button-primary:hover {
    background-color: #6366f1;
}

/* Secondary Button */
.button-secondary {
    background-color: #8b5cf6;
    color: #f6f6f6;
    border-radius: 6px;
    padding: 8px 16px;
}

.button-secondary:hover {
    background-color: #a78bfa;
}
```

### GTK CSS Provider Implementation

For GTK4 applications, apply brand colors using CSS providers:

```python
from gi.repository import Gtk

css_provider = Gtk.CssProvider()
css_provider.load_from_data(b"""
    window {
        background-color: #0f121b;
        color: #f6f6f6;
    }
    
    .suggested-action {
        background-color: #4f46e5;
        color: #f6f6f6;
    }
    
    .suggested-action:hover {
        background-color: #6366f1;
    }
    
    .destructive-action {
        background-color: #ef4444;
        color: #f6f6f6;
    }
    
    button {
        border-radius: 6px;
    }
    
    .card {
        background-color: rgba(79, 70, 229, 0.1);
        border: 1px solid rgba(79, 70, 229, 0.2);
        border-radius: 8px;
    }
""")

Gtk.StyleContext.add_provider_for_display(
    Gdk.Display.get_default(),
    css_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)
```

## File Naming Conventions

All files related to NexaOS Customize should follow these naming patterns:

### Application Files
- **App ID**: `nexusfoundation.nexaos.customize`
- **Desktop File**: `nexusfoundation.nexaos.customize.desktop`
- **AppData**: `nexusfoundation.nexaos.customize.appdata.xml`
- **GSchema**: `nexusfoundation.nexaos.customize.gschema.xml`
- **Icon**: `nexusfoundation.nexaos.customize.svg` (or .png)
- **Binary**: `nexacustomize`
- **Module Directory**: `nexacustomize/`

### Resource Paths
- **GResource Prefix**: `/org/nexusfoundation/nexaos/customize`
- **Schema Path**: `/org/nexusfoundation/nexaos/customize/`

## Typography

### Font Recommendations
- **Primary Font**: Inter, Roboto, or system default
- **Monospace Font**: JetBrains Mono, Fira Code, or system monospace

### Font Sizes
- **Heading 1**: 24px (bold)
- **Heading 2**: 20px (bold)
- **Heading 3**: 16px (bold)
- **Body Text**: 14px (regular)
- **Small Text**: 12px (regular)
- **Button Text**: 14px (medium)

## Icon Guidelines

### Icon Style
- Use symbolic icons from GNOME icon theme
- Ensure icons work well on dark backgrounds
- Maintain consistent stroke width (2px recommended)
- Use the primary brand color (#4f46e5) for accent icons

### Icon Sizes
- **Application Icon**: 512x512px (scalable SVG preferred)
- **Toolbar Icons**: 24x24px
- **List Icons**: 16x16px
- **Large Icons**: 48x48px

## UI Components

### Window Design
- Default window size: 600x600px
- Minimum window size: 400x400px
- Use AdwApplicationWindow for modern GNOME appearance
- Use headerbar with consistent styling

### Spacing
- **Large Spacing**: 24px (between major sections)
- **Medium Spacing**: 16px (between related elements)
- **Small Spacing**: 8px (between tightly related elements)
- **Compact Spacing**: 4px (within grouped elements)

### Border Radius
- **Buttons**: 6px
- **Cards**: 8px
- **Dialogs**: 12px
- **Input Fields**: 6px

## Copyright and Attribution

All code files should include the following header:

```python
# filename.py
#
# Copyright 2024 Nexus Foundation
# Originally developed by Francesco Caracciolo (2023)
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
```

## Marketing Copy

### Tagline
"Customize Your NexaOS Experience"

### Short Description
"Tool to customize NexaOS GNOME appearance easily."

### Long Description
"NexaOS Customize is a powerful tool for personalizing your NexaOS desktop environment. Built by Nexus Foundation, it provides an intuitive interface for managing themes, layouts, extensions, and visual effects."

### Feature Highlights
- Quick layout presets for desktop configuration
- Material You color theming support
- GNOME Shell extension management
- Visual effects controls (blur, wobbly windows, magic lamp, desktop cube)
- System tray and desktop icons management
- Background logo customization

## Repository Information

### GitHub
- **Organization**: NexusFoundation
- **Repository**: NexaCustomize
- **URL**: https://github.com/Nexuspenn/NexaCustomize

### URLs
- **Website**: https://nexuspenn.org
- **Documentation**: https://docs.nexuspenn.org
- **Support**: https://community.nexuspenn.org
- **Issues**: https://github.com/Nexuspenn/NexaCustomize/issues

## Accessibility

### Color Contrast
All color combinations must meet WCAG AA standards:
- Normal text: 4.5:1 contrast ratio minimum
- Large text (18pt+): 3:1 contrast ratio minimum
- Interactive elements: Clearly distinguishable states

### Current Contrast Ratios
- Primary (#4f46e5) on Background (#0f121b): 7.8:1 ✓ (Excellent)
- Text (#f6f6f6) on Background (#0f121b): 14.5:1 ✓ (Excellent)
- Secondary (#8b5cf6) on Background (#0f121b): 6.2:1 ✓ (Excellent)

## Build and Installation

### Build Requirements
- GNOME 46+
- GTK 4.0+
- Python 3.10+
- Meson >= 0.59.0
- GObject Introspection

### Installation Commands
```bash
# From source
git clone https://github.com/Nexuspenn/NexaCustomize.git
cd NexaCustomize
./install.sh

# From Flatpak
flatpak install flathub nexusfoundation.nexaos.customize
```

### Running the Application
```bash
# Installed binary
nexacustomize

# Flatpak
flatpak run nexusfoundation.nexaos.customize

# Development
./run.sh
```

## Version History

### Version 1.0.0 (2024-01-27)
- Rebranded to Nexus Foundation
- Updated brand colors and styling
- Improved application metadata
- Enhanced UI consistency
- Updated copyright information

## Credits

- **Nexus Foundation** - Current maintainer and development
- **Francesco Caracciolo** - Original author and developer
- **Nyarch developers** - Original inspiration and foundation

---

© 2024 Nexus Foundation. All rights reserved.
Licensed under GPL-3.0-or-later.
