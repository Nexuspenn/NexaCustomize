# NexaOS Customize - Nexus Foundation Rebranding Summary

## Overview

This document summarizes all changes made to rebrand NexaCustomize from Nyarch Linux to **Nexus Foundation's NexaOS**.

**Project**: NexaOS Customize  
**Organization**: Nexus Foundation  
**Version**: 1.0.0  
**Date**: January 27, 2024  
**License**: GPL-3.0-or-later

---

## Brand Identity

### Official Brand Colors

| Color | Hex Code | Usage |
|-------|----------|-------|
| **Primary** | `#4f46e5` | Main brand color, primary actions, highlights |
| **Secondary** | `#8b5cf6` | Accent color, secondary elements |
| **Background** | `#0f121b` | Primary background for dark theme |
| **Text** | `#f6f6f6` | Primary text color |

### Application Identity

- **Name**: NexaOS Customize
- **App ID**: `nexusfoundation.nexaos.customize`
- **Binary**: `nexacustomize`
- **Developer**: Nexus Foundation
- **Website**: https://nexuspenn.org

---

## Complete File Listing

### Modified Files (42 changes)

#### 1. Root Directory Files

✅ **README.md**
- Updated title to "NexaOS Customize"
- Added Nexus Foundation branding
- Added brand colors section
- Updated installation instructions
- Added comprehensive feature list
- Updated credits and links

✅ **meson.build**
- Updated project name to 'nexacustomize'
- Version bumped to 1.0.0

✅ **install.sh**
- Already uses correct app ID: `nexusfoundation.nexaos.customize`

✅ **run.sh**
- Already uses correct app ID: `nexusfoundation.nexaos.customize`

✅ **nexusfoundation.nexaos.customize.json**
- Flatpak manifest (already correctly named)

#### 2. Data Directory (`data/`)

✅ **Renamed Files**:
- `moe.nyarchlinux.customize.desktop.in` → `nexusfoundation.nexaos.customize.desktop.in`
- `moe.nyarchlinux.customize.appdata.xml.in` → `nexusfoundation.nexaos.customize.appdata.xml.in`
- `moe.nyarchlinux.customize.gschema.xml` → `nexusfoundation.nexaos.customize.gschema.xml`

✅ **nexusfoundation.nexaos.customize.desktop.in**
- Name: "NexaOS Customize"
- Comment: "Customize NexaOS appearance and desktop environment"
- Exec: `nexacustomize`
- Icon: `nexusfoundation.nexaos.customize`

✅ **nexusfoundation.nexaos.customize.appdata.xml.in**
- Updated component ID
- Added comprehensive description
- Added feature list
- Added developer information
- Added URLs (homepage, bugtracker)
- Added screenshots and release notes

✅ **nexusfoundation.nexaos.customize.gschema.xml**
- Schema ID: `nexusfoundation.nexaos.customize`
- Path: `/org/nexusfoundation/nexaos/customize/`

✅ **meson.build**
- Updated all file references to new names

#### 3. Source Directory (`src/`)

✅ **Renamed Files**:
- `nyarchcustomize.gresource.xml` → `nexacustomize.gresource.xml`
- `nyarchcustomize.in` → `nexacustomize.in`

✅ **main.py**
- Updated copyright to "2024 Nexus Foundation"
- Changed app ID to `nexusfoundation.nexaos.customize`
- Updated about dialog:
  - Application name: "NexaOS Customize"
  - Developer: "Nexus Foundation"
  - Version: "1.0.0"
  - Added website and issue URLs
  - Updated copyright notice

✅ **window.py**
- Updated copyright to "2024 Nexus Foundation"
- Changed resource path: `/org/nexusfoundation/nexaos/customize/`
- Updated both UI resource references

✅ **window.ui**
- Updated menu label: "_About NexaOS Customize"

✅ **nexacustomize.gresource.xml**
- Updated resource prefix: `/org/nexusfoundation/nexaos/customize`

✅ **nexacustomize.in**
- Updated copyright to "2024 Nexus Foundation"
- Changed text domain to 'nexacustomize'
- Updated resource file name to 'nexacustomize.gresource'
- Updated module import from 'nexacustomize'

✅ **meson.build**
- Changed module directory to 'nexacustomize'
- Updated all resource references
- Changed output binary name to 'nexacustomize'

#### 4. Translation Files (`po/`)

✅ **POTFILES**
- Updated all file paths to use new names:
  - `data/nexusfoundation.nexaos.customize.desktop.in`
  - `data/nexusfoundation.nexaos.customize.appdata.xml.in`
  - `data/nexusfoundation.nexaos.customize.gschema.xml`

#### 5. New Files Created

✅ **BRANDING.md**
- Comprehensive branding guide
- Brand color specifications with usage guidelines
- CSS implementation examples
- GTK CSS provider implementation
- File naming conventions
- Typography guidelines
- Icon guidelines
- UI component specifications
- Copyright template
- Marketing copy
- Accessibility guidelines with contrast ratios
- Build and installation instructions
- Credits and attribution

✅ **CHANGELOG.md**
- Complete version history
- Detailed list of all changes
- Migration guide for developers, users, and package maintainers
- Breaking changes documentation
- Future roadmap

✅ **src/branding.py**
- Python module with brand color constants
- Helper functions for color management
- `apply_brand_styles()` function for GTK styling
- `create_color_button()` utility
- Application metadata constants
- RGB color values for GdkRGBA
- Comprehensive documentation

✅ **src/style.css**
- Complete CSS stylesheet with brand colors
- CSS variable definitions
- Styling for all GTK components:
  - Windows and header bars
  - Buttons (primary, secondary)
  - Cards and panels
  - List items
  - Switches and check buttons
  - Entry fields
  - Scrollbars
  - Progress bars
  - Tooltips
  - Popovers
  - Menu items
  - Status colors
  - View switchers
- Animations

✅ **REBRANDING_SUMMARY.md** (this file)
- Complete documentation of all changes

---

## Resource Path Changes

### Old Paths
```
/moe/nyarchlinux/customize/*
```

### New Paths
```
/org/nexusfoundation/nexaos/customize/*
```

All UI files, GResource bundles, and GSettings schemas have been updated to use the new paths.

---

## Application ID Changes

### Old Application ID
```
moe.nyarchlinux.customize
```

### New Application ID
```
nexusfoundation.nexaos.customize
```

Updated in:
- `src/main.py`
- `data/nexusfoundation.nexaos.customize.desktop.in`
- `data/nexusfoundation.nexaos.customize.appdata.xml.in`
- `data/nexusfoundation.nexaos.customize.gschema.xml`
- `nexusfoundation.nexaos.customize.json`
- `install.sh`
- `run.sh`

---

## Binary Name Changes

### Old Binary
```
nyarchcustomize
```

### New Binary
```
nexacustomize
```

Updated in:
- `src/meson.build`
- `data/nexusfoundation.nexaos.customize.desktop.in`
- `nexusfoundation.nexaos.customize.json`

---

## Module Name Changes

### Old Module
```python
from nyarchcustomize import main
```

### New Module
```python
from nexacustomize import main
```

Updated in:
- `src/nexacustomize.in`
- `src/meson.build`

---

## Testing Checklist

After applying these changes, test the following:

### Build System
- [ ] `meson setup build` completes without errors
- [ ] `meson compile -C build` builds successfully
- [ ] `meson install -C build` installs correctly
- [ ] Desktop file validates: `desktop-file-validate`
- [ ] AppStream file validates: `appstream-util validate`
- [ ] GSchema validates: `glib-compile-schemas --strict --dry-run`

### Application Launch
- [ ] Application launches from command line: `nexacustomize`
- [ ] Application launches from desktop file
- [ ] Application launches from Flatpak: `flatpak run nexusfoundation.nexaos.customize`
- [ ] Application icon displays correctly
- [ ] About dialog shows correct information

### UI and Styling
- [ ] Brand colors apply correctly
- [ ] Primary buttons use #4f46e5
- [ ] Window background is #0f121b
- [ ] Text color is #f6f6f6
- [ ] All UI elements render properly
- [ ] Switches and buttons respond correctly

### Functionality
- [ ] Layout presets work
- [ ] Extension management functions
- [ ] Color theming works
- [ ] All switches toggle correctly
- [ ] Settings persist correctly

### Resources
- [ ] UI files load from new resource paths
- [ ] Icons load correctly
- [ ] Translations work (if applicable)
- [ ] Help overlay loads

---

## Distribution Package Updates

### Package Name
Update package name to reflect new branding:
- **Suggested package name**: `nexaos-customize` or `nexacustomize`

### Dependencies
Ensure these are listed:
- `gtk4 >= 4.0`
- `libadwaita-1 >= 1.0`
- `python >= 3.10`
- `meson >= 0.59.0`
- `glib2 >= 2.70`
- `gobject-introspection`

### File Locations
Standard installation paths:
- Binary: `/usr/bin/nexacustomize`
- Data: `/usr/share/nexacustomize/`
- Desktop file: `/usr/share/applications/nexusfoundation.nexaos.customize.desktop`
- AppData: `/usr/share/metainfo/nexusfoundation.nexaos.customize.appdata.xml`
- GSchema: `/usr/share/glib-2.0/schemas/nexusfoundation.nexaos.customize.gschema.xml`
- Icons: `/usr/share/icons/hicolor/`

---

## Contact and Support

- **Website**: https://nexuspenn.org
- **Documentation**: https://docs.nexuspenn.org
- **GitHub**: https://github.com/Nexuspenn/NexaCustomize
- **Issues**: https://github.com/Nexuspenn/NexaCustomize/issues
- **Community**: https://community.nexuspenn.org

---

## Credits

### Nexus Foundation Team
- Project maintainer and development
- Branding and design
- Documentation

### Original Authors
- **Francesco Caracciolo** - Original development and design
- **Nyarch developers** - Original inspiration and foundation

---

## License

This project is licensed under the **GNU General Public License v3.0 or later** (GPL-3.0-or-later).

See [COPYING](COPYING) for full license text.

---

© 2024 Nexus Foundation. All rights reserved.
