# Changelog - Nexus Foundation Rebrand

## Version 1.0.0 (2024-01-27) - Nexus Foundation Rebrand

### Major Changes

#### Branding
- **Organization**: Changed from Nyarch to Nexus Foundation
- **Application Name**: NexaOS Customize
- **App ID**: `org.nexuspenn.nexaos.customize` (was `moe.nyarchlinux.customize`)
- **Binary Name**: `nexacustomize` (was `nyarchcustomize`)

#### Brand Colors
- **Primary Color**: #4f46e5 (Indigo)
- **Secondary Color**: #8b5cf6 (Purple)
- **Background**: #0f121b (Dark Blue)
- **Text**: #f6f6f6 (Light Gray)

### File Changes

#### Renamed Files

**Data Directory**:
- `moe.nyarchlinux.customize.desktop.in` → `org.nexuspenn.nexaos.customize.desktop.in`
- `moe.nyarchlinux.customize.appdata.xml.in` → `org.nexuspenn.nexaos.customize.appdata.xml.in`
- `moe.nyarchlinux.customize.gschema.xml` → `org.nexuspenn.nexaos.customize.gschema.xml`

**Source Directory**:
- `nyarchcustomize.gresource.xml` → `nexacustomize.gresource.xml`
- `nyarchcustomize.in` → `nexacustomize.in`
- Module directory: `nyarchcustomize/` → `nexacustomize/`

#### Updated Files

**Configuration Files**:
- `meson.build`: Updated project name and version
- `src/meson.build`: Updated module names and paths
- `data/meson.build`: Updated file references
- `po/POTFILES`: Updated file paths

**Source Files**:
- `src/main.py`: Updated app ID, copyright, and about dialog
- `src/window.py`: Updated copyright and resource paths
- `src/nexacustomize.in`: Updated module imports and text domain
- `src/nexacustomize.gresource.xml`: Updated resource prefix
- `src/window.ui`: Updated menu labels

**Documentation**:
- `README.md`: Complete rewrite with Nexus Foundation branding
- Added `BRANDING.md`: Comprehensive branding guidelines
- Added `CHANGELOG.md`: This file

**New Files**:
- `src/branding.py`: Python module for brand colors and styling
- `src/style.css`: Custom CSS with brand colors

### Resource Path Changes

**Old Resource Paths**:
- `/moe/nyarchlinux/customize/*`

**New Resource Paths**:
- `/org/org.nexuspenn.nexaos.customize/*`

### Application ID Changes

**Old Application ID**:
- `moe.nyarchlinux.customize`

**New Application ID**:
- `org.nexuspenn.nexaos.customize`

### Build System Changes

**Meson**:
- Project name: `nexacustomize`
- Version: `1.0.0`
- Updated all install paths and module directories

**Flatpak**:
- App ID: `org.nexuspenn.nexaos.customize`
- Bundle name: `nexacustomize.flatpak`

### Copyright Updates

All source files now include:
```
Copyright 2024 Nexus Foundation
Originally developed by Francesco Caracciolo (2023)
```

### About Dialog Information

- **Application Name**: NexaOS Customize
- **Developer**: Nexus Foundation
- **Version**: 1.0.0
- **Website**: https://nexuspenn.org
- **Issues**: https://github.com/Nexuspenn/NexaCustomize/issues
- **License**: GPL-3.0-or-later

### Credits

- **Nexus Foundation**: Current maintainer and development
- **Francesco Caracciolo**: Original author and developer
- **Nyarch developers**: Original inspiration and foundation

---

## Migration Guide

### For Developers

If you're working with the codebase:

1. **Update Git Remote** (if applicable):
   ```bash
   git remote set-url origin https://github.com/Nexuspenn/NexaCustomize.git
   ```

2. **Clean Previous Build**:
   ```bash
   rm -rf build/
   rm -rf flatpak-app/
   ```

3. **Rebuild Application**:
   ```bash
   meson setup build
   meson compile -C build
   ```

4. **Update Module Imports**:
   - Change `from nyarchcustomize import` → `from nexacustomize import`
   - Update any hardcoded paths referencing `nyarchlinux` or `moe.nyarchlinux`

### For Users

If you had the previous version installed:

1. **Uninstall Old Version**:
   ```bash
   # Flatpak
   flatpak uninstall moe.nyarchlinux.customize
   
   # Or from source
   cd /path/to/old/NexaCustomize
   sudo ninja -C build uninstall
   ```

2. **Install New Version**:
   ```bash
   # Flatpak
   flatpak install flathub org.nexuspenn.nexaos.customize
   
   # Or from source
   git clone https://github.com/Nexuspenn/NexaCustomize.git
   cd NexaCustomize
   ./install.sh
   ```

3. **Settings Migration**:
   - Settings are stored in GSettings under the new schema
   - Old settings from `moe.nyarchlinux.customize` will not be automatically migrated
   - You may need to reconfigure your preferences

### For Package Maintainers

1. **Update Package Names**:
   - Binary: `nexacustomize`
   - Desktop file: `org.nexuspenn.nexaos.customize.desktop`
   - App ID: `org.nexuspenn.nexaos.customize`

2. **Update Dependencies**:
   - GNOME 46+ (recommended)
   - GTK 4.0+
   - Python 3.10+
   - GObject Introspection

3. **Update Install Paths**:
   - Binary: `/usr/bin/nexacustomize` (or appropriate prefix)
   - Data: `/usr/share/nexacustomize/`
   - Desktop file: `/usr/share/applications/`
   - AppData: `/usr/share/metainfo/`
   - Icons: `/usr/share/icons/hicolor/`

### Breaking Changes

⚠️ **Important**: This is a major rebrand with breaking changes:

1. **Application ID Changed**: Any scripts or configs referencing the old app ID need updating
2. **Binary Name Changed**: Update any launchers or scripts calling `nyarchcustomize`
3. **Resource Paths Changed**: Extensions or themes referencing old paths need updates
4. **Settings Schema Changed**: Old GSettings will not migrate automatically

### Compatibility

- **GTK Version**: GTK 4.0+ (no change)
- **GNOME Version**: GNOME 46+ recommended (was 40+)
- **Python Version**: Python 3.10+ (was 3.8+)
- **Architecture**: All architectures supported

---

## Previous Versions

### Version 0.3.6 (Pre-Rebrand)
- Last version under Nyarch branding
- Application ID: `moe.nyarchlinux.customize`
- Developer: Francesco Caracciolo

### Version 0.3.5 and Earlier
- See original repository history for details
- Developed by Francesco Caracciolo
- Based on Nyarch Linux customization tools

---

## Future Plans

### Version 1.1.0 (Planned)
- Enhanced Material You integration
- Additional layout presets
- Improved extension management
- Performance optimizations

### Version 1.2.0 (Planned)
- Custom theme creation
- Profile import/export
- Backup and restore settings
- Advanced customization options

---

For detailed branding guidelines, see [BRANDING.md](BRANDING.md).
For build instructions, see [README.md](README.md).
For issues and support, visit https://github.com/Nexuspenn/NexaCustomize/issues
